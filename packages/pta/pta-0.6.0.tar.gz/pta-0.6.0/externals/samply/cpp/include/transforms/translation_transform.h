// Copyright(C) 2018 Mattia Gollub, mattia.gollub@bsse.ethz.ch
// Computational Systems Biology group, ETH Zurich
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef SAMPLY_TRANSLATION_TRANSFORM_H
#define SAMPLY_TRANSLATION_TRANSFORM_H

#include "affine_transform_base.h"

namespace samply {

/**
 * @brief Affine transform with identity linear component and dense translation.
 *
 * @tparam Storage Class implementing the representation of the transform in
 * memory.
 */
template <typename Scalar, typename Storage = AffineTransformStorage<Scalar>>
class TranslationTransform
    : public AffineTransformBase<TranslationTransform<Scalar, Storage>, Storage> {
public:
    using Base = AffineTransformBase<TranslationTransform<Scalar, Storage>, Storage>;
    using Base::Base;

    /**
     * @brief Applies this affine transform after another transform. The
     * resulting transform transforms a vector v as (this * (other * v)).
     *
     * @param transform Transform to which this transform is applied.
     * @return Transform resulting from the concatenation.
     */
    template <typename OtherTransform, typename OtherStorage>
    auto operator*(
        const AffineTransformBase<OtherTransform, OtherStorage>& transform) const;

    /**
     * @brief Applies this affine transform to a matrix or vector.
     *
     * @param matrix Matrix or vector to which the transform must be applied.
     * @return The transformed matrix.
     */
    template <typename MatrixType>
    Matrix<Scalar> operator*(const Eigen::MatrixBase<MatrixType>& matrix) const;

    /**
     * @brief Returns the inverse of this affine transform. If the inverse is
     * not defined for this transform, the pseudoinverse is returned.
     *
     * @return The inverse or pseudoinverse of the matrix.
     */
    auto inverse() const;
};

//==============================================================================
//	TranslationTransform public methods implementation.
//==============================================================================

template <typename Scalar, typename Storage>
template <typename OtherTransform, typename OtherStorage>
inline auto TranslationTransform<Scalar, Storage>::operator*(
    const AffineTransformBase<OtherTransform, OtherStorage>& transform) const
{
    return AffineDenseTransform<Scalar>(transform.get_linear(),
                                        transform.get_shift() + Base::get_shift());
}

template <typename Scalar, typename Storage>
template <typename MatrixType>
inline Matrix<Scalar> TranslationTransform<Scalar, Storage>::operator*(
    const Eigen::MatrixBase<MatrixType>& matrix) const
{
    if (Base::get_linear().rows() == Base::get_linear().cols()) {
        return matrix.colwise() + Base::get_shift();
    } else {
        Matrix<Scalar> result =
            Matrix<Scalar>::Zero(Base::get_linear().rows(), matrix.cols());
        result.block(0, 0, std::min(result.rows(), matrix.rows()),
                     std::min(result.cols(), matrix.cols())) =
            matrix
                .block(0, 0, std::min(result.rows(), matrix.rows()),
                       std::min(result.cols(), matrix.cols()))
                .colwise() +
            Base::get_shift();
        return result;
    }
}

template <typename Scalar, typename Storage>
inline auto TranslationTransform<Scalar, Storage>::inverse() const
{
    return TranslationTransform<Scalar>(Base::get_linear().transpose(),
                                        -Base::get_shift());
}

}  // namespace samply

#endif