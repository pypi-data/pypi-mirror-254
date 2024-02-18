// Copyright (c) 2021 ETH Zurich, Mattia Gollub (mattia.gollub@bsse.ethz.ch)
// Computational Systems Biology group, D-BSSE
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef PTA_US_PYTHON_BINDINGS
#define PTA_US_PYTHON_BINDINGS

#include <pybind11/pybind11.h>

namespace py = pybind11;

void add_us_python_bindings(py::module& m);

#endif