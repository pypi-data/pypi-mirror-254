// Copyright(C) 2018-2022 Mattia Gollub, mattia.gollub@bsse.ethz.ch
// Computational Systems Biology group, ETH Zurich
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef PTA_PYTHON_PROGRESS_LOGGER_H
#define PTA_PYTHON_PROGRESS_LOGGER_H

#include <loggers/progress_logger.h>
#include <pybind11/pybind11.h>

#include <chrono>
#include <iomanip>
#include <iostream>

namespace py = pybind11;

namespace samply {

/**
 * @brief MCMC logger reporting the status on the simulation on the console.
 *
 * @tparam ChainState Type of the state of a chain.
 * @tparam DurationFormat Type used for storing and specifying elapsed times.
 */
template <typename ChainState, typename DurationFormat = std::chrono::milliseconds>
class PythonProgressLogger : public ProgressLogger<ChainState, DurationFormat> {
  public:
    /**
     * @brief Construct a new ConsoleProgressLogger object.
     *
     * @param worker_id Identifier of the worker using this logger.
     * @param log_period Reporting period in milliseconds.
     */
    PythonProgressLogger(const size_t worker_id, const DurationFormat log_period_s)
        : ProgressLogger<ChainState, DurationFormat>(worker_id, log_period_s)
    {}

    PythonProgressLogger(const PythonProgressLogger<ChainState, DurationFormat>& other)
        : ProgressLogger<ChainState, DurationFormat>(other)
    {}

  protected:
    void print_progress(const std::string& progress_string) override
    {
        py::gil_scoped_acquire gil_acquire;
        std::cout << progress_string << std::flush;
    }
};

} // namespace samply

#endif
