# Copyright (C) 2018 Mattia Gollub, mattia.gollub@bsse.ethz.ch
# Computational Systems Biology group, ETH Zurich
#
# This software is freely available under the GNU General Public License v3.
# See the LICENSE file or http://www.gnu.org/licenses/ for further information.

cmake_minimum_required (VERSION 3.13)

project(pta)

option(THERMODYNAMIC_SAMPLERS "Build thermodynamic samplers" ON)

SET(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_EXTENSIONS OFF)

# Helper function for debugging CMAKE variables.
# ================================================
function(print_cmake_variables)
    message(STATUS "==========================================================")
	message(STATUS " CMAKE VARIABLES:")
    get_cmake_property(cmake_variable_names VARIABLES)
    foreach (variable_name ${cmake_variable_names})
        message(STATUS "${variable_name} = ${${variable_name}}")
    endforeach()
    message(STATUS "==========================================================")
endfunction()

list(APPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_LIST_DIR}/cmake)
set(HYPERFLUX_ROOT "${CMAKE_HOME_DIRECTORY}/.."
	CACHE STRING "PTA root directory") # Deprecated
set(PTA_ROOT "${CMAKE_HOME_DIRECTORY}/.."
	CACHE STRING "PTA root directory")

add_subdirectory(externals)
add_subdirectory(python)