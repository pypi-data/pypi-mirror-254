// Copyright (c) 2021 ETH Zurich, Mattia Gollub (mattia.gollub@bsse.ethz.ch)
// Computational Systems Biology group, D-BSSE
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef SAMPLY_COMMONS_H
#define SAMPLY_COMMONS_H

#include <Eigen/Core>
#include <Eigen/SparseCore>
#include <cstdint>
#include <inttypes.h>

namespace samply {

using Index = std::int32_t;

template <typename Scalar>
using Matrix = Eigen::Matrix<Scalar, Eigen::Dynamic, Eigen::Dynamic>;

template <typename Scalar> using Vector = Eigen::Matrix<Scalar, Eigen::Dynamic, 1>;

using IndexVector = Vector<Index>;

template <typename Scalar> using RowVector = Eigen::Matrix<Scalar, 1, Eigen::Dynamic>;

template <typename Scalar> using SparseMatrix = Eigen::SparseMatrix<Scalar>;

template <typename Scalar> using SparseVector = Eigen::SparseVector<Scalar>;

} // namespace samply

#endif