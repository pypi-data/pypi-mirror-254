// Copyright(C) 2018 Mattia Gollub, mattia.gollub@bsse.ethz.ch
// Computational Systems Biology group, ETH Zurich
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef SAMPLY_ROW_SELECTION_TRANSFORM_H
#define SAMPLY_ROW_SELECTION_TRANSFORM_H

#include "affine_transform_base.h"
#include "affine_transform_storage.h"

namespace samply {

/**
 * @brief Row-selection transform.
 *
 * @tparam Storage Class implementing the representation of the transform in
 * memory.
 */
template <typename Scalar, typename Storage = AffineTransformStorage<Scalar>>
class RowSelectionTransform
    : public AffineTransformBase<RowSelectionTransform<Scalar, Storage>, Storage> {
  public:
    using Base = AffineTransformBase<RowSelectionTransform<Scalar, Storage>, Storage>;
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
//	RowSelectionTransform public methods implementation.
//==============================================================================

template <typename Scalar, typename Storage>
template <typename OtherTransform, typename OtherStorage>
inline auto RowSelectionTransform<Scalar, Storage>::operator*(
    const AffineTransformBase<OtherTransform, OtherStorage>& transform) const
{
    return AffineDenseTransform<Scalar>(
        transform.get_linear()(Base::get_storage().get_indices(), Eigen::all),
        transform.get_shift()(Base::get_storage().get_indices()));
}

template <typename Scalar, typename Storage>
template <typename MatrixType>
inline auto RowSelectionTransform<Scalar, Storage>::operator*(
    const Eigen::MatrixBase<MatrixType>& matrix) const
{
    return matrix(Base::get_storage().get_indices(), Eigen::all);
}

template <typename Scalar, typename Storage>
inline auto RowSelectionTransform<Scalar, Storage>::inverse() const
{
    Matrix<Scalar> inv_T;
    if (Base::get_linear().rows() == Base::get_linear().cols())
        inv_T = Base::get_linear().inverse();
    else
        inv_T = Base::get_linear().completeOrthogonalDecomposition().pseudoInverse();
    return RowSelectionTransform(inv_T, Eigen::VectorXd::Zero(inv_T.rows()));
}

} // namespace samply

#endif