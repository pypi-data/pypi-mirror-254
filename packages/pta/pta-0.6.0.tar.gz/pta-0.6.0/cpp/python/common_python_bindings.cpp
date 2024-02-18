// Copyright (c) 2021 ETH Zurich, Mattia Gollub (mattia.gollub@bsse.ethz.ch)
// Computational Systems Biology group, D-BSSE
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#include <pybind11/chrono.h>
#include <pybind11/pybind11.h>
#include <settings.h>

using namespace samply;

namespace py = pybind11;

void add_common_python_bindings(py::module& m)
{
    py::class_<Settings>(m, "SamplerSettings")
        .def(py::init<>())
        .def_readwrite("worker_id", &Settings::worker_id)
        .def_readwrite("num_steps", &Settings::num_steps)
        .def_readwrite("num_chains", &Settings::num_chains)
        .def_readwrite("steps_thinning", &Settings::steps_thinning)
        .def_readwrite("num_skipped_steps", &Settings::num_skipped_steps)
        .def_readwrite("log_interval", &Settings::console_logging_interval_ms)
        .def_readwrite("log_directory", &Settings::log_directory)
        .def_readwrite("max_threads", &Settings::max_threads);;
}