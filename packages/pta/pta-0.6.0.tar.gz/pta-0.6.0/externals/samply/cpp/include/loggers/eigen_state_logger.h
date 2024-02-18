// Copyright(C) 2019 Mattia Gollub, mattia.gollub@bsse.ethz.ch
// Computational Systems Biology group, ETH Zurich
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef SAMPLY_EIGEN_STATE_LOGGER_H
#define SAMPLY_EIGEN_STATE_LOGGER_H

#include <Eigen/StdVector>
#include <mutex>
#include <numeric>
#include <vector>

#include "state_logger.h"

namespace samply {

template <typename Scalar> class EigenStateStorage {
  public:
    typedef Eigen::Matrix<Scalar, Eigen::Dynamic, Eigen::Dynamic> StoredState;
    typedef std::vector<StoredState, Eigen::aligned_allocator<StoredState>>
        StoredStates;

    EigenStateStorage(const std::vector<size_t>& chains_per_thread,
                      const Eigen::Index num_rows,
                      const Eigen::Index num_columns,
                      const size_t num_preallocated_states = 1u)
        : num_rows_(num_rows)
        , num_columns_(num_columns)
        , states_(0)
        , worker_start_idxs_(1, 0)
    {
        states_.reserve(num_preallocated_states);
        std::partial_sum(chains_per_thread.begin(), chains_per_thread.end(),
                         std::back_inserter(worker_start_idxs_));
        worker_start_idxs_.pop_back();
    }

    const StoredStates& get_states() const { return states_; }

    void
    log_state(const StoredState& state, const size_t worker_idx, const size_t state_idx)
    {
        // Prevent access from other threads.
        std::scoped_lock states_lock(states_mutex_);

        // Extend the list if necessary.
        if (state_idx >= states_.size())
            states_.resize(state_idx + 1, StoredState(num_rows_, num_columns_));

        // Insert the state.
        states_[state_idx].block(0u, worker_start_idxs_[worker_idx], num_rows_,
                                 state.cols()) = state;
    }

  private:
    std::mutex states_mutex_;
    StoredStates states_;
    std::vector<size_t> worker_start_idxs_;
    const Eigen::Index num_rows_;
    const Eigen::Index num_columns_;
};

template <typename ChainState, typename DurationFormat = std::chrono::milliseconds>
class EigenStateLogger : public StateLogger<ChainState, DurationFormat> {
  public:
    typedef Eigen::MatrixXd StoredState;
    typedef std::vector<StoredState, Eigen::aligned_allocator<StoredState>>
        StoredStates;

    EigenStateLogger(EigenStateStorage<double>& storage,
                     const size_t worker_id,
                     const size_t steps_log_interval,
                     const size_t num_skipped_steps = 0u)
        : state_idx_(0u)
        , storage_(storage)
        , StateLogger<ChainState, DurationFormat>(
              worker_id, steps_log_interval, num_skipped_steps)
    {}

    EigenStateLogger(const EigenStateLogger<ChainState>& other)
        : StateLogger<ChainState, DurationFormat>(other)
        , state_idx_(other.state_idx_)
        , storage_(other.storage_)
    {}

    void start() override {}

    void stop(const bool time_limit_reached = false) override {}

  protected:
    void log_state(ChainState& chain_state, const size_t step_idx) override
    {
        storage_.log_state(chain_state.get(), this->worker_id_, state_idx_);
        state_idx_++;
    }

  private:
    EigenStateStorage<double>& storage_;
    size_t state_idx_;
};

} // namespace samply

#endif
