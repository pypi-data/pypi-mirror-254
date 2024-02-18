// Copyright (c) 2020 ETH Zurich, Mattia Gollub (mattia.gollub@bsse.ethz.ch)
// Computational Systems Biology group, D-BSSE
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef SAMPLY_INTERSECTIONS_PACKET_WITH_WEIGHTS_H
#define SAMPLY_INTERSECTIONS_PACKET_WITH_WEIGHTS_H

#include <Eigen/Dense>

#include "commons.h"
#include "intersections_packet.h"

namespace samply {

template <typename Scalar>
struct IntersectionsPacketWithWeights : public IntersectionsPacket<Scalar> {
    Vector<Scalar> weights;

    IntersectionsPacketWithWeights(const Vector<Scalar>& segment_starts,
                                   const Vector<Scalar>& segment_ends,
                                   const Vector<Scalar>& weights)
        : IntersectionsPacket<Scalar>(segment_starts, segment_ends), weights(weights)
    {
    }

    IntersectionsPacketWithWeights(const Vector<Scalar>& segment_starts,
                                   const Vector<Scalar>& segment_ends,
                                   const Eigen::VectorXi& ray_indices,
                                   const Eigen::Index num_rays,
                                   const Vector<Scalar>& weights)
        : IntersectionsPacket<Scalar>(
              segment_starts, segment_ends, ray_indices, num_rays),
          weights(weights)
    {
    }

    template <typename IndexList>
    IntersectionsPacketWithWeights<Scalar> operator()(
        const IndexList& ray_indices) const
    {
        if (!this->one_ray_one_intersection)
            throw std::runtime_error("Not implemented yet.");
        return IntersectionsPacketWithWeights<Scalar>(this->segment_starts(ray_indices),
                                                      this->segment_ends(ray_indices),
                                                      weights(ray_indices));
    }

    IntersectionsPacketWithWeights<Scalar> intersect(
        const IntersectionsPacketWithWeights<Scalar>& other) const
    {
        if (!other.one_ray_one_intersection || !this->one_ray_one_intersection)
            throw std::runtime_error(
                "IntersectionsPacket::intersect can "
                "be used only if all rays have a single intersection");

        if (!((this->segment_ends.array() > other.segment_starts.array()) &&
              (other.segment_ends.array() > this->segment_starts.array()))
                 .all()) {
            throw std::runtime_error(
                "The intersections don't overlap on "
                "at least one ray");
        }

        return IntersectionsPacketWithWeights<Scalar>(
            this->segment_starts.cwiseMax(other.segment_starts),
            this->segment_ends.cwiseMin(other.segment_ends), weights);
    }

    template <typename Function>
    Vector<Scalar> for_each_ray(Function&& ray_function) const
    {
        assert(!this->one_ray_one_intersection);
        Eigen::Index current_ray = 0;
        Eigen::Index current_ray_start_idx = 0;
        Vector<Scalar> result(this->num_rays);

        for (Eigen::Index segment_idx = 0; segment_idx < this->segment_starts.size();
             segment_idx++) {
            if (segment_idx + 1 == this->segment_starts.size() ||
                this->ray_indices(segment_idx + 1) != current_ray) {
                // The current segment belongs to a new ray.
                Eigen::Index num_ray_segments = segment_idx - current_ray_start_idx + 1;

                // Execute the function on the ray we just completed.
                result(current_ray) = ray_function(
                    this->segment_starts.segment(current_ray_start_idx,
                                                 num_ray_segments),
                    this->segment_ends.segment(current_ray_start_idx, num_ray_segments),
                    weights.segment(current_ray_start_idx, num_ray_segments),
                    current_ray);

                // Advance indices to start a new ray.
                if (segment_idx + 1 != this->segment_starts.size())
                    assert(this->ray_indices(segment_idx + 1) == current_ray + 1);
                current_ray_start_idx = segment_idx + 1;
                current_ray++;
            }
        }

        return result;
    }
};

}  // namespace samply

#endif