// Copyright(C) 2018 Mattia Gollub, mattia.gollub@bsse.ethz.ch
// Computational Systems Biology group, ETH Zurich
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef SAMPLY_MARKOV_CHAIN_H
#define SAMPLY_MARKOV_CHAIN_H

#include <chrono>
#include <vector>

namespace samply {

/**
 * @brief Represents a Markov Chain and provides methods for its simulation.
 *
 * @tparam Derived Type of the Markov Chain implementation used.
 * @tparam State_ Type representing a state of the chain.
 * @tparam Logger Type of the logger monitoring the state of the simulation.
 * @tparam StatesAllocator Type of the allocator for containers of states.
 */
template <
    typename Derived,
    typename State_,
    typename InternalState_,
    template <typename, typename>
    typename Logger>
class MarkovChain {
  public:
    /**
     * @brief Duration type used for computing elapsed times.
     */
    typedef std::chrono::microseconds DurationFormat;

    /**
     * @brief The type of a state of the chain.
     */
    typedef State_ State;
    typedef InternalState_ InternalState;

    class LazyChainStateRef {
      public:
        LazyChainStateRef(Derived& markov_chain, const InternalState& internal_state)
            : markov_chain_(markov_chain)
            , internal_state_(internal_state)
            , has_state_(false)
        {}

        const State& get()
        {
            if (!has_state_) {
                state_ = markov_chain_.convert_from_internal_state(internal_state_);
                has_state_ = true;
            }
            return state_;
        }

        const InternalState& get_internal_state() const { return internal_state_; }

      private:
        Derived& markov_chain_;
        const InternalState& internal_state_;
        State state_;
        bool has_state_;
    };

    /**
     * @brief The type of the logger used for monitoring the simulation.
     */
    typedef Logger<LazyChainStateRef, DurationFormat> LoggerType;

    /**
     * @brief Construct a new MarkovChain object.
     *
     * @param initial_state Initial state of the chain.
     * @param logger The logger used to monitor the state of the simulation.
     */
    MarkovChain(const LoggerType& logger);

    /**
     * @brief Simulate the chain for a given number of steps.
     * The simulation starts from the last state stored in the chain.
     *
     * @tparam DurationFormat Duration type used for specifying the maximum
     * simulation time.
     * @param num_steps Number of steps to simulate.
     * @param steps_thinning Period at which the chain state is stored. This is
     * generally useful if the length on the entire chain doesn't fit in the
     * computer memory.
     * @param max_time Maximum simulation time.
     * @return Number of stored states at the end of the simulation.
     */
    template <typename InputDuration = DurationFormat>
    size_t simulate(
        const size_t num_steps, const InputDuration max_time = DurationFormat::max());

    /**
     * @brief Set the state of the chain. If the chain already contains states,
     * the new state will be appended after the existing ones.
     *
     * @param initial_state New initial state of the chain.
     * @return size_t Number of states stored in the chain after the new one
     * has been added.
     */
    void set_state(const State& state);

    State get_state();

    LoggerType& get_logger();

  protected:
    virtual void initialize(const State& state) = 0;
    /**
     * @brief Execute one step of the simulation.
     *
     * @param state Current state of the chain.
     * @return The new state of the chain.
     */
    virtual void simulate_step(State& state) = 0;
    virtual State convert_from_internal_state(const InternalState& internal_state) = 0;
    virtual InternalState convert_to_internal_state(const State& state) = 0;

  private:
    // Vector containing all the stored states of the chain.
    InternalState internal_state_;

    // Tuple containing the logger monitoring the state of the simulations.
    LoggerType logger_;
};

//==============================================================================
//	MarkovChain public methods implementation.
//==============================================================================

#define _SAMPLY_MARKOVCHAIN_TEMPLATE_DECL                                              \
    typename Derived, typename State, typename InternalState,                          \
        template <typename, typename>                                                  \
        typename Logger
#define _SAMPLY_MARKOVCHAIN_TEMPLATE_SPEC Derived, State, InternalState, Logger

template <_SAMPLY_MARKOVCHAIN_TEMPLATE_DECL>
inline MarkovChain<_SAMPLY_MARKOVCHAIN_TEMPLATE_SPEC>::MarkovChain(
    const LoggerType& logger)
    : logger_(logger)
{}

template <_SAMPLY_MARKOVCHAIN_TEMPLATE_DECL>
template <typename InputDuration>
inline size_t MarkovChain<_SAMPLY_MARKOVCHAIN_TEMPLATE_SPEC>::simulate(
    const size_t num_steps, const InputDuration max_time)
{
    using std::chrono::duration_cast;
    using chain_clock = std::chrono::steady_clock;

    // Validate inputs.
    assert(num_steps > 0);
    assert(max_time <= duration_cast<InputDuration>(DurationFormat::max()));

    // Start timer and logger.
    const auto start_time = chain_clock::now();
    logger_.start();

    // Run the chain for the desired number of steps.
    bool time_limit_reached = false;
    size_t step_idx = 0u;
    static_cast<Derived&>(*this).initialize(internal_state_);

    for (; step_idx < num_steps && !time_limit_reached; ++step_idx) {
        // Simulate the next step of the chain.
        static_cast<Derived&>(*this).simulate_step(internal_state_);

        // Notify the logger that the step has been completed.
        const auto elapsed_time =
            duration_cast<DurationFormat>(chain_clock::now() - start_time);
        LazyChainStateRef state_ref(static_cast<Derived&>(*this), internal_state_);
        logger_.log(state_ref, elapsed_time, step_idx + 1);

        time_limit_reached = elapsed_time >= max_time;
    }

    // Terminate the logger and return the number of recorded step.
    logger_.stop(time_limit_reached);
    return step_idx + 1;
}

template <_SAMPLY_MARKOVCHAIN_TEMPLATE_DECL>
inline void
MarkovChain<_SAMPLY_MARKOVCHAIN_TEMPLATE_SPEC>::set_state(const State& state)
{
    internal_state_ = static_cast<Derived&>(*this).convert_to_internal_state(state);
}

template <_SAMPLY_MARKOVCHAIN_TEMPLATE_DECL>
inline State MarkovChain<_SAMPLY_MARKOVCHAIN_TEMPLATE_SPEC>::get_state()
{
    return static_cast<Derived&>(*this).convert_from_internal_state(internal_state_);
}

template <_SAMPLY_MARKOVCHAIN_TEMPLATE_DECL>
inline typename MarkovChain<_SAMPLY_MARKOVCHAIN_TEMPLATE_SPEC>::LoggerType&
MarkovChain<_SAMPLY_MARKOVCHAIN_TEMPLATE_SPEC>::get_logger()
{
    return logger_;
}

} // namespace samply

#endif
