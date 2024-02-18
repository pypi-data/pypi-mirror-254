// Copyright(C) 2018 Mattia Gollub, mattia.gollub@bsse.ethz.ch
// Computational Systems Biology group, ETH Zurich
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef SAMPLY_IDENTITY_TRANSFORM_H
#define SAMPLY_IDENTITY_TRANSFORM_H

#include "affine_transform_base.h"

namespace samply {

/**
 * @brief Identity affine transform.
 *
 * @tparam Storage Class implementing the representation of the transform in
 * memory.
 */
template <typename Scalar, typename Storage = AffineTransformStorage<Scalar>>
class IdentityTransform
    : public AffineTransformBase<IdentityTransform<Scalar, Storage>, Storage> {
  public:
    using Base = AffineTransformBase<IdentityTransform<Scalar, Storage>, Storage>;
    using Base::Base;

    /**
     * @brief Constructs a new IdentityTransform object of the desired size.
     *
     * @param n_dimensions Number of dimensions of the desired transform.
     */
    IdentityTransform(const Eigen::Index n_dimensions);

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
    const Eigen::MatrixBase<MatrixType>&
    operator*(const Eigen::MatrixBase<MatrixType>& matrix) const;

    /**
     * @brief Returns the inverse of this affine transform. If the inverse is
     * not defined for this transform, the pseudoinverse is returned.
     *
     * @return The inverse or pseudoinverse of the matrix.
     */
    auto inverse() const;
};

//==============================================================================
//	IdentityTransform public methods implementation.
//==============================================================================

template <typename Scalar, typename Storage>
inline IdentityTransform<Scalar, Storage>::IdentityTransform(
    const Eigen::Index n_dimensions)
    : AffineTransformBase<IdentityTransform, Storage>(
          Eigen::MatrixXd::Identity(n_dimensions, n_dimensions),
          Eigen::VectorXd::Zero(n_dimensions))
{}

template <typename Scalar, typename Storage>
template <typename OtherTransform, typename OtherStorage>
inline auto IdentityTransform<Scalar, Storage>::operator*(
    const AffineTransformBase<OtherTransform, OtherStorage>& transform) const
{
    return transform;
}

template <typename Scalar, typename Storage>
template <typename MatrixType>
inline const Eigen::MatrixBase<MatrixType>&
IdentityTransform<Scalar, Storage>::operator*(
    const Eigen::MatrixBase<MatrixType>& matrix) const
{
    return matrix;
}

template <typename Scalar, typename Storage>
inline auto IdentityTransform<Scalar, Storage>::inverse() const
{
    return IdentityTransform(Base::get_shift().size());
}

} // namespace samply

#endif