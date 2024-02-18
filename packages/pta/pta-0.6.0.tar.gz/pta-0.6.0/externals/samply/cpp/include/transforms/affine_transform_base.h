// Copyright(C) 2018 Mattia Gollub, mattia.gollub@bsse.ethz.ch
// Computational Systems Biology group, ETH Zurich
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef SAMPLY_AFFINE_TRANSFORM_BASE_H
#define SAMPLY_AFFINE_TRANSFORM_BASE_H

#include <Eigen/Core>

#include "../commons.h"
#include "../rays_packet.h"

namespace samply {

template <class>
struct Traits {
};
template <template <class, class> class _Transform, class _Scalar, class _Storage>
struct Traits<_Transform<_Scalar, _Storage>> {
    template <class _ScalarType, class _StorageType>
    using TransformType = _Transform<_ScalarType, _StorageType>;
    using ScalarType = _Scalar;
    using StorageType = _Storage;
};

/**
 * @brief Interface for classes implementing affine transforms.
 *
 * @tparam Transform Class providing a specific affine transform implementation.
 * @tparam Storage Class implementing the representation of the transform in
 * memory.
 */
template <typename Derived, typename Storage>
class AffineTransformBase {
public:
    AffineTransformBase() = delete;

    using ScalarType = typename Traits<Derived>::ScalarType;

    /**
     * @brief Construct a new AffineTransformBase object.
     *
     * @param T Linear part of the transform.
     * @param shift Translation part of the transform.
     */
    AffineTransformBase(const Matrix<ScalarType>& T, const Vector<ScalarType>& shift);

    /**
     * @brief Constructs a new AffineTransformBase object from existing storage.
     *
     * @param storage Object containing an existing memory representation of the
     * affine transform.
     */
    AffineTransformBase(const Storage& storage);

    /**
     * @brief Move-constructs a new AffineTransformBase object from existing
     * storage.
     *
     * @param storage Object containing an existing memory representation of the
     * affine transform.
     */
    AffineTransformBase(Storage&& storage);

    /**
     * @brief Copy-constructs a new AffineTransformBase object from an existing
     * transform.
     *
     * @param storage Object containing the transform that must be copied into
     * th newly created instance.
     */
    template <typename OtherTransform, typename OtherStorage>
    AffineTransformBase(const AffineTransformBase<OtherTransform, OtherStorage>& other);

    /**
     * @brief Move-constructs a new AffineTransformBase object from an existing
     * transform.
     *
     * @param storage Object containing the transform that must be moved into
     * th newly created instance.
     */
    template <typename OtherTransform, typename OtherStorage>
    AffineTransformBase(AffineTransformBase<OtherTransform, OtherStorage>&& other);

    /**
     * @brief Apply this affine transform after another transform. The
     * resulting transform transforms a vector v as (this * (other * v)).
     *
     * @param transform Transform to which this transform is applied.
     * @return Transform resulting from the concatenation.
     */
    template <typename OtherTransform, typename OtherStorage>
    auto operator*(
        const AffineTransformBase<OtherTransform, OtherStorage>& transform) const;

    /**
     * @brief Apply this affine transform to a matrix or vector.
     *
     * @param matrix Matrix or vector to which the transform must be applied.
     * @return The transformed matrix.
     */
    template <typename MatrixType>
    auto operator*(const Eigen::MatrixBase<MatrixType>& matrix) const;

    /**
     * @brief Apply this affine transform to a RaysPacket object.
     *
     * @param rays Rays to which the transform must be applied.
     * @return The transformed rays.
     */
    RaysPacket<ScalarType> operator*(const RaysPacket<ScalarType>& rays) const;

    /**
     * @brief Returns a new affine transform containing only the linear part of
     * this transform.
     *
     * @return The linear part of the transform.
     */
    auto linear() const;

    /**
     * @brief Returns the inverse of this affine transform. If the inverse is
     * not defined for this transform, the pseudoinverse is returned.
     *
     * @return The inverse or pseudoinverse of the matrix.
     */
    auto inverse() const;

