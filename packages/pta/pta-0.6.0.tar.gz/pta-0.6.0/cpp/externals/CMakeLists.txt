# Copyright (C) 2018 Mattia Gollub, mattia.gollub@bsse.ethz.ch
# Computational Systems Biology group, ETH Zurich
#
# This software is freely available under the GNU General Public License v3.
# See the LICENSE file or http://www.gnu.org/licenses/ for further information.

cmake_minimum_required (VERSION 3.12)

if(THERMODYNAMIC_SAMPLERS)
	add_subdirectory(gurobi)
endif()