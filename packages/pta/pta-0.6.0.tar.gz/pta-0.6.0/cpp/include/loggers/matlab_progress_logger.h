// Copyright (c) 2021 ETH Zurich, Mattia Gollub (mattia.gollub@bsse.ethz.ch)
// Computational Systems Biology group, D-BSSE
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef PTA_MATLAB_PROGRESS_LOGGER_H
#define PTA_MATLAB_PROGRESS_LOGGER_H

#include <chrono>
#include <iomanip>
#include <iostream>
#include <mex.hpp>

#include "progress_logger.h"

namespace pta {

/**
 * @brief MCMC logger reporting the status on the simulation on the console.
 *
 * @tparam ChainState Type of the state of a chain.
 * @tparam DurationFormat Type used for storing and specifying elapsed times.
 */
template <typename ChainState, typename DurationFormat = std::chrono::milliseconds>
class MatlabProgressLogger : public ProgressLogger<ChainState, DurationFormat> {
  public:
    /**
     * @brief Construct a new ConsoleLogger object.
     *
     * @param worker_id Identifier of the worker using this logger.
     * @param log_period Reporting period in milliseconds.
     */
    MatlabProgressLogger(std::shared_ptr<matlab::engine::MATLABEngine> matlab_engine,
                         const size_t worker_id,
                         const std::chrono::milliseconds log_period_s)
        : ProgressLogger<ChainState, DurationFormat>(worker_id, log_period_s),
          matlab_engine_(matlab_engine)
    {}

    MatlabProgressLogger(const MatlabProgressLogger<ChainState, DurationFormat>& other)
        : ProgressLogger<ChainState, DurationFormat>(other),
          matlab_engine_(other.matlab_engine_), factory_()
    {}

  protected:
    void print_progress(const std::string& progress_string) override
    {
        // Pass stream content to MATLAB fprintf function
        // https://ch.mathworks.com/help/matlab/matlab_external/displaying-output-in-matlab-command-window.html
        matlab_engine_->feval(
            u"fprintf", 0,
            std::vector<matlab::data::Array>({factory_.createScalar(progress_string)}));
    }

  private:
    std::shared_ptr<matlab::engine::MATLABEngine> matlab_engine_;

    matlab::data::ArrayFactory factory_;
};

} // namespace pta

#endif