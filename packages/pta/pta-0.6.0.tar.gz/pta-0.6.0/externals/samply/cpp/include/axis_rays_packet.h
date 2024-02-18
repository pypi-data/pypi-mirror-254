// Copyright (c) 2019 ETH Zurich, Mattia Gollub (mattia.gollub@bsse.ethz.ch)
// Computational Systems Biology group, D-BSSE
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef SAMPLY_AXIS_RAYS_PACKET_H
#define SAMPLY_AXIS_RAYS_PACKET_H

#include "commons.h"

namespace samply {

template <typename Scalar> struct AxisRaysPacket {
    Matrix<Scalar> origins;
    IndexVector directions;

    void at(Matrix<Scalar>& output_points, const Vector<Scalar>& t) const
    {
        output_points = origins;
        for (Eigen::Index i = 0u; i < t.size(); ++i)
            output_points(directions(i), i) += t(i);
    }

    Matrix<Scalar> at(const Vector<Scalar>& t) const
    {
        Matrix<Scalar> result;
        this->at(result, t);
        return result;
    }

    void
    at(Matrix<Scalar>& output_points,
       const IndexVector& ray_indices,
       const Vector<Scalar>& t) const
    {
        output_points = origins(Eigen::all, ray_indices);
        for (const auto& i : ray_indices)
            output_points(directions(i), i) += t(i);
    }

    Matrix<Scalar> at(const IndexVector& ray_indices, const Vector<Scalar>& t) const
    {
        Matrix<Scalar> result;
        this->at(result, ray_indices, t);
        return result;
    }

    void at(Vector<Scalar>& output_points, Index& ray_index, const Scalar t) const
    {
        output_points = origins(Eigen::all, ray_index);
        output_points(directions(ray_index), ray_index) += t(ray_index);
    }

    Vector<Scalar> at(Index& ray_index, const Scalar t) const
    {
        Vector<Scalar> result = origins(Eigen::all, ray_index);
        this->at(result, ray_index, t);
        return result;
    }
};

} // namespace samply

#endif