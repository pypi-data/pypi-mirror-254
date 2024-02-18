// Copyright(C) 2018 Mattia Gollub, mattia.gollub@bsse.ethz.ch
// Computational Systems Biology group, ETH Zurich
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef HYPERFLUX_PROGRESS_LOGGER_H
#define HYPERFLUX_PROGRESS_LOGGER_H

#include <chrono>
#include <iomanip>
#include <iostream>

namespace samply {

/**
 * @brief MCMC logger reporting the status on the simulation on the console.
 *
 * @tparam ChainState Type of the state of a chain.
 * @tparam DurationFormat Type used for storing and specifying elapsed times.
 */
template <typename ChainState, typename DurationFormat = std::chrono::milliseconds>
class ProgressLogger {
public:
    /**
     * @brief Construct a new ProgressLogger object.
     *
     * @param worker_id Identifier of the worker using this logger.
     * @param log_period Reporting period in milliseconds.
     */
    ProgressLogger(const size_t worker_id, const DurationFormat log_period_s)
        : worker_id_(worker_id),
          log_period_(std::chrono::duration_cast<DurationFormat>(log_period_s)),
          last_log_time_(0),
          last_log_step_idx_(0u)
    {
    }

    ProgressLogger(const ProgressLogger<ChainState, DurationFormat>& other)
        : last_log_time_(other.last_log_time_),
          last_log_step_idx_(other.last_log_step_idx_),
          log_period_(other.log_period_),
          worker_id_(other.worker_id_),
          output_stream_()
    {
    }

    /**
     * @brief Log the current status of the simulation on the console.
     *
     * @param chain_state The current state of the chain being simulated by
     * the owning worker.
     * @param total_time The total elapsed time since the start of the
     * simulation.
     * @param total_steps The total number of steps completed since the
     * start of the simulation.
     */
    void log(const ChainState& chain_state,
             const DurationFormat total_time,
             const size_t step_idx)
    {
        const auto interval_time = total_time - last_log_time_;
        if (interval_time >= log_period_) {
            // Convert time to decimal representation and compute the steps
            // rate.
            typedef std::chrono::duration<double> DoubleSeconds;
            const double double_interval_time =
                std::chrono::duration_cast<DoubleSeconds>(interval_time).count();
            const double elapsed_time =
                std::chrono::duration_cast<DoubleSeconds>(total_time).count();
            const size_t interval_steps = step_idx - last_log_step_idx_;
            const double steps_rate =
                static_cast<double>(interval_steps) / double_interval_time;

            output_stream_ << std::fixed << std::setw(10) << std::setprecision(0)
                           << worker_id_ << " |" << std::setw(10)
                           << std::setprecision(2) << elapsed_time << " |"
                           << std::setw(10) << std::setprecision(0) << step_idx + 1
                           << " |" << std::setw(10) << std::setprecision(2)
                           << steps_rate << " |" << std::endl;
            print_progress(output_stream_.str());
            output_stream_.str("");

            last_log_time_ = total_time;
            last_log_step_idx_ = step_idx;
        }
    }

    /**
     * @brief Notifies the logger that a simulation started.
     */
    void start()
    {
        output_stream_ << std::endl << "Starting simulation ..." << std::endl;
        output_stream_ << "------------------------------------------------"
                       << std::endl;
        output_stream_ << "    worker |  time (s) |     steps |   steps/s  "
                       << std::endl;
        output_stream_ << "------------------------------------------------"
                       << std::endl;
        print_progress(output_stream_.str());
        output_stream_.str("");
    }

    /**
     * @brief Notifies the logger that the simulation terminated.
     *
     * @param time_limit_reached If true, signals that time limit has been
     * reached during the simulation and the chain might not have converged.
     */
    void stop(const bool time_limit_reached = false)
    {
        if (time_limit_reached)
            output_stream_ << "Time limit reached. The chain might not have converged."
                           << std::endl;
        else
            output_stream_ << "Done." << std::endl;
        print_progress(output_stream_.str());
        output_stream_.str("");
    }

protected:
    virtual void print_progress(const std::string& progress_string) = 0;

private:
    // Elapsed simulation time when the last line was logged.
    DurationFormat last_log_time_;

    // Number of steps completed when the last line was logged.
    size_t last_log_step_idx_;

    // Minimum time between two log actions.
    DurationFormat log_period_;

    // Identifier of the worker owning this logger.
    size_t worker_id_;

    std::ostringstream output_stream_;
};

}  // namespace samply

#endif