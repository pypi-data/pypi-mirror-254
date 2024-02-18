// Copyright (c) 2020 ETH Zurich, Mattia Gollub (mattia.gollub@bsse.ethz.ch)
// Computational Systems Biology group, D-BSSE
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef SAMPLY_ELLIPSOID_H
#define SAMPLY_ELLIPSOID_H

#include <Eigen/Dense>
#include <cmath>
#include <exception>
#include <utility>

#include "intersections_packet.h"
#include "rays_packet.h"
#include "reparametrized_object.h"

namespace samply {

/**
 * @brief Class describing a n-dimensional ellipsoid.
 *
 * @tparam Scalar Type used for intersection operations.
 */
template <typename ScalarType> class Ellipsoid {
  public:
    /**
     * @brief Scalar type used for intersection operations.
     */
    typedef ScalarType Scalar;

    /**
     * @brief Construct a new Ellipsoid object. The ellipsoid is defined as the
     * set { x \in R^d | x = E*y + f, |y| <= 1 }
     * @param E Linear transform from the unit hypersphere to the ellipsoid.
     * @param f Shift from the unit hypersphere to the ellipsoid.
     */
    Ellipsoid(const Matrix<double>& E, const Vector<double>& f);

    /**
     * @brief Construct a new Ellipsoid object representing the unit
     * hypersphere.
     *
     * @param n_dimensions Number of dimensions of the ellipsoid.
     */
    Ellipsoid(const Eigen::Index n_dimensions);

    /**
     * @brief Construct a new Ellipsoid object representing the a hypersphere with the
     * given radius.
     *
     * @param n_dimensions Number of dimensions of the ellipsoid.
     */
    Ellipsoid(const Eigen::Index n_dimensions, const double radius);

    /**
     * @brief Find the intersections between a set of rays and the ellipsoid.
     *
     * @param rays A set of rays for which intersections with the ellipsoid must
     * be found.
     * @return An object describing all the intersections of the rays with the
     * ellipsoid.
     */
    template <typename RaysPacketType>
    void intersect(
        IntersectionsPacket<Scalar>& output_intersections,
        const RaysPacketBase<ScalarType, RaysPacketType>& rays);

    /**
     * @brief Get a reparametrized version of this object such that intersection
     * operations are easy.
     *
     * @return Reparametrized version of this object, containing the
     * transforms mapping between the two parametrizations.
     */
    ReparametrizedObject<Ellipsoid<Scalar>>
    get_optimally_reparametrized_descriptor() const;

    /**
     * @brief Get the dimensionality of the ellipsoid.
     *
     * @return The dimensionality of the ellipsoid.
     */
    Eigen::Index dimensionality() const { return f_.size(); }

    /**
     * @brief Checks whether the ellipsoid is a unit hypersphere or not.
     *
     * @return True if the ellipsoid is a unit hypersphere. False otherwise.
     */
    bool is_standard() const { return is_standard_; }

  private:
    const Matrix<double> E_full_precision;
    const Vector<double> f_full_precision;

    const Matrix<Scalar> E_inv_;
    const Vector<Scalar> f_;
    const double scale_;
    const double scale_squared_;

    const bool is_standard_;
    const bool is_scaled_standard_;

    // Persistent temporary variables, to avoid reallocation at each call.
    Matrix<Scalar> a_, b_, c_;
    Matrix<Scalar> discriminant_;
};

//==============================================================================
//	Ellipsoid public methods implementation.
//==============================================================================

template <typename ScalarType>
Ellipsoid<ScalarType>::Ellipsoid(const Matrix<double>& E, const Vector<double>& f)
    : E_full_precision(E)
    , f_full_precision(f)
    , E_inv_((E.completeOrthogonalDecomposition().pseudoInverse().transpose() *
              E.completeOrthogonalDecomposition().pseudoInverse())
                 .cast<ScalarType>())
    , f_(f.cast<ScalarType>())
    , is_standard_(E.isIdentity() && f.isZero())
    , is_scaled_standard_(false)
    , scale_(std::nan(""))
    , scale_squared_(std::nan(""))
{}

template <typename ScalarType>
Ellipsoid<ScalarType>::Ellipsoid(const Eigen::Index n_dimensions)
    : E_full_precision(Matrix<double>::Identity(n_dimensions, n_dimensions))
    , f_full_precision(Vector<double>::Zero(n_dimensions))
    , E_inv_(Matrix<ScalarType>::Identity(n_dimensions, n_dimensions))
    , f_(Vector<ScalarType>::Zero(n_dimensions))
    , is_standard_(true)
    , is_scaled_standard_(false)
    , scale_(1.0)
    , scale_squared_(1.0)
{}

template <typename ScalarType>
Ellipsoid<ScalarType>::Ellipsoid(const Eigen::Index n_dimensions, const double scale)
    : E_full_precision(Matrix<double>::Identity(n_dimensions, n_dimensions))
    , f_full_precision(Vector<double>::Zero(n_dimensions))
    , E_inv_(Matrix<ScalarType>::Identity(n_dimensions, n_dimensions))
    , f_(Vector<ScalarType>::Zero(n_dimensions))
    , is_standard_(false)
    , is_scaled_standard_(true)
    , scale_(scale)
    , scale_squared_(scale * scale)
{}

template <typename ScalarType>
template <typename RaysPacketType>
void Ellipsoid<ScalarType>::intersect(
    IntersectionsPacket<Scalar>& output_intersections,
    const RaysPacketBase<ScalarType, RaysPacketType>& rays)
{
    // The intersection can be determined by solving the equation :
    // t ^ 2 * d*inv(E)*d + t * 2 * d*inv(E)*(o - f) + (o - f)*inv(E)*(o - f) - 1 = 0
    // If the ellipsoid is a unit hypershpere the equation reduces to :
    // t ^ 2 * d*d + t * 2 * d*o + o * o - 1 = 0

    // Compute coefficients of the quadratic equation.
    if (is_standard_) {
        // If this is a standard ellipsoid we can assume that
        // E = I and f = 0.
        a_ = rays.directions.colwise().squaredNorm();
        b_ = 2 * rays.directions.cwiseProduct(rays.origins).colwise().sum();
        c_ = rays.origins.colwise().squaredNorm().array() - 1;
    }
    else if (is_scaled_standard_) {
        // If this is a scaled standard ellipsoid we can assume that
        // E = I * scale and f = 0.
        a_ = rays.directions.colwise().squaredNorm();
        b_ = 2 * rays.directions.cwiseProduct(rays.origins).colwise().sum();
        c_ = rays.origins.colwise().squaredNorm().array() - scale_squared_;
    }
    else {
        // Otherwise use the formula for the general case.
        auto offsets = (rays.origins.colwise() - f_);
        auto inv_E_times_directions = (E_inv_ * rays.directions);
        auto inv_E_times_offsets = (E_inv_ * offsets);
        a_ = rays.directions.cwiseProduct(inv_E_times_directions).colwise().sum();
        b_ = 2 * rays.directions.cwiseProduct(inv_E_times_offsets).colwise().sum();
        c_ = offsets.cwiseProduct(inv_E_times_offsets).colwise().sum().array() - 1;
    }
    discriminant_ = b_.array().square().matrix() - 4 * a_.cwiseProduct(c_);

    // Compute discriminant and assert that each ray intersects the ellipsoid
    // exactly twice. Otherwise, the origin is not inside the ellipsoid and
    // something went wrong during previous MC steps.
    assert((discriminant_.array() > Scalar(0.0)).all());

    // Obtain the intersection points by solving the quadratic equation.
    output_intersections.segment_starts =
        (-b_ - discriminant_.cwiseSqrt()).cwiseQuotient(2 * a_).transpose();
    output_intersections.segment_ends =
        (-b_ + discriminant_.cwiseSqrt()).cwiseQuotient(2 * a_).transpose();
    output_intersections.num_rays = output_intersections.segment_starts.size();
    output_intersections.one_ray_one_intersection = true;
}

template <typename ScalarType>
ReparametrizedObject<Ellipsoid<ScalarType>>
Ellipsoid<ScalarType>::get_optimally_reparametrized_descriptor() const
{
    AffineTransform<double> from_parametrization =
        AffineTransform<double>(E_full_precision, f_full_precision);
    return ReparametrizedObject<Ellipsoid<Scalar>>(
        Ellipsoid<Scalar>(E_full_precision.cols()), from_parametrization,
        from_parametrization.inverse());
}

} // namespace samply

#endif