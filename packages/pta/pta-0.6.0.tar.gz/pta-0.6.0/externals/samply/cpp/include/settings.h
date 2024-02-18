// Copyright(C) 2018 Mattia Gollub, mattia.gollub@bsse.ethz.ch
// Computational Systems Biology group, ETH Zurich
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef HYPERFLUX_SETTINGS_H
#define HYPERFLUX_SETTINGS_H

#include <stdint.h>

#include <chrono>
#include <string>

namespace samply {

struct Settings {
    size_t worker_id;

    // Chain simulation settings.
    size_t num_steps;
    size_t num_chains;
    size_t steps_thinning;
    size_t num_skipped_steps;

    // Logging settings.
    std::chrono::microseconds console_logging_interval_ms;
    std::string log_directory;

    // Threading settings.
    size_t max_threads = std::numeric_limits<size_t>::max();
};

}  // namespace samply

#endif