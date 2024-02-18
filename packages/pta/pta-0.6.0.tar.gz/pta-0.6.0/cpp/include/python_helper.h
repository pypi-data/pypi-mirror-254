// Copyright (c) 2021 ETH Zurich, Mattia Gollub (mattia.gollub@bsse.ethz.ch)
// Computational Systems Biology group, D-BSSE
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef PTA_PYTHON_HELPER_H
#define PTA_PYTHON_HELPER_H

#include <pybind11/eigen.h>
#include <pybind11/pybind11.h>
#include <settings.h>

#include <Eigen/Dense>
#include <Eigen/StdVector>
#include <tuple>
#include <unordered_map>
#include <vector>

#include "commons.h"
#include "eigen-hash.h"
#include "settings/free_energy_sampling_settings.h"
#include "settings/uniform_flux_sampling_settings.h"

namespace py = pybind11;

namespace pta {
namespace python_helper {

template <typename Matrix, typename Allocator>
py::array_t<typename Matrix::Scalar>
vector_of_eigen_matrices_to_numpy_3d_array(const std::vector<Matrix, Allocator>& data)
{
    assert(!data.empty());

    // Access matrices using numpy storage order.
    using PyMatrixMap =
        Eigen::Map<Eigen::Matrix<typename Matrix::Scalar, Eigen::Dynamic,
                                 Eigen::Dynamic, Eigen::RowMajor>>;

    // Ask numpy to allocate 3D array.
    py::array_t<typename Matrix::Scalar> result(
        std::vector<size_t>{data.size(), static_cast<size_t>(data[0].rows()),
                            static_cast<size_t>(data[0].cols())});

    // Copy the data.
    for (size_t matrix_idx = 0u; matrix_idx < data.size(); ++matrix_idx) {
        PyMatrixMap destination_matrix(result.mutable_data(matrix_idx), data[0].rows(),
                                       data[0].cols());
        destination_matrix = data[matrix_idx];
    }

    return result;
}

template <typename Matrix>
py::array_t<typename Matrix::Scalar> eigen_vector_to_numpy_vector(const Matrix& data)
{
    // assert(!data.empty());

    // Access matrices using numpy storage order.
    using PyMatrixMap =
        Eigen::Map<Eigen::Matrix<typename Matrix::Scalar, Eigen::Dynamic,
                                 Eigen::Dynamic, Eigen::RowMajor>>;

    // Ask numpy to allocate the array.
    py::array_t<typename Matrix::Scalar> result(
        std::vector<size_t>{static_cast<size_t>(data.size()), 1u});

    // Copy the data.
    PyMatrixMap destination_matrix(result.mutable_data(), data.rows(), data.cols());
    destination_matrix = data;

    return result;
}

template <typename Scalar>
py::array_t<Scalar>
vector_of_vectors_to_numpy_matrix(const std::vector<std::vector<Scalar>>& data)
{
    assert(!data.empty());

    // Access matrices using numpy storage order.
    using PyMatrixMap = Eigen::Map<
        Eigen::Matrix<Scalar, Eigen::Dynamic, Eigen::Dynamic, Eigen::RowMajor>>;
    using StdVectorMap =
        Eigen::Map<const Eigen::Matrix<Scalar, Eigen::Dynamic, Eigen::Dynamic>>;

    // Ask numpy to allocate the array.
    py::array_t<Scalar> result(std::vector<size_t>{data.size(), data[0].size()});

    // Copy the data.
    for (size_t vector_idx = 0u; vector_idx < data.size(); ++vector_idx) {
        PyMatrixMap destination_matrix(result.mutable_data(vector_idx), 1u,
                                       data[0].size());
        StdVectorMap source_vector(data[vector_idx].data(), 1u, data[0].size());
        destination_matrix = source_vector;
    }

    return result;
}

template <typename Hasher>
std::tuple<py::array_t<uint8_t>, py::array_t<uint32_t>> direction_counts_to_python(
    const std::unordered_map<std::vector<uint8_t>, uint32_t, Hasher>& directions_counts)
{
    samply::Vector<uint32_t> counts(directions_counts.size());
    std::vector<std::vector<uint8_t>> directions(directions_counts.size());

    size_t direction_idx = 0u;
    for (const auto& it : directions_counts) {
        directions[direction_idx] = it.first;
        counts[direction_idx] = it.second;
        direction_idx++;
    }

    return {vector_of_vectors_to_numpy_matrix(directions),
            eigen_vector_to_numpy_vector(counts)};
}

} // namespace python_helper
} // namespace pta

#endif
