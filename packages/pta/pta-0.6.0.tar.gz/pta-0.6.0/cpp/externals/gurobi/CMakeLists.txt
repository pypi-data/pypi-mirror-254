# Copyright (C) 2018 Mattia Gollub, mattia.gollub@bsse.ethz.ch
# Computational Systems Biology group, ETH Zurich
#
# This software is freely available under the GNU General Public License v3.
# See the LICENSE file or http://www.gnu.org/licenses/ for further information.

cmake_minimum_required (VERSION 3.12)

# Get the root directory of the Gurobi installation.
file(TO_CMAKE_PATH "$ENV{GUROBI_HOME}" GUROBI_HOME)

# Find path to Gurobi include files.
find_path(GUROBI_INCLUDE_DIR
    NAMES gurobi_c++.h
	PATHS "${GUROBI_HOME}/include")
set(GUROBI_INCLUDE_DIRS 
	"${GUROBI_INCLUDE_DIR}"
	CACHE STRING "Gurobi headers path")

# Find Gurobi C library.
file(GLOB GUROBI_LIBRARY_CANDIDATES
	RELATIVE "${GUROBI_HOME}/lib/"
	"${GUROBI_HOME}/lib/gurobi*.lib"
	"${GUROBI_HOME}/lib/libgurobi*.so"
	"${GUROBI_HOME}/lib/libgurobi*.dylib")
find_library(GUROBI_LIBRARY
	NAMES ${GUROBI_LIBRARY_CANDIDATES}
    PATHS "${GUROBI_HOME}/lib")

# Compile Gurobi C++ library.
if (CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC")
endif()
file(GLOB GUROBI_SRC
	"${GUROBI_HOME}/src/cpp/*.h"
	"${GUROBI_HOME}/src/cpp/*.cpp")
add_library(gurobi STATIC ${GUROBI_SRC})
target_include_directories(gurobi PUBLIC "${GUROBI_INCLUDE_DIRS}")
target_link_libraries(gurobi "${GUROBI_LIBRARY}")