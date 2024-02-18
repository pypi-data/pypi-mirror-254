// Copyright (c) 2021 ETH Zurich, Mattia Gollub (mattia.gollub@bsse.ethz.ch)
// Computational Systems Biology group, D-BSSE
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef SAMPLY_RAYS_PACKET_H
#define SAMPLY_RAYS_PACKET_H

#include <type_traits>

#include "commons.h"

namespace samply {

template <typename Scalar> struct RaysPacket;

//======================================================================================
//	Storage types for ray packets.
//======================================================================================

template <typename Scalar> struct RaysPacketStorage {
    RaysPacketStorage() {}

    RaysPacketStorage(const Matrix<Scalar>& origins, const Matrix<Scalar>& directions)
        : origins(origins)
        , directions(directions)
    {}

    Matrix<Scalar> origins;
    Matrix<Scalar> directions;
};

template <typename Scalar, typename ViewFunc1, typename ViewFunc2 = ViewFunc1>
struct RaysPacketViewStorage {
    RaysPacketViewStorage(
        const RaysPacket<Scalar>& ray_packet, const ViewFunc1 view_function)
        : origins(view_function(ray_packet.origins))
        , directions(view_function(ray_packet.directions))
    {}

    RaysPacketViewStorage(
        const RaysPacket<Scalar>& ray_packet,
        const ViewFunc1 view_function_origins,
        const ViewFunc2 view_function_directions)
        : origins(view_function_origins(ray_packet.origins))
        , directions(view_function_directions(ray_packet.directions))
    {}

    typename std::invoke_result<ViewFunc1, Matrix<Scalar>>::type origins;
    typename std::invoke_result<ViewFunc2, Matrix<Scalar>>::type directions;
};

//======================================================================================
//	Base class for ray packets.
//======================================================================================

template <typename Scalar, typename Storage> struct RaysPacketBase : public Storage {
    using Storage::Storage;

    void at(Matrix<Scalar>& output_points, const Vector<Scalar>& t) const
    {
        output_points = this->origins + this->directions * t.asDiagonal();
    }

    Matrix<Scalar> at(const Vector<Scalar>& t) const
    {
        Matrix<Scalar> result;
        this->at(result, t);
        return result;
    }

    void
    at(Matrix<Scalar>& output_points,
       const Eigen::VectorXi& ray_indices,
       const Vector<Scalar>& t) const
    {
        output_points = this->origins(Eigen::all, ray_indices) +
                        this->directions(Eigen::all, ray_indices) * t.asDiagonal();
    }

    Matrix<Scalar> at(const Eigen::VectorXi& ray_indices, const Vector<Scalar>& t) const
    {
        Matrix<Scalar> result;
        this->at(result, ray_indices, t);
        return result;
    }

    void at(Vector<Scalar>& output_points, const int& ray_index, const Scalar t) const
    {
        output_points =
            this->origins.col(ray_index) + this->directions.col(ray_index) * t;
    }

    Vector<Scalar> at(const int& ray_index, const Scalar t) const
    {
        Vector<Scalar> result;
        this->at(result, ray_index, t);
        return result;
    }

    template <typename IndexList>
    RaysPacket<Scalar> operator()(const IndexList& ray_indices) const
    {
        return RaysPacket<Scalar>{
            this->origins(Eigen::all, ray_indices),
            this->directions(Eigen::all, ray_indices)};
    }
};

//======================================================================================
//	Rays packets classes.
//======================================================================================

template <typename Scalar>
struct RaysPacket : public RaysPacketBase<Scalar, RaysPacketStorage<Scalar>> {
    using RaysPacketBase<Scalar, RaysPacketStorage<Scalar>>::RaysPacketBase;
};

template <typename Scalar, typename ViewFunc1, typename ViewFunc2 = ViewFunc1>
struct RaysPacketView : public RaysPacketBase<
                            Scalar,
                            RaysPacketViewStorage<Scalar, ViewFunc1, ViewFunc2>> {
    using RaysPacketBase<Scalar, RaysPacketViewStorage<Scalar, ViewFunc1, ViewFunc2>>::
        RaysPacketBase;
};

} // namespace samply

#endif