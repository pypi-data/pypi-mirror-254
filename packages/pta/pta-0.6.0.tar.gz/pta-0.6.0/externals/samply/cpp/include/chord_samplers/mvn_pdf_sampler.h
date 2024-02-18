// Copyright (c) 2020 ETH Zurich, Mattia Gollub (mattia.gollub@bsse.ethz.ch)
// Computational Systems Biology group, D-BSSE
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef SAMPLY_MVN_PDF_SAMPLER_H
#define SAMPLY_MVN_PDF_SAMPLER_H

#include "axis_rays_packet.h"
#include "commons.h"
#include "helpers/sampling_helper.h"
#include "intersections_packet_with_weights.h"
#include "rays_packet.h"
#include "reparametrized_object.h"
#include <cmath>

namespace samply {

/**
 * @brief Class for sampling along a ray crossing a Multivariate Normal
 * Distribution (MVN).
 *
 * @tparam ScalarType Scalar type for sampling operations.
 */
template <typename ScalarType> class MvnPdfSampler {
  public:
    /**
     * @brief Scalar type used for sampling operations.
     */
    typedef ScalarType Scalar;

    /**
     * @brief Construct a new instance of the MvnPdfSampler class with zero mean
     * and identity convariance.
     *
     * @param num_variables Number of variables in the MVN.
     */
    MvnPdfSampler(size_t num_variables)
        : is_standard_(true)
        , samples_transform_(
              Matrix<double>::Identity(num_variables, num_variables),
              Vector<double>::Zero(num_variables))
    {}

    /**
     * @brief Construct a new instance of the MvnPdfSampler class.
     *
     * @param samples_transform Transform from the unit MVN to desired MVN.
     */
    MvnPdfSampler(const AffineTransform<double>& samples_transform)
        : samples_transform_(samples_transform)
        , is_standard_(false)
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
    ReparametrizedObject<MvnPdfSampler<Scalar>>
    get_optimally_reparametrized_sampler() const;

    const Vector<Scalar>& get_last_sampled_ts() const { return last_sampled_ts_; }

  protected:
    AffineTransform<double> samples_transform_;

    bool is_standard_;

    Vector<Scalar> last_sampled_ts_;

    // Persistent temporary variables, to avoid reallocation at each call.
    Vector<Scalar> stds_square_;
    Vector<Scalar> stds_;
    Vector<Scalar> means_;
    Vector<Scalar> weights_;
};

//==============================================================================
//	MvnPdfSampler public methods implementation.
//==============================================================================

template <typename ScalarType>
inline void MvnPdfSampler<ScalarType>::sample1d(
    Vector<ScalarType>& result_t,
    const RaysPacket<Scalar>& rays,
    const IntersectionsPacket<Scalar>& intersections,
    SamplingHelper& sampling_helper)
{
    if (!is_standard_)
        throw std::runtime_error("MvnPdfSampler must be reparametrized");
    result_t.resize(intersections.num_rays);

    // Compute mean and standard deviation of the Gaussian distributions on the
    // chords. This is obtained by inserting the ray equations into the MVN
    // density formulas and writing the result in the form of a Gaussian over t.
    stds_square_ =
        (rays.directions.array().square()).colwise().sum().transpose().cwiseInverse();
    stds_ = stds_square_.array().sqrt();
    means_ = (rays.directions.cwiseProduct(-rays.origins))
                 .colwise()
                 .sum()
                 .transpose()
                 .cwiseProduct(stds_square_);

    if (intersections.one_ray_one_intersection) {
        for (Eigen::Index i = 0; i < intersections.num_rays; i++) {
            if (rays.directions.col(i).isZero()) {
                result_t(i) = sampling_helper.get_random_uniform_scalar(
                    intersections.segment_starts(i), intersections.segment_ends(i));
            }
            else {
                result_t(i) = sampling_helper.get_random_truncated_normal(
                    means_[i], stds_[i], intersections.segment_starts(i),
                    intersections.segment_ends(i));
            }
        }
    }
    else {
        // Otherwise we need to first sample a segment from all the segments
        // belonging to each ray and then sample a point from it.
        auto sample_on_segments_union = [&](const auto& segment_starts,
                                            const auto& segment_ends,
                                            const Eigen::Index ray_index) -> Scalar {
            // Choose the segment from which the next point must be sampled.
            const Eigen::Index num_segments = segment_starts.size();
            if (weights_.size() < num_segments)
                weights_.resize(num_segments);
            auto segment_weights = weights_.head(num_segments);
            sampling_helper.get_normal_cdf_interval<Scalar>(
                segment_weights, segment_starts, segment_ends, means_[ray_index],
                stds_[ray_index]);

            if (!(segment_weights.array() > 0).any()) {
                return 0;
            }
            else {
                const Eigen::Index sampled_segment_idx =
                    sampling_helper.sample_index_with_weights<Scalar>(segment_weights);

                // Sample the next point uniformly on the chosen segment.
                return sampling_helper.get_random_truncated_normal(
                    means_[ray_index], stds_[ray_index],
                    segment_starts(sampled_segment_idx),
                    segment_ends(sampled_segment_idx));
            }
        };

        // For each ray, identify the segments belonging to it and sample from
        // union.
        intersections.for_each_ray(result_t, sample_on_segments_union);
    }

    last_sampled_ts_ = result_t;
}

template <typename ScalarType>
inline void MvnPdfSampler<ScalarType>::sample1d(
    Vector<ScalarType>& result_t,
    const AxisRaysPacket<Scalar>& in_rays,
    const IntersectionsPacket<Scalar>& in_intersections,
    SamplingHelper& sampling_helper)
{
    sample1d(
        result_t, AffineTransform<Scalar>::identity(in_rays.origins.rows()) * in_rays,
        in_intersections, sampling_helper);
}

template <typename ScalarType>
ReparametrizedObject<MvnPdfSampler<ScalarType>>
MvnPdfSampler<ScalarType>::get_optimally_reparametrized_sampler() const
{
    return ReparametrizedObject<MvnPdfSampler<Scalar>>(
        MvnPdfSampler<Scalar>(samples_transform_.get_shift().size()),
        samples_transform_, samples_transform_.inverse());
}

} // namespace samply

#endif