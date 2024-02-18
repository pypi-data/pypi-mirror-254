// Copyright(C) 2018 Mattia Gollub, mattia.gollub@bsse.ethz.ch
// Computational Systems Biology group, ETH Zurich
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef SAMPLY_REPARAMETRIZED_OBJECT_H
#define SAMPLY_REPARAMETRIZED_OBJECT_H

#include "transforms/transforms.h"

namespace samply {

template <typename Object>
class ReparametrizedObject : public Object {
public:
    typedef double Scalar;
    ReparametrizedObject(Object&& object,
                         const AffineTransform<Scalar>& from_parametrization_transform,
                         const AffineTransform<Scalar>& to_parametrization_transform);

    ReparametrizedObject(Object&& object);

    const AffineTransform<Scalar>& from_frame() const;
    const AffineTransform<Scalar>& to_frame() const;
    const bool needs_frame() const
    {
        return needs_frame_;
    }

private:
    AffineTransform<Scalar> from_parametrization_transform_;
    AffineTransform<Scalar> to_parametrization_transform_;
    bool needs_frame_;
};

//==============================================================================
//	ReparametrizedObject public methods implementation.
//==============================================================================

template <typename Object>
ReparametrizedObject<Object>::ReparametrizedObject(
    Object&& object,
    const AffineTransform<Scalar>& from_parametrization_transform,
    const AffineTransform<Scalar>& to_parametrization_transform)
    : Object(object),
      from_parametrization_transform_(from_parametrization_transform),
      to_parametrization_transform_(to_parametrization_transform),
      needs_frame_(true)
{
}

template <typename Object>
ReparametrizedObject<Object>::ReparametrizedObject(Object&& object)
    : Object(object),
      from_parametrization_transform_(Matrix<Scalar>(), Vector<Scalar>()),
      to_parametrization_transform_(Matrix<Scalar>(), Vector<Scalar>()),
      needs_frame_(false)
{
}

template <typename Object>
inline const AffineTransform<typename ReparametrizedObject<Object>::Scalar>&
ReparametrizedObject<Object>::from_frame() const
{
    return from_parametrization_transform_;
}

template <typename Object>
inline const AffineTransform<typename ReparametrizedObject<Object>::Scalar>&
ReparametrizedObject<Object>::to_frame() const
{
    return to_parametrization_transform_;
}

}  // namespace samply

#endif