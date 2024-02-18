// Copyright (c) 2020 ETH Zurich, Mattia Gollub (mattia.gollub@bsse.ethz.ch)
// Computational Systems Biology group, D-BSSE
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef SAMPLY_POLYTOPE_H
#define SAMPLY_POLYTOPE_H

#include <Eigen/Dense>
#include <utility>

#include "axis_rays_packet.h"
#include "commons.h"
#include "intersections_packet.h"
#include "rays_packet.h"
#include "reparametrized_object.h"

namespace samply {

/**
 * @brief Class describing a n-dimensional polytope.
 *
 * @tparam Scalar Type used for intersection operations.
 */
template <typename ScalarType> class Polytope {
  public:
    /**
     * @brief Scalar type used for intersection operations.
     */
    typedef ScalarType Scalar;

    /**
     * @brief Construct a new Polytope object. The polytope is defined as the
     * set { x \in R^d | G*x <= h } and is assumed to have maximum isotropy.
     *
     * @param G NumConstraints-by-NumDimensions matrix containing the normal
     * vectors of the planes constraining the polytope.
     * @param h NumConstraints-by-1 vector containing the offsets of the planes
     * constraining the polytope.
     */
    Polytope(const Matrix<double>& G, const Matrix<double>& h)
        : Polytope(
              G, h, AffineTransform<double>::identity(static_cast<Index>(G.cols())))
    {}

    /**
     * @brief Construct a new Polytope object. The polytope is defined as the
     * set { x \in R^d | G*x <= h }
     *
     * @param G NumConstraints-by-NumDimensions matrix containing the normal
     * vectors of the planes constraining the polytope.
     * @param h NumConstraints-by-1 vector containing the offsets of the planes
     * constraining the polytope.
     * @param from_max_isotropy_frame_transform Transform from a coordinate
     * frame in which the polytope has maximum isotropy to the frame in which G
     * and h are given.
     */
    Polytope(
        const Matrix<double>& G,
        const Matrix<double>& h,
        const AffineTransform<double>& from_optimal_frame_transform)
        : G_full_precision(G)
        , h_full_precision(h)
        , G_(G.cast<Scalar>())
        , h_(h.cast<Scalar>())
        , from_optimal_frame_transform_(from_optimal_frame_transform)
        , numerator_cache_()
        , denominator_cache_()
    {
        // Make sure that the constraint matrix doesn't contain zero-rows.
        assert((G.cwiseAbs().rowwise().sum().array() != Scalar(0.0)).all());
    }

    /**
     * @brief Set the current state of the Markov Chains. This is used to cache
     * values that speed up ray-object intersections.
     *
     * @param state Current state of the Markov Chains.
     */
    void initialize(const Matrix<Scalar>& state);

    /**
     * @brief Find the intersections between a set of rays and the polytope.
     *
     * @param rays A set of rays for which intersections with the polytope must
     * be found.
     * @return An object describing all the intersections of the rays with the
     * polytope.
     */
    void intersect(
        IntersectionsPacket<Scalar>& output_intersections,
        const AxisRaysPacket<Scalar>& rays);

    /**
     * @brief Find the intersections between a set of rays and the polytope.
     *
     * @param rays A set of rays for which intersections with the polytope must
     * be found.
     * @return An object describing all the intersections of the rays with the
     * polytope.
     */
    template <typename RaysPacketType>
    void intersect(
        IntersectionsPacket<Scalar>& output_intersections,
        const RaysPacketBase<ScalarType, RaysPacketType>& rays);

    /**
     * @brief Update the positions of the Markov Chains relative to the previous
     * state, in the directions given by the rays for which intersections where
     * last tested.
     *
     * @param t Distance of the new states along each ray.
     */
    void update_position(const Vector<Scalar>& t);

    /**
     * @brief Get the dimensionality of the polytope.
     *
     * @return The dimensionality of the polytope.
     */
    Eigen::Index dimensionality() const { return G_.cols(); }

    /**
     * @brief Get a reparametrized version of this object such that intersection
     * operations are easy.
     *
     * @return Reparametrized version of this object, containing the
     * transforms mapping between the two parametrizations.
     */
    ReparametrizedObject<Polytope<Scalar>>
    get_optimally_reparametrized_descriptor() const;

  private:
    // NumConstraints-by-NumDimensions matrix containing the normal
    // vectors of the planes constraining the polytope.
    const Matrix<double> G_full_precision;

    // NumConstraints-by-1 vector containing the offsets of the planes
    // constraining the polytope.
    const Vector<double> h_full_precision;

    // NumConstraints-by-NumDimensions matrix containing the normal
    // vectors of the planes constraining the polytope.
    const Matrix<Scalar> G_;

    // NumConstraints-by-1 vector containing the offsets of the planes
    // constraining the polytope.
    const Vector<Scalar> h_;

    // Transform from a coordinate frame in which intersection computations are easier.
    const AffineTransform<double> from_optimal_frame_transform_;

    // Matrix caching the numerator and denominator used in the last
    // intersection tests.
    Matrix<Scalar> numerator_cache_;
    Matrix<Scalar> denominator_cache_;

    // Persistent temporary variables, to avoid reallocation of the matrices at each
    // call.
    Matrix<Scalar> all_intersections_t_inv_;
    Vector<Scalar> segment_starts_;
    Vector<Scalar> segment_ends_;
};

//==============================================================================
//	Polytope public methods implementation.
//==============================================================================

template <typename ScalarType>
void Polytope<ScalarType>::initialize(const Matrix<ScalarType>& state)
{
    numerator_cache_ = G_ * state - h_.replicate(1, state.cols());
}

template <typename ScalarType>
void Polytope<ScalarType>::intersect(
    IntersectionsPacket<ScalarType>& output_intersections,
    const AxisRaysPacket<ScalarType>& rays)
{
    constexpr Scalar infinity = std::numeric_limits<Scalar>::infinity();

    // Find all intersections with the constraints. Note that if any
    // element of G*directions is zero, NaNs will be generated. Since
    // IEC 559 guarantees that <= and >= involving NaNs return false, these
    // will be replaced by infinity when choosing the closest intersection
    // later on.

    // Faster than Eigen's slicing, which internally allocates space for copies of the
    // indices.
    denominator_cache_.resize(G_.rows(), rays.directions.size());
    for (Index i = 0; i < rays.directions.size(); i++)
        denominator_cache_.col(i) = G_.col(rays.directions(i));

    all_intersections_t_inv_ = -denominator_cache_.cwiseQuotient(numerator_cache_);

    segment_starts_ = all_intersections_t_inv_.colwise().minCoeff().cwiseInverse();
    segment_ends_ = all_intersections_t_inv_.colwise().maxCoeff().cwiseInverse();

    output_intersections.segment_starts =
        (segment_starts_.array() <= 0.0).select(segment_starts_, -infinity);
    output_intersections.segment_ends =
        (segment_ends_.array() >= 0.0).select(segment_ends_, infinity);
    output_intersections.num_rays = output_intersections.segment_starts.size();
    output_intersections.one_ray_one_intersection = true;
}

template <typename ScalarType>
template <typename RaysPacketType>
void Polytope<ScalarType>::intersect(
    IntersectionsPacket<ScalarType>& output_intersections,
    const RaysPacketBase<ScalarType, RaysPacketType>& rays)
{
    constexpr Scalar infinity = std::numeric_limits<Scalar>::infinity();

    // Find all intersections with the constraints. Note that if any
    // element of G*directions is zero, NaNs will be generated. Since
    // IEC 559 guarantees that <= and >= involving NaNs return false, these
    // will be replaced by infinity when choosing the closest intersection
    // later on.
    denominator_cache_.noalias() = G_ * rays.directions;

    all_intersections_t_inv_ = -denominator_cache_.cwiseQuotient(numerator_cache_);

    segment_starts_ = all_intersections_t_inv_.colwise().minCoeff().cwiseInverse();
    segment_ends_ = all_intersections_t_inv_.colwise().maxCoeff().cwiseInverse();

    output_intersections.segment_starts =
        (segment_starts_.array() <= 0.0).select(segment_starts_, -infinity);
    output_intersections.segment_ends =
        (segment_ends_.array() >= 0.0).select(segment_ends_, infinity);
    output_intersections.num_rays = output_intersections.segment_starts.size();
    output_intersections.one_ray_one_intersection = true;
}

template <typename ScalarType>
void Polytope<ScalarType>::update_position(const Vector<Scalar>& t)
{
    numerator_cache_ += denominator_cache_ * t.asDiagonal();
}

template <typename ScalarType>
ReparametrizedObject<Polytope<ScalarType>>
Polytope<ScalarType>::get_optimally_reparametrized_descriptor() const
{
    AffineTransform<double> from_parametrization = from_optimal_frame_transform_;
    AffineTransform<double> to_parametrization =
        from_optimal_frame_transform_.inverse();

    return ReparametrizedObject<Polytope<Scalar>>(
        Polytope<Scalar>(
            G_full_precision * from_parametrization.get_linear(),
            h_full_precision - G_full_precision * from_parametrization.get_shift(),
            AffineTransform<double>::identity(static_cast<Index>(G_.cols()))),
        from_parametrization, to_parametrization);
}

} // namespace samply

#endif