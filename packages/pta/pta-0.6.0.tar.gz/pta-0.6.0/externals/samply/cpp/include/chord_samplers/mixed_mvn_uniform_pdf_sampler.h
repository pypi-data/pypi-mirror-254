// Copyright (c) 2020 ETH Zurich, Mattia Gollub (mattia.gollub@bsse.ethz.ch)
// Computational Systems Biology group, D-BSSE
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef SAMPLY_MIXED_MVN_UNIFORM_PDF_SAMPLER_H
#define SAMPLY_MIXED_MVN_UNIFORM_PDF_SAMPLER_H

#include "helpers/sampling_helper.h"
#include "intersections_packet.h"
#include "mvn_pdf_sampler.h"
#include "rays_packet.h"
#include "reparametrized_object.h"
#include "uniform_pdf_sampler.h"

namespace samply {

/**
 * @brief Class for sampling along a ray crossing a mixed MVN-uniform
 * probability distribution.
 *
 * @tparam ScalarType Scalar type for sampling operations.
 */
template <typename ScalarType>
class MixedMvnUniformPdfSampler : public MvnPdfSampler<ScalarType>,
                                  public UniformPdfSampler<ScalarType> {
  public:
    /**
     * @brief Scalar type used for sampling operations.
     */
    typedef ScalarType Scalar;

    /**
     * @brief Construct a new instance of the MixedMvnUniformPdf Sampler class.
     *
     * @param samples_transform Transform from the unit MVN to the desired MVN.
     * @param vars_to_mvn_vars Transform from the sampling variables (including
     * the uniform ones) to the MVN-distributed variables. This is usually a row
     * selection transform.
     */
    MixedMvnUniformPdfSampler(
        const AffineTransform<double>& samples_transform,
        const AffineTransform<double>& vars_to_mvn_vars)
        : MvnPdfSampler<ScalarType>(samples_transform)
        , UniformPdfSampler<ScalarType>(vars_to_mvn_vars.get_linear().cols())
        , vars_to_mvn_vars_(vars_to_mvn_vars)
    {}

    /**
     * @brief Construct a new instance of the MixedMvnUniformPdfSampler class.
     * This is a degenerate case in which all variables are uniformly
     * distributed.
     *
     * @param num_variables Dimensionality of the space on which the
     * probability distribution is defined.
     */
    MixedMvnUniformPdfSampler(size_t num_variables)
        : MvnPdfSampler<ScalarType>(num_variables)
        , UniformPdfSampler<ScalarType>(num_variables)
        , vars_to_mvn_vars_(
              Matrix<double>::Identity(num_variables, num_variables),
              Vector<double>::Zero(num_variables))
    {}

    /**
     * @brief Samples a point along each of the specified rays.
     *
     * @param rays Rays along which points must be sampled.
     * @param intersections Intersection points defining the sections on each
     * ray from which the points can be sampled.
     * @param sampling_helper Helper object for generating random numbers.
     * @return Vector containing the sampled points on each ray.
     */
    void sample1d(
        Vector<ScalarType>& result_t,
        const RaysPacket<Scalar>& rays,
        const IntersectionsPacket<Scalar>& intersections,
        SamplingHelper& sampling_helper);

    /**
     * @brief Samples a point along each of the specified rays.
     *
     * @param rays Rays along which points must be sampled.
     * @param intersections Intersection points defining the sections on each
     * ray from which the points can be sampled.
     * @param sampling_helper Helper object for generating random numbers.
     * @return Vector containing the sampled points on each ray.
     */
    void sample1d(
        Vector<ScalarType>& result_t,
        const AxisRaysPacket<Scalar>& rays,
        const IntersectionsPacket<Scalar>& intersections,
        SamplingHelper& sampling_helper);

    /**
     * @brief Get a reparametrized version of this object such that sampling
     * operations are easy.
     *
     * @return Reparametrized version of this object, containing the
     * transforms mapping between the two parametrizations.
     */
    ReparametrizedObject<MixedMvnUniformPdfSampler<Scalar>>
    get_optimally_reparametrized_sampler() const;

  protected:
    AffineTransform<double> vars_to_mvn_vars_;

    // Persistent temporary variables, to avoid reallocation at each call.
    std::vector<Eigen::Index> non_degenerate_ray_ids_;
    std::vector<Eigen::Index> degenerate_ray_ids_;
};

//==============================================================================
//	MixedMvnUniformPdfSampler public methods implementation.
//==============================================================================

template <typename ScalarType>
inline void MixedMvnUniformPdfSampler<ScalarType>::sample1d(
    Vector<ScalarType>& result_t,
    const RaysPacket<Scalar>& rays,
    const IntersectionsPacket<Scalar>& intersections,
    SamplingHelper& sampling_helper)
{
    result_t.resize(intersections.num_rays);
    Eigen::Index n_rays = rays.origins.cols();
    non_degenerate_ray_ids_.resize(0);
    degenerate_ray_ids_.resize(0);
    non_degenerate_ray_ids_.reserve(n_rays);
    degenerate_ray_ids_.reserve(n_rays);

    for (Eigen::Index i = 0; i < n_rays; i++) {
        if (rays.directions.col(i).isZero())
            degenerate_ray_ids_.push_back(i);
        else
            non_degenerate_ray_ids_.push_back(i);
    }

    if (degenerate_ray_ids_.size() == 0)
        // Special case where all the rays are non-degenerate.
        MvnPdfSampler<Scalar>::sample1d(result_t, rays, intersections, sampling_helper);
    else if (non_degenerate_ray_ids_.size() > 0) {
        // For the non-degenerated rays (i.e. rays that have support from the
        // MVN distributed parameters), sample the next points according to the
        // MVN distribution.
        Vector<Scalar> temp_t;
        MvnPdfSampler<Scalar>::sample1d(
            temp_t, rays(non_degenerate_ray_ids_),
            intersections(non_degenerate_ray_ids_), sampling_helper);
        result_t(non_degenerate_ray_ids_) = temp_t;
    }
    if (degenerate_ray_ids_.size() > 0) {
        // For the degenerated rays, sample the next points uniformly.
        Vector<Scalar> temp_t;
        UniformPdfSampler<Scalar>::sample1d(
            temp_t, rays(degenerate_ray_ids_), intersections(degenerate_ray_ids_),
            sampling_helper);
        result_t(degenerate_ray_ids_) = temp_t;
    }
}

template <typename ScalarType>
inline void MixedMvnUniformPdfSampler<ScalarType>::sample1d(
    Vector<ScalarType>& result_t,
    const AxisRaysPacket<Scalar>& in_rays,
    const IntersectionsPacket<Scalar>& in_intersections,
    SamplingHelper& sampling_helper)
{
    return sample1d(
        result_t, AffineTransform<Scalar>::identity(in_rays.origins.rows()) * in_rays,
        in_intersections, sampling_helper);
}

template <typename ScalarType>
ReparametrizedObject<MixedMvnUniformPdfSampler<ScalarType>>
MixedMvnUniformPdfSampler<ScalarType>::get_optimally_reparametrized_sampler() const
{
    // TODO: computation of the inverse fails.
    AffineTransform<double> from_optimal_parametrization =
        vars_to_mvn_vars_.inverse() * MvnPdfSampler<ScalarType>::samples_transform_;
    AffineTransform<double> to_optimal_parametrization =
        MvnPdfSampler<ScalarType>::samples_transform_.inverse() * vars_to_mvn_vars_;

    return ReparametrizedObject<MixedMvnUniformPdfSampler<Scalar>>(
        MixedMvnUniformPdfSampler<Scalar>(
            MvnPdfSampler<ScalarType>::samples_transform_.get_shift().size()),
        from_optimal_parametrization, to_optimal_parametrization);
}

} // namespace samply

#endif