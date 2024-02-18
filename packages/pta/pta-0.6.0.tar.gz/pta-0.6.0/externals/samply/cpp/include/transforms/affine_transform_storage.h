// Copyright(C) 2018 Mattia Gollub, mattia.gollub@bsse.ethz.ch
// Computational Systems Biology group, ETH Zurich
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef SAMPLY_AFFINE_TRANSFORM_STORAGE_H
#define SAMPLY_AFFINE_TRANSFORM_STORAGE_H

#include <Eigen/Core>

#include "../commons.h"

namespace samply {

template <typename Scalar>
class AffineTransformStorageRef;

template <typename Scalar>
class AffineTransformStorageConstRef;

/**
 * @brief Class describing dense storage of an affine transform. Beside the
 * linear and translation components, the class stores the diagonal of the
 * linear component in a separate vector.
 *
 */
template <typename ScalarType>
class AffineTransformStorage {
public:
    typedef ScalarType Scalar;
    AffineTransformStorage() = delete;

    /**
     * @brief Constructs a new AffineTransformStorage object.
     *
     * @param T Linear component of the transform.
     * @param shift Translation component of the transform.
     */
    AffineTransformStorage(const Matrix<Scalar>& T, const Vector<Scalar>& shift);

    /**
     * @brief Copy-constructs a new AffineTransformStorage object.
     *
     * @param other The object that must be copied into the newly created one.
     */
    AffineTransformStorage(const AffineTransformStorage<Scalar>& other);

    /**
     * @brief Copy-constructs a new AffineTransformStorage object.
     *
     * @param other The object that must be copied into the newly created one.
     */
    AffineTransformStorage(const AffineTransformStorageRef<Scalar>& other);

    /**
     * @brief Copy-constructs a new AffineTransformStorage object.
     *
     * @param other The object that must be copied into the newly created one.
     */
    AffineTransformStorage(const AffineTransformStorageConstRef<Scalar>& other);

    /**
     * @brief Move-constructs a new AffineTransformStorage object.
     *
     * @param other The object that must be moved into the newly created one.
     */
    AffineTransformStorage(AffineTransformStorage<Scalar>&& other);

    /**
     * @brief Sets the linear component of the transform. This updates the
     * diagonal as well.
     *
     * @param linear The linear component of the transform.
     */
    void set_linear(const Matrix<Scalar>& linear);

    /**
     * @brief Sets the translation component of the transform.
     *
     * @param shift The translation component of the transform.
     */
    void set_shift(const Vector<Scalar>& shift);

    /**
     * @brief Sets the diagonal of the linear component of the transform. This
     * sets the off-diagonal elements to zero.
     *
     * @param diagonal The diagonal of the linear component of the transform.
     */
    void set_diagonal_linear(const Vector<Scalar>& diagonal);

    /**
     * @brief Gets the linear component of the transform.
     *
     * @return The linear component of the transform.
     */
    const Matrix<Scalar>& get_linear() const noexcept
    {
        return T_;
    }

    /**
     * @brief Gets the shift component of the transform.
     *
     * @return The shift component of the transform.
     */
    const Vector<Scalar>& get_shift() const noexcept
    {
        return shift_;
    }

    /**
     * @brief Gets the diagonal of the linear component of the transform.
     *
     * @return The diagonal of the linear component of the transform.
     */
    const Vector<Scalar>& get_diagonal() const noexcept
    {
        return diagonal_;
    }

    /**
     * @brief Gets the indices associated with the transform (may be unused).
     *
     * @return The indices associated with the linear transform.
     */
    const Vector<Eigen::Index>& get_indices() const noexcept
    {
        return indices_;
    }

protected:
    Matrix<Scalar> T_;
    Vector<Scalar> shift_;
    Vector<Scalar> diagonal_;
    Vector<Eigen::Index> indices_;
};

/**
 * @brief Class representing a reference to an existing storage object. Allows
 * to build affine transform which use existing data without triggering copies.
 *
 * @note Owners of an AffineTransformStorageRef object are responsible of the
 * validity of the underlying storage object during the lifetime of the
 * reference.
 */
template <typename ScalarType>
class AffineTransformStorageRef {
public:
    typedef ScalarType Scalar;

    AffineTransformStorageRef() = delete;

    /**
     * @brief Constructs a new AffineTransformStorageRef object.
     *
     * @param An existing AffineTransformStorage object.
     */
    AffineTransformStorageRef(AffineTransformStorage<Scalar>& storage)
        : storage_ref_(storage)
    {
    }

    /**
     * @brief Gets the linear component of the transform.
     *
     * @return The linear component of the transform.
     */
    const Matrix<Scalar>& get_linear() const noexcept
    {
        return storage_ref_.get_linear();
    }

    /**
     * @brief Gets the shift component of the transform.
     *
     * @return The shift component of the transform.
     */
    const Vector<Scalar>& get_shift() const noexcept
    {
        return storage_ref_.get_shift();
    }

    /**
     * @brief Gets the diagonal of the linear component of the transform.
     *
     * @return The diagonal of the linear component of the transform.
     */
    const Vector<Scalar>& get_diagonal() const noexcept
    {
        return storage_ref_.get_diagonal();
    }

    /**
     * @brief Gets the indices associated with the transform (may be unused).
     *
     * @return The indices associated with the linear transform.
     */
    const Vector<Eigen::Index>& get_indices() const noexcept
    {
        return storage_ref_.get_indices();
    }

private:
    AffineTransformStorage<Scalar>& storage_ref_;
};

/**
 * @brief Class representing a constant reference to an existing storage object.
 * Allows to build affine transform which use existing data without triggering
 * copies.
 *
 * @note Owners of an AffineTransformStorageConstRef object are responsible of
 * the validity of the underlying storage object during the lifetime of the
 * reference.
 */
template <typename ScalarType>
class AffineTransformStorageConstRef {
public:
    typedef ScalarType Scalar;

    AffineTransformStorageConstRef() = delete;

    /**
     * @brief Constructs a new AffineTransformStorageConstRef object.
     *
     * @param An existing AffineTransformStorage object.
     */
    AffineTransformStorageConstRef(const AffineTransformStorage<Scalar>& storage)
        : storage_ref_(storage)
    {
    }

    /**
     * @brief Gets the linear component of the transform.
     *
     * @return The linear component of the transform.
     */
    const Matrix<Scalar>& get_linear() const noexcept
    {
        return storage_ref_.get_linear();
    }

    /**
     * @brief Gets the shift component of the transform.
     *
     * @return The shift component of the transform.
     */
    const Vector<Scalar>& get_shift() const noexcept
    {
        return storage_ref_.get_shift();
    }

    /**
     * @brief Gets the diagonal of the linear component of the transform.
     *
     * @return The diagonal of the linear component of the transform.
     */
    const Vector<Scalar>& get_diagonal() const noexcept
    {
        return storage_ref_.get_diagonal();
    }

    /**
     * @brief Gets the indices associated with the transform (may be unused).
     *
     * @return The indices associated with the linear transform.
     */
    const Vector<Eigen::Index>& get_indices() const noexcept
    {
        return storage_ref_.get_indices();
    }

private:
    const AffineTransformStorage<Scalar>& storage_ref_;
};

//==============================================================================
//	AffineTransformStorage public methods implementation.
//==============================================================================

template <typename ScalarType>
inline AffineTransformStorage<ScalarType>::AffineTransformStorage(
    const Matrix<ScalarType>& T, const Vector<ScalarType>& shift)
    : T_(T),
      shift_(shift),
      diagonal_(T.diagonal()),
      indices_(Vector<Eigen::Index>::Zero(shift.size()))
{
    for (Eigen::Index i = 0; i < T_.rows(); ++i) {
        auto row = this->get_linear().row(i);
        if ((row.array() != 0.0).count() == 1)
            for (Eigen::Index j = 0; j < row.cols(); ++j) {
                if (row(j) == 1.0) {
                    indices_[i] = j;
                    break;
                }
            }
        else
            indices_[i] = -1;
    }
}

template <typename ScalarType>
inline AffineTransformStorage<ScalarType>::AffineTransformStorage(
    const AffineTransformStorage<ScalarType>& other)
    : T_(other.T_),
      shift_(other.shift_),
      diagonal_(other.diagonal_),
      indices_(other.indices_)
{
}

template <typename ScalarType>
inline AffineTransformStorage<ScalarType>::AffineTransformStorage(
    const AffineTransformStorageRef<ScalarType>& other)
    : T_(other.T_),
      shift_(other.shift_),
      diagonal_(other.diagonal_),
      indices_(other.indices_)
{
}

template <typename ScalarType>
inline AffineTransformStorage<ScalarType>::AffineTransformStorage(
    const AffineTransformStorageConstRef<ScalarType>& other)
    : T_(other.T_),
      shift_(other.shift_),
      diagonal_(other.diagonal_),
      indices_(other.indices_)
{
}

template <typename ScalarType>
inline AffineTransformStorage<ScalarType>::AffineTransformStorage(
    AffineTransformStorage<ScalarType>&& other)
    : T_(std::move(other.T_)),
      shift_(std::move(other.shift_)),
      diagonal_(std::move(other.diagonal_)),
      indices_(std::move(other.indices_))
{
}

template <typename ScalarType>
inline void AffineTransformStorage<ScalarType>::set_linear(
    const Matrix<ScalarType>& linear)
{
    T_ = linear;
    diagonal_ = linear.diagonal();
}

template <typename ScalarType>
inline void AffineTransformStorage<ScalarType>::set_shift(
    const Vector<ScalarType>& shift)
{
    shift_ = shift;
}

template <typename ScalarType>
inline void AffineTransformStorage<ScalarType>::set_diagonal_linear(
    const Vector<ScalarType>& linear)
{
    T_.setZero();
    T_.diagonal() = linear.asDiagonal();
    diagonal_ = linear.diagonal();
}

}  // namespace samply

#endif