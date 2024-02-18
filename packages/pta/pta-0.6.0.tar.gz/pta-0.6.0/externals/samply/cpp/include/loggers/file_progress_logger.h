// Copyright(C) 2018 Mattia Gollub, mattia.gollub@bsse.ethz.ch
// Computational Systems Biology group, ETH Zurich
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef HYPERFLUX_FILE_PROGRESS_LOGGER_H
#define HYPERFLUX_FILE_PROGRESS_LOGGER_H

#include <fstream>

#define NOMINMAX  // Prevent Windows.h from defining min/max macros.
#include <filesystem/path.h>

#include "progress_logger.h"

namespace samply {

/**
 * @brief MCMC logger reporting the status on the simulation on the console.
 *
 * @tparam ChainState Type of the state of a chain.
 * @tparam DurationFormat Type used for storing and specifying elapsed times.
 *
 * Monitor on Linux with:
 *	watch tail -q -n 1 *.log
 */
template <typename ChainState, typename DurationFormat = std::chrono::milliseconds>
class FileProgressLogger : public ProgressLogger<ChainState, DurationFormat> {
public:
    /**
     * @brief Construct a new ConsoleLogger object.
     *
     * @param worker_id Identifier of the worker using this logger.
     * @param log_period Reporting period in milliseconds.
     */
    FileProgressLogger(std::string log_folder,
                       const size_t worker_id,
                       const DurationFormat log_period_s)
        : ProgressLogger<ChainState, DurationFormat>(worker_id, log_period_s)
    {
        ::filesystem::path log_directory(log_folder);
        ::filesystem::path log_file(std::string("hyperflux.status.") +
                                  std::to_string(worker_id) + std::string(".log"));
        ::filesystem::path log_full_path = log_directory / log_file;

        ::filesystem::create_directory(log_folder);
        file_name_ = log_full_path.str();

        file_.open(file_name_);
        if (!file_.is_open())
            throw std::runtime_error("Unable to create log file");
    }

    FileProgressLogger(const FileProgressLogger<ChainState, DurationFormat>& other)
        : ProgressLogger<ChainState, DurationFormat>(other),
          file_name_(other.file_name_)
    {
        file_.open(file_name_);
        if (!file_.is_open())
            throw std::runtime_error("Unable to create log file");
    }

    ~FileProgressLogger()
    {
        file_.close();
    }

protected:
    void print_progress(const std::string& progress_string) override
    {
        file_ << progress_string;
        file_.flush();
    }

private:
    std::ofstream file_;
    std::string file_name_;
};

}  // namespace samply

#endif