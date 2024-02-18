// Copyright(C) 2019 Mattia Gollub, mattia.gollub@bsse.ethz.ch
// Computational Systems Biology group, ETH Zurich
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef SAMPLY_STATE_LOGGER_H
#define SAMPLY_STATE_LOGGER_H

#include <chrono>
#include <iostream>

namespace samply {

template <typename ChainState, typename DurationFormat = std::chrono::milliseconds>
class StateLogger {
  public:
    StateLogger(
        const size_t worker_id,
        const size_t steps_log_interval,
        const size_t num_skipped_steps = 0)
        : worker_id_(worker_id)
        , steps_log_interval_(steps_log_interval)
        , next_logging_step_(num_skipped_steps)
    {}

    StateLogger(const StateLogger<ChainState>& other)
        : worker_id_(other.worker_id_)
        , steps_log_interval_(other.steps_log_interval_)
        , next_logging_step_(other.next_logging_step_)
    {}

    void
    log(ChainState& chain_state, const DurationFormat total_time, const size_t step_idx)
    {
        if (step_idx + 1 == next_logging_step_) {
            next_logging_step_ += steps_log_interval_;
            log_state(chain_state, step_idx);
        }
    }

    virtual void start() {}

    virtual void stop(const bool time_limit_reached = false) {}

  protected:
    virtual void log_state(ChainState& chain_state, const size_t step_idx) = 0;

    // Identifier of the worker owning this logger.
    const size_t worker_id_;

  private:
    const size_t steps_log_interval_;

    size_t next_logging_step_;
};

} // namespace samply

#endif