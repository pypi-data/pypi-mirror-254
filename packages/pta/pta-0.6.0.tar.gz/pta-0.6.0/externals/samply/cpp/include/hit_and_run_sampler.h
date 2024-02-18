// Copyright (c) 2021 ETH Zurich, Mattia Gollub (mattia.gollub@bsse.ethz.ch)
// Computational Systems Biology group, D-BSSE
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef SAMPLY_HIT_AND_RUN_H
#define SAMPLY_HIT_AND_RUN_H

#include "commons.h"
#include "helpers/sampling_helper.h"
#include "hit_and_run_transforms.h"
#include "intersections_packet.h"
#include "markov_chain.h"
#include "rays_packet.h"
#include "reparametrized_object.h"

namespace samply {

/**
 * @brief Implements hit-and-run sampling with general space descriptors and
 * probability distributions.
 *
 * The sampler supports simulation of multiple chains in parallel, which is
 * computationally more efficient than simulating each chain in a separate
 * sampler because of optimization of linear algebra operations.
 *
 * @tparam Scalar Floating point type used in the simulation.
 * @tparam NumDimensions Number of dimensions of the sampling space.
 * @tparam NumChains Number of chains to pack in a single simulation. Packed
 * chains can be simulated faster than using multiple parallel samplers.
 * @tparam SpaceDescriptor Type of the descriptor used to constrain the sampling
 * space.
 * @tparam ChordSampler Type of the sampler used for sampling on the
 * 1-dimensional chord at each step of the simulation.
 * @tparam Type of the logger used for monitoring the state of the simulation.
 */
template <
    typename Scalar,
    template <typename>
    typename DirectionSampler,
    template <typename>
    typename SpaceDescriptor,
    template <typename>
    typename ChordSampler,
    template <typename, typename>
    typename Logger>

class HitAndRunSampler : public MarkovChain<
                             HitAndRunSampler<
                                 Scalar,
                                 DirectionSampler,
                                 SpaceDescriptor,
                                 ChordSampler,
                                 Logger>,
                             Matrix<Scalar>,
                             Matrix<Scalar>,
                             Logger> {
  public:
    /**
     * @brief Base class of the sampler providing general operations for Markov
     * Chains.
     */
    typedef MarkovChain<HitAndRunSampler, Matrix<Scalar>, Matrix<Scalar>, Logger> Base;

    /**
     * @brief The type of the class providing the direction sampler.
     */
    typedef DirectionSampler<Scalar> DirectionSamplerType;

    /**
     * @brief The type of the descriptor of the sampling space.
     */
    typedef SpaceDescriptor<Scalar> DescriptorType;

    /**
     * @brief The type of the 1D sampler.
     */
    typedef ChordSampler<Scalar> ChordSamplerType;

    // Make sure that the MarkovChain class can access the protected methods of
    // this, in particular the next_state() implementation.
    friend Base;

    /**
     * @brief The type of a state of the simulation.
     */
    typedef typename Base::State State;
    typedef typename Base::InternalState InternalState;

    /**
     * @brief Construct a new HitAndRunSampler object.
     *
     * @param descriptor Descriptor of the bounds of the sampling space.
     * @param sampler Object used for sampling points on the 1-d chord at each
     * step of the simulation.
     * @param initial_state Initial state of the chain.
     * @param logger Instance of the logger used to monitor the state of the
     * simulation.
     */
    HitAndRunSampler(
        const DirectionSampler<Scalar>& direction_sampler,
        const SpaceDescriptor<Scalar>& descriptor,
        const ChordSampler<Scalar>& sampler,
        const typename Base::LoggerType& logger)
        : Base(logger)
        , direction_sampler(direction_sampler)
        , space_descriptor(descriptor)
        , chord_sampler(sampler)
        , direction_sampler_Fp(
              direction_sampler.get_optimally_reparametrized_descriptor())
        , space_descriptor_Fi(descriptor.get_optimally_reparametrized_descriptor())
        , chord_sampler_Fs(sampler.get_optimally_reparametrized_sampler())
        , transforms_(direction_sampler_Fp, space_descriptor_Fi, chord_sampler_Fs)
    {}

    const SpaceDescriptor<Scalar>& get_space_descriptor() const
    {
        return space_descriptor_Fi;
    }

    const ChordSampler<Scalar>& get_chord_sampler() const { return chord_sampler_Fs; }

  protected:
    void initialize(const InternalState& state) override
    {
        space_descriptor_Fi.initialize(state);
    }

    /**
     * @brief Execute one step of the simulation.
     *
     * @param state Current state of the chain.
     * @return The new state of the chain.
     */
    void simulate_step(InternalState& state) override
    {
        // 1) Sample new directions according to the direction sampler.
        direction_sampler_Fp.get_directions(
            directions_Fp_, static_cast<Index>(state.cols()));

        // 2) Find the intersections between the current rays and the space
        //    descriptor in the Fi frame.
        rays_Fi_.origins = state;
        transforms_.transform_directions_from_Fp_to_Fi(
            rays_Fi_.directions, directions_Fp_);
        space_descriptor_Fi.intersect(intersections_, rays_Fi_);

        // 3) Sample new points along the resulting chords in the Fs frame. Then
        //    compute the new states in the internal frame (i.e. Fi).
        if (transforms_.is_Fs_equal_Fi()) {
            chord_sampler_Fs.sample1d(t_, rays_Fi_, intersections_, sampling_helper);
        }
        else {
            transforms_.transform_rays_from_Fi_to_Fs(
                rays_Fs_, rays_Fi_, directions_Fp_);
            chord_sampler_Fs.sample1d(t_, rays_Fs_, intersections_, sampling_helper);
        }
        space_descriptor_Fi.update_position(t_);

        rays_Fi_.at(state, t_);
    }

    State convert_from_internal_state(const InternalState& internal_state) override
    {
        return transforms_.transform_from_Fi(internal_state);
    }

    InternalState convert_to_internal_state(const State& state) override
    {
        return transforms_.transform_to_Fi(state);
    }

  private:
    // Helper object used to generate random numbers.
    SamplingHelper sampling_helper;

    // Sampler for ray directions.
    DirectionSampler<Scalar> direction_sampler;
    ReparametrizedObject<DirectionSampler<Scalar>> direction_sampler_Fp;

    // Descriptor of the sampling space.
    SpaceDescriptor<Scalar> space_descriptor;
    ReparametrizedObject<SpaceDescriptor<Scalar>> space_descriptor_Fi;

    // Object used for sampling on the 1-d chord of each hit-and-run step.
    ChordSampler<Scalar> chord_sampler;
    ReparametrizedObject<ChordSampler<Scalar>> chord_sampler_Fs;

    HitAndRunTransforms<Scalar> transforms_;

    // Persistent temporary variables, to avoid reallocation of the matrices at each
    // call.
    typename DirectionSamplerType::DirectionsType directions_Fp_;
    typename DirectionSamplerType::RaysPacketType rays_Fi_;
    IntersectionsPacket<Scalar> intersections_;
    Vector<Scalar> t_;
    RaysPacket<Scalar> rays_Fs_;
};

} // namespace samply

#endif
