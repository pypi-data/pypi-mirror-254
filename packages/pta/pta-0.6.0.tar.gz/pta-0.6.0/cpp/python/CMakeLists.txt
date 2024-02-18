cmake_minimum_required(VERSION 3.4)

add_subdirectory(pybind11)

#===============================================================================
# Set default options and library directories if none was specified.
#===============================================================================

if(NOT SAMPLY_ROOT)
	set(SAMPLY_ROOT "../../externals/samply/")
	get_filename_component(SAMPLY_ROOT "${SAMPLY_ROOT}" ABSOLUTE)
endif()
set(Samply_INCLUDE_DIRS "${SAMPLY_ROOT}/cpp/include/")
set(Filesystem_INCLUDE_DIRS "${SAMPLY_ROOT}/cpp/externals/filesystem/")
set(Pcg_INCLUDE_DIRS "${SAMPLY_ROOT}/cpp/externals/pcg-cpp/include/")
set(DynamicBitset_INCLUDE_DIRS "../externals/dynamic_bitset/")

if(NOT EIGEN_ROOT)
	set(EIGEN_ROOT "${SAMPLY_ROOT}/cpp/externals/eigen/")
	get_filename_component(EIGEN_ROOT "${EIGEN_ROOT}" ABSOLUTE)
endif()
set(Eigen_INCLUDE_DIRS "${EIGEN_ROOT}/")

if(NOT EXISTS "${Eigen_INCLUDE_DIRS}/Eigen/Dense")
	message(FATAL_ERROR "Eigen is not present in the specified directory: \
		${EIGEN_ROOT}")
endif()

if(NOT DEFINED PTA_VERSION)
	set(PTA_VERSION "undefined")
endif()

#===============================================================================
# Optimize building flags for the architetcture of the CPU in use.
#===============================================================================

include(OptimizeArchitectureFlags)
optimize_architecture_flags()

#===============================================================================
# Helper functions for adding library dependencies.
#===============================================================================

function(add_common_dependencies target_name)
    target_include_directories(${target_name} PUBLIC "../include" )
	target_include_directories(${target_name} PUBLIC ${Eigen_INCLUDE_DIRS})
	target_include_directories(${target_name} PUBLIC ${Samply_INCLUDE_DIRS})
	target_include_directories(${target_name} PUBLIC ${Filesystem_INCLUDE_DIRS})
	target_include_directories(${target_name} PUBLIC ${Pcg_INCLUDE_DIRS})
	target_include_directories(${target_name} PUBLIC ${DynamicBitset_INCLUDE_DIRS})
	target_include_directories(${target_name} PUBLIC ${GUROBI_INCLUDE_DIRS})
endfunction(add_common_dependencies)

function(add_gurobi_dependency target_name)
    add_dependencies(${target_name} gurobi)
	target_include_directories(${target_name} PUBLIC "${GUROBI_INCLUDE_DIRS}")
	target_link_libraries(${target_name} PUBLIC gurobi)
endfunction(add_gurobi_dependency)

#===============================================================================
# Create build targets.
#===============================================================================

pybind11_add_module(
	_pta_python_binaries
	common_python_bindings.cpp
	us_python_bindings.cpp
	tfs_python_bindings.cpp
	python_bindings.cpp)
add_common_dependencies(_pta_python_binaries)
add_gurobi_dependency(_pta_python_binaries)

target_compile_definitions(
	_pta_python_binaries PRIVATE
	VERSION_INFO=${PTA_VERSION})

install(TARGETS _pta_python_binaries DESTINATION ${PTA_ROOT})