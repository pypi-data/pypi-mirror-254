// Copyright (c) 2020 ETH Zurich, Mattia Gollub (mattia.gollub@bsse.ethz.ch)
// Computational Systems Biology group, D-BSSE
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef SAMPLY_UNIFORM_PDF_SAMPLER_H
#define SAMPLY_UNIFORM_PDF_SAMPLER_H

#include "commons.h"
#include "helpers/sampling_helper.h"
#include "intersections_packet.h"
#include "rays_packet.h"
#include "reparametrized_object.h"

namespace samply {

/**
 * @brief Class for uniformly sampling along a ray.
 *
 * @tparam ScalarType Scalar type for sampling operations.
 */
template <typename ScalarType> class UniformPdfSampler {
  public:
    /**
     * @brief Scalar type used for sampling operations.
     */
    typedef ScalarType Scalar;

    /**
     * @brief Construct a new instance of the UniformPdfSampler class.
     *
     * @param num_dimensions Dimensionality of the space on which the
     * probability distribution is defined.
     */
    UniformPdfSampler(const Eigen::Index num_dimensions);

    /**
     * @brief Samples a point along each of the specified rays.
     *
     * @tparam RaysPacketType Type of object describing the rays.
     * @param rays Rays along which points must be sampled.
     * @param intersections Intersection points defining the sections on each
     * ray from which the points can be sampled.
     * @param sampling_helper Helper object for generating random numbers.
     * @return Vector containing the sampled points on each ray.
     */
    template <typename RaysPacketType>
    void sample1d(
        Vector<ScalarType>& result_t,
        const RaysPacketType& rays,
        const IntersectionsPacket<Scalar>& intersections,
        SamplingHelper& sampling_helper);

    /**
     * @brief Get a reparametrized version of this object such that sampling
     * operations are easy.
     *
     * @return Reparametrized version of this object, containing the
     * transforms mapping between the two parametrizations.
     */
    ReparametrizedObject<UniformPdfSampler>
    get_optimally_reparametrized_sampler() const;

  private:
    Eigen::Index num_dimensions_;

    // Persistent temporary variables, to avoid reallocation at each call.
    Vector<Scalar> weights_;
};

//==============================================================================
//	UniformPdfSampler public methods implementation.
//==============================================================================

template <typename ScalarType>
UniformPdfSampler<ScalarType>::UniformPdfSampler(const Eigen::Index num_dimensions)
    : num_dimensions_(num_dimensions)
{}

template <typename ScalarType>
template <typename RaysPacketType>
inline void UniformPdfSampler<ScalarType>::sample1d(
    Vector<ScalarType>& result_t,
    const RaysPacketType& rays,
    const IntersectionsPacket<ScalarType>& intersections,
    SamplingHelper& sampling_helper)
{
    if (intersections.one_ray_one_intersection) {
        // If each ray has exactly one segment we sample on those segments
        // directly.
        result_t = sampling_helper.get_random_uniform(
            intersections.segment_starts, intersections.segment_ends);
    }
    else {
        // Otherwise, for each ray we need to first sample one out of the
        // segments belonging to the ray and then sample a point from it.
        auto sample_on_segments_union = [&](const auto& segment_starts,
                                            const auto& segment_ends,
                                            const Eigen::Index ray_index) -> Scalar {
            // Choose the segment from which the next point must be sampled.
            const Eigen::Index num_segments = segment_starts.size();
            if (weights_.size() < num_segments)
                weights_.resize(num_segments);
            auto segment_weights = weights_.head(num_segments);

            segment_weights = segment_ends - segment_starts;
            Eigen::Index sampled_segment_idx =
                sampling_helper.sample_index_with_weights<Scalar>(segment_weights);

            // Sample the next point uniformly on the chosen segment.
            return sampling_helper.get_random_uniform_scalar(
                segment_starts(sampled_segment_idx), segment_ends(sampled_segment_idx));
        };

        // Apply the sampling function to each ray.
        result_t.resize(intersections.num_rays);
        intersections.for_each_ray(result_t, sample_on_segments_union);
    }
}

template <typename ScalarType>
ReparametrizedObject<UniformPdfSampler<ScalarType>>
UniformPdfSampler<ScalarType>::get_optimally_reparametrized_sampler() const
{
    // Any parametrization is equally good for uniform sampling.
    return ReparametrizedObject<UniformPdfSampler<Scalar>>(
        UniformPdfSampler<Scalar>(num_dimensions_));
}

} // namespace samply

#endif