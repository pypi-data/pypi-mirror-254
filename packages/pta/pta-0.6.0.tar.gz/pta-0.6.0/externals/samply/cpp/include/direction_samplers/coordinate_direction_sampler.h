// Copyright (c) 2021 ETH Zurich, Mattia Gollub (mattia.gollub@bsse.ethz.ch)
// Computational Systems Biology group, D-BSSE
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef SAMPLY_COORDINATE_DIRECTION_SAMPLER_H
#define SAMPLY_COORDINATE_DIRECTION_SAMPLER_H

#include <Eigen/Dense>

#include "axis_rays_packet.h"
#include "commons.h"
#include "helpers/sampling_helper.h"
#include "reparametrized_object.h"

namespace samply {

/**
 * @brief Samples directions aligned with the axes of the standard basis.
 *
 * @tparam Scalar Type used to describe the directions.
 */
template <typename ScalarType> class CoordinateDirectionSampler {
  public:
    /**
     * @tparam Scalar Type used to describe the directions.
     */
    typedef ScalarType Scalar;

    /**
     * @brief Type of rays packets constructed from this sampler.
     */
    typedef AxisRaysPacket<ScalarType> RaysPacketType;

    /**
     * @brief Type of the directions.
     */
    typedef IndexVector DirectionsType;

    CoordinateDirectionSampler(const AffineTransform<ScalarType>& directions_transform)
        : directions_transform_(directions_transform)
        , dimensionality_(static_cast<Index>(directions_transform.get_linear().cols()))
    {}

    void get_directions(DirectionsType& output_directions, const Index num_directions);

    /**
     * @brief Get the dimensionality of the sampled directions.
     *
     * @return The dimensionality of the sampled directions.
     */
    Index dimensionality() const { return dimensionality_; }

    ReparametrizedObject<CoordinateDirectionSampler<ScalarType>>
    get_optimally_reparametrized_descriptor() const;

  private:
    const AffineTransform<ScalarType> directions_transform_;
    const Index dimensionality_;

    // Helper object used to generate random numbers.
    SamplingHelper sampling_helper_;
};

//==============================================================================
//	CoordinateDirectionSampler public methods implementation.
//==============================================================================

template <typename ScalarType>
void CoordinateDirectionSampler<ScalarType>::get_directions(
    typename CoordinateDirectionSampler<ScalarType>::DirectionsType& output_directions,
    const Index num_directions)
{
    if (!directions_transform_.is_identity())
        throw std::runtime_error("CoordinateDirectionSampler must be reparametrized");
    sampling_helper_.get_random_integers(
        output_directions, 0, dimensionality() - 1, num_directions);
}

template <typename ScalarType>
ReparametrizedObject<CoordinateDirectionSampler<ScalarType>>
CoordinateDirectionSampler<ScalarType>::get_optimally_reparametrized_descriptor() const
{
    return ReparametrizedObject<CoordinateDirectionSampler<Scalar>>(
        CoordinateDirectionSampler<Scalar>(
            AffineTransform<double>::identity(dimensionality())),
        directions_transform_, directions_transform_.inverse());
}

} // namespace samply

#endif