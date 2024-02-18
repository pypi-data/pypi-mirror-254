// Copyright(C) 2018 Mattia Gollub, mattia.gollub@bsse.ethz.ch
// Computational Systems Biology group, ETH Zurich
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef SAMPLY_AFFINE_DIAGONAL_TRANSFORM_H
#define SAMPLY_AFFINE_DIAGONAL_TRANSFORM_H

#include "affine_dense_transform.h"
#include "affine_transform_base.h"
#include "affine_transform_storage.h"

namespace samply {

/**
 * @brief Affine transform with diagonal linear component and dense translation.
 *
 * @tparam Storage Class implementing the representation of the transform in
 * memory.
 */
template <typename Scalar, typename Storage = AffineTransformStorage<Scalar>>
class AffineDiagonalTransform
    : public AffineTransformBase<AffineDiagonalTransform<Scalar, Storage>, Storage> {
  public:
    using Base = AffineTransformBase<AffineDiagonalTransform<Scalar, Storage>, Storage>;
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
//	AffineDiagonalTransform public methods implementation.
//==============================================================================

template <typename Scalar, typename Storage>
template <typename OtherTransform, typename OtherStorage>
inline auto AffineDiagonalTransform<Scalar, Storage>::operator*(
    const AffineTransformBase<OtherTransform, OtherStorage>& transform) const
{
    return AffineDenseTransform<Scalar>(
        Base::get_diagonal().asDiagonal() * transform.get_linear(),
        Base::get_diagonal().asDiagonal() * transform.get_shift() + Base::get_shift());
}

template <typename Scalar, typename Storage>
template <typename MatrixType>
inline auto AffineDiagonalTransform<Scalar, Storage>::operator*(
    const Eigen::MatrixBase<MatrixType>& matrix) const
{
    return (Base::get_diagonal().asDiagonal() * matrix).colwise() + Base::get_shift();
}

template <typename Scalar, typename Storage>
inline auto AffineDiagonalTransform<Scalar, Storage>::inverse() const
{
    Matrix<Scalar> inv_T =
        Matrix<Scalar>::Zero(Base::get_linear().cols(), Base::get_linear().rows());
    inv_T.diagonal() = Base::get_diagonal().cwiseInverse();
    return AffineDiagonalTransform<Scalar>(inv_T, -inv_T * Base::get_shift());
}

} // namespace samply

#endif