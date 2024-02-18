// Copyright (c) 2021 ETH Zurich, Mattia Gollub (mattia.gollub@bsse.ethz.ch)
// Computational Systems Biology group, D-BSSE
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#include <pybind11/chrono.h>
#include <pybind11/eigen.h>
#include <pybind11/iostream.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "common_python_bindings.h"
#include "tfs_python_bindings.h"
#include "us_python_bindings.h"

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

//==============================================================================
//  Define Pybind11 bindings.
//==============================================================================

PYBIND11_MODULE(_pta_python_binaries, m)
{
    m.doc() = R"pbdoc(
        PTA binaries interface.
    )pbdoc";

    add_common_python_bindings(m);
    add_us_python_bindings(m);
    add_tfs_python_bindings(m);

#ifdef VERSION_INFO
    m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
    m.attr("__version__") = "dev";
#endif
}