    /**
     * @brief Gets a constant reference to the linear part of this transform.
     *
     * @return Constant reference to the linear part of this transform.
     */
    const Matrix<ScalarType>& get_linear() const noexcept;

    /**
     * @brief Gets a constant reference to the translation part of this
     * transform.
     *
     * @return Constant reference to the translation part of this transform.
     */
    const Vector<ScalarType>& get_shift() const noexcept;

    /**
     * @brief Gets a constant reference to the diagonal of the linear part of
     * this transform.
     *
     * @return Constant reference to the diagonal of the linear part of this
     * transform.
     */
    const Vector<ScalarType>& get_diagonal() const noexcept;

    const Storage& get_storage() const
    {
        return storage_;
    }

protected:
    // Memory representation of the transform.
    Storage storage_;
};

//==============================================================================
//	AffineTransformBase public methods implementation.
//==============================================================================

template <typename Transform, typename Storage>
inline AffineTransformBase<Transform, Storage>::AffineTransformBase(
    const Matrix<ScalarType>& T, const Vector<ScalarType>& shift)
    : storage_(T, shift)
{
}

template <typename Transform, typename Storage>
inline AffineTransformBase<Transform, Storage>::AffineTransformBase(
    const Storage& storage)
    : storage_(storage)
{
}

template <typename Transform, typename Storage>
inline AffineTransformBase<Transform, Storage>::AffineTransformBase(Storage&& storage)
    : storage_(std::move(storage))
{
}

template <typename Transform, typename Storage>
template <typename OtherTransform, typename OtherStorage>
inline AffineTransformBase<Transform, Storage>::AffineTransformBase(
    const AffineTransformBase<OtherTransform, OtherStorage>& other)
    : storage_(other.get_storage())
{
}

template <typename Transform, typename Storage>
template <typename OtherTransform, typename OtherStorage>
inline AffineTransformBase<Transform, Storage>::AffineTransformBase(
    AffineTransformBase<OtherTransform, OtherStorage>&& other)
    : storage_(std::move(other.storage_))
{
}

template <typename Transform, typename Storage>
template <typename OtherTransform, typename OtherStorage>
inline auto AffineTransformBase<Transform, Storage>::operator*(
    const AffineTransformBase<OtherTransform, OtherStorage>& transform) const
{
    return static_cast<Transform&>(*this).operator*(transform);
}

template <typename Transform, typename Storage>
template <typename MatrixType>
inline auto AffineTransformBase<Transform, Storage>::operator*(
    const Eigen::MatrixBase<MatrixType>& matrix) const
{
    return static_cast<Transform&>(*this).operator*(matrix);
}

template <typename Transform, typename Storage>
inline RaysPacket<typename Traits<Transform>::ScalarType>
AffineTransformBase<Transform, Storage>::operator*(
    const RaysPacket<ScalarType>& rays) const
{
    return static_cast<Transform&>(*this).operator*(rays);
}

template <typename Transform, typename Storage>
inline auto AffineTransformBase<Transform, Storage>::linear() const
{
    return static_cast<Transform&>(*this).linear();
}

template <typename Transform, typename Storage>
inline auto AffineTransformBase<Transform, Storage>::inverse() const
{
    return static_cast<Transform&>(*this).inverse();
}

template <typename Transform, typename Storage>
inline const Matrix<typename Traits<Transform>::ScalarType>&
AffineTransformBase<Transform, Storage>::get_linear() const noexcept
{
    return storage_.get_linear();
}

template <typename Transform, typename Storage>
inline const Vector<typename Traits<Transform>::ScalarType>&
AffineTransformBase<Transform, Storage>::get_shift() const noexcept
{
    return storage_.get_shift();
}

template <typename Transform, typename Storage>
inline const Vector<typename Traits<Transform>::ScalarType>&
AffineTransformBase<Transform, Storage>::get_diagonal() const noexcept
{
    return storage_.get_diagonal();
}

}  // namespace samply

#endif