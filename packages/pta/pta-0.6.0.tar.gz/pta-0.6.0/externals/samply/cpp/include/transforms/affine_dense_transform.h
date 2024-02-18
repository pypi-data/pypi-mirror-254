// Copyright(C) 2018 Mattia Gollub, mattia.gollub@bsse.ethz.ch
// Computational Systems Biology group, ETH Zurich
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef SAMPLY_AFFINE_DENSE_TRANSFORM_H
#define SAMPLY_AFFINE_DENSE_TRANSFORM_H

#include "affine_transform_base.h"
#include "affine_transform_storage.h"

namespace samply {

/**
 * @brief Affine transform with dense linear and translation components.
 *
 * @tparam Storage Class implementing the representation of the transform in
 * memory.
 */
template <typename Scalar, typename Storage = AffineTransformStorage<Scalar>>
class AffineDenseTransform
    : public AffineTransformBase<AffineDenseTransform<Scalar, Storage>, Storage> {
  public:
    using Base = AffineTransformBase<AffineDenseTransform<Scalar, Storage>, Storage>;
    using Base::Base;

    /**
     * @brief Applies this affine transform after another transform. The
     * resulting transform transforms a vector v as (this * (other * v)).
     *
     * @param transform Transform to which this transform is applied.
     * @return Transform resulting from the concatenation.
     */
    template <typename OtherTransform, typename OtherStorage>
    auto
    operator*(const AffineTransformBase<OtherTransform, OtherStorage>& transform) const;

    /**
     * @brief Applies this affine transform to a matrix or vector.
     *
     * @param matrix Matrix or vector to which the transform must be applied.
     * @return The transformed matrix.
     */
    template <typename MatrixType>
    auto operator*(const Eigen::MatrixBase<MatrixType>& matrix) const;

    /**
     * @brief Returns the inverse of this affine transform. If the inverse is
     * not defined for this transform, the pseudoinverse is returned.
     *
     * @return The inverse or pseudoinverse of the matrix.
     */
    auto inverse() const;
};

//==============================================================================
//	AffineDenseTransform public methods implementation.
//==============================================================================

template <typename Scalar, typename Storage>
template <typename OtherTransform, typename OtherStorage>
inline auto AffineDenseTransform<Scalar, Storage>::operator*(
    const AffineTransformBase<OtherTransform, OtherStorage>& transform) const
{
    return AffineDenseTransform<Scalar>(
        Base::get_linear() * transform.get_linear(),
        Base::get_linear() * transform.get_shift() + Base::get_shift());
}

template <typename Scalar, typename Storage>
template <typename MatrixType>
inline auto AffineDenseTransform<Scalar, Storage>::operator*(
    const Eigen::MatrixBase<MatrixType>& matrix) const
{
    return (Base::get_linear() * matrix).colwise() + Base::get_shift();
}

template <typename Scalar, typename Storage>
inline auto AffineDenseTransform<Scalar, Storage>::inverse() const
{
    Matrix<Scalar> inv_T;
    if (Base::get_linear().rows() == Base::get_linear().cols())
        // If the linear component is square, compute its inverse.
        inv_T = Base::get_linear().inverse();
    else
        // Otherwise compute the pseudoinverse.
        inv_T = Base::get_linear().completeOrthogonalDecomposition().pseudoInverse();
    return AffineDenseTransform<Scalar>(inv_T, -inv_T * Base::get_shift());
}

} // namespace samply

#endif