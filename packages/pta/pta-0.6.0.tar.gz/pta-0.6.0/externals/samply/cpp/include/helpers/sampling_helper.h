// Copyright (c) 2020 ETH Zurich, Mattia Gollub (mattia.gollub@bsse.ethz.ch)
// Computational Systems Biology group, D-BSSE
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef SAMPLY_SAMPLING_HELPER_H
#define SAMPLY_SAMPLING_HELPER_H

#include <Eigen/Dense>
#include <chrono>
#include <cmath>
#include <numeric>
#include <pcg_random.hpp>
#include <random>
#include <stdexcept>
#include <type_traits>

#include "../commons.h"
#include "../externals/rtnorm/rtnorm.hpp"

namespace samply {

/**
 * @brief Helper class for generating random elements.
 */
class SamplingHelper {
  public:
    /**
     * @brief Construct a new instance of the SamplingHelper class.
     */
    SamplingHelper()
        : generator(static_cast<unsigned int>(
              std::chrono::system_clock::now().time_since_epoch().count()))
    {}

    /**
     * @brief Get a random scalar element within the specified bounds.
     *
     * @tparam Scalar Type of the random scalar.
     * @param lower_bound Minimum value of the sampled scalar.
     * @param upper_bound Maximum value of the sampled scalar.
     * @return A random element within the specified bounds.
     */
    template <typename Scalar>
    Scalar
    get_random_uniform_scalar(const Scalar lower_bound, const Scalar upper_bound);

    /**
     * @brief Create a matrix with elements uniformly distributed between the
     * given bounds.
     *
     * @tparam Scalar Type of the elements of the matrix.
     * @param lower_bound Lower bound of the uniform interval.
     * @param upper_bound Upper bound of the uniform interval.
     * @param num_rows Number of rows.
     * @param num_cols Number of columns.
     * @return num_rows-by-num_cols matrix containing the generated elements.
     */
    template <typename Scalar>
    Matrix<Scalar> get_random_uniform(
        const Scalar lower_bound,
        const Scalar upper_bound,
        const Eigen::Index num_rows,
        const Eigen::Index num_cols);

    /**
     * @brief Create a matrix with elements uniformly distributed between the
     * given bounds.
     *
     * @tparam Derived1 Type of the matrix providing the lower bounds.
     * @tparam Derived2 Type of the matrix providing the upper bounds.
     * @param lower_bounds Matrix containing the lower bounds for each element
     * of the output matrix.
     * @param upper_bounds Matrix containing the upper bounds for each element
     * of the output matrix.
     * @return Matrix containing the generated elements.
     */
    template <typename Derived1, typename Derived2>
    auto get_random_uniform(
        const Eigen::MatrixBase<Derived1>& lower_bounds,
        const Eigen::MatrixBase<Derived2>& upper_bounds);

    /**
     * @brief Created a matrix with normally distributed random elements.
     *
     * @tparam Scalar Type of the random elements.
     * @tparam Rows Number of rows of the matrix.
     * @tparam Cols Number of columns of the matrix.
     * @param mean Mean of the normal distribution used to generated the
     * elements.
     * @param std_dev Standard deviation of the normal distribution used to
     * generated the elements.
     * @param num_rows Number of rows.
     * @param num_cols Number of columns.
     * @return Matrix containing the generated elements.
     */
    template <typename Scalar>
    void get_random_normals(
        Matrix<Scalar>& output_normals,
        const Scalar mean,
        const Scalar std_dev,
        const int num_rows,
        const int num_cols);

    /**
     * @brief Create a matrix of uniformly distributed random directions.
     *
     * @tparam Scalar Type of the elements of the vector.
     * @tparam NumDimensions Dimensionality of the direction vectors.
     * @tparam NumDirections Number of direction vectors to generate.
     * @param num_dimensions Dimensionality of the direction vectors.
     * @param num_directions Number of direction vectors to generate.
     * @return Matrix containing the generated direction vectors.
     */
    template <typename Scalar>
    void get_random_directions(
        Matrix<Scalar>& output_directions,
        const int num_dimensions,
        const int num_directions);

    /**
     * @brief Get a vector of random integers within a given interval.
     *
     * @param min_value Lower bound of the random elements.
     * @param max_value Upper bound of the random elements.
     * @param num_values Number of elements to generate.
     * @return Vector containing the random integers.
     */
    void get_random_integers(
        IndexVector& output_indices,
        const Index min_value,
        const Index max_value,
        const size_t num_values);

    /**
     * @brief Sample an index given weights for each element.
     *
     * @tparam Scalar Type of the weights.
     * @param index_weights Vector containing the weights of each index.
     * @return The sampled index.
     */
    template <typename Scalar>
    Eigen::Index
    sample_index_with_weights(const Eigen::Ref<const Vector<Scalar>>& index_weights);

    /**
     * @brief Sample a random element from a truncated normal distribution.
     *
     * @tparam Scalar Type of the sampled element.
     * @param mean Mean of the normal distribution.
     * @param sigma Standard deviation of the normal distribution.
     * @param lower_bound Lower bound of the truncated area.
     * @param upper_bound Upper bound of the truncated area.
     * @return The sampled element.
     */
    template <typename Scalar>
    Scalar get_random_truncated_normal(
        const Scalar mean,
        const Scalar sigma,
        const Scalar lower_bound,
        const Scalar upper_bound);

    /**
     * @brief Compute the Cumulative Density Function (CDF) of a standard normal
     * distribution at a given value.
     *
     * @tparam Scalar Type of the returned value.
     * @param b Point at which the CDF must be computed.
     * @return The CDF at the given point.
     */
    template <typename Scalar> Scalar get_normal_cdf(const Scalar b) const;

    /**
     * @brief Compute the Cumulative Density Function (CDF) of a standard normal
     * distribution within the specified intervals.
     *
     * @tparam Scalar Type of the returned values.
     * @param a Lower bounds of the intervals.
     * @param b Upper bounds of the intervals.
     * @return The CDFs on the given intervals.
     */
    template <typename Scalar>
    auto
    get_normal_cdf_interval(const Vector<Scalar>& a, const Vector<Scalar>& b) const;

    template <typename Scalar>
    void get_normal_cdf_interval(
        Eigen::Ref<Vector<Scalar>> result_cdf,
        const Eigen::Ref<const Vector<Scalar>>& a,
        const Eigen::Ref<const Vector<Scalar>>& b,
        const Scalar mean,
        const Scalar std) const;

  private:
    // Type of the random engine used by the helper.
    typedef pcg32 Generator;

    // The random engine used by the helper.
    Generator generator;

    // Persistent distribution definitions to allow return of Eigen expressions.
    std::uniform_real_distribution<double> uniform_double_distribution_;
    std::uniform_real_distribution<float> uniform_float_distribution_;
    Matrix<double> random_normals_double_;

    static constexpr double sqrt2_inv_ = 0.7071067811865475244008443621048490392;
};

//==============================================================================
//	SamplingHelper public methods implementation.
//==============================================================================

template <typename Scalar>
inline Scalar SamplingHelper::get_random_uniform_scalar(
    const Scalar lower_bound, const Scalar upper_bound)
{
    std::uniform_real_distribution<Scalar> distribution(lower_bound, upper_bound);
    return distribution(generator);
}

template <typename Scalar>
inline Matrix<Scalar> SamplingHelper::get_random_uniform(
    const Scalar lower_bound,
    const Scalar upper_bound,
    const Eigen::Index num_rows,
    const Eigen::Index num_cols)
{
    assert(num_rows > 0 && num_cols > 0);
    std::uniform_real_distribution<Scalar> distribution(lower_bound, upper_bound);
    return Matrix<Scalar>::NullaryExpr(
        num_rows, num_cols, [&]() { return distribution(generator); });
}

template <typename Derived1, typename Derived2>
auto SamplingHelper::get_random_uniform(
    const Eigen::MatrixBase<Derived1>& lower_bounds,
    const Eigen::MatrixBase<Derived2>& upper_bounds)
{
    // Validate inputs.
    EIGEN_STATIC_ASSERT_SAME_MATRIX_SIZE(Derived1, Derived2);
    assert(
        lower_bounds.rows() == upper_bounds.rows() &&
        lower_bounds.cols() == upper_bounds.cols());

    const auto interval_width = upper_bounds - lower_bounds;

    // If possible, return an expression using a member distribution object to avoid
    // allocation of a temporary result. Otherwise, return an evaluated matrix.
    if constexpr (std::is_same<typename Derived1::Scalar, double>::value) {
        return Matrix<typename Derived1::Scalar>::NullaryExpr(
                   lower_bounds.rows(), lower_bounds.cols(),
                   [&]() { return uniform_double_distribution_(generator); })
                   .cwiseProduct(interval_width) +
               lower_bounds;
    }
    else {
        std::uniform_real_distribution<typename Derived1::Scalar> distribution;
        return (Matrix<typename Derived1::Scalar>::NullaryExpr(
                    lower_bounds.rows(), lower_bounds.cols(),
                    [&]() { return distribution(generator); })
                    .cwiseProduct(interval_width) +
                lower_bounds)
            .eval();
    }
}

template <typename Scalar>
inline void SamplingHelper::get_random_normals(
    Matrix<Scalar>& output_normals,
    const Scalar mean,
    const Scalar std_dev,
    const int num_rows,
    const int num_cols)
{
    assert(num_rows > 0 && num_cols > 0);
    std::normal_distribution<Scalar> distribution(mean, std_dev);
    output_normals = Matrix<Scalar>::NullaryExpr(
        num_rows, num_cols, [&]() { return distribution(generator); });
}

template <typename Scalar>
inline void SamplingHelper::get_random_directions(
    Matrix<Scalar>& output_directions,
    const int num_dimensions,
    const int num_directions)
{
    if constexpr (std::is_same<Scalar, double>::value) {
        get_random_normals<Scalar>(
            random_normals_double_, static_cast<Scalar>(0), static_cast<Scalar>(1),
            num_dimensions, num_directions);
        output_directions.noalias() =
            random_normals_double_ *
            random_normals_double_.colwise().norm().cwiseInverse().asDiagonal();
    }
    else {
        Matrix<Scalar> random_normals;
        get_random_normals<Scalar>(
            random_normals_double_, static_cast<Scalar>(0), static_cast<Scalar>(1),
            num_dimensions, num_directions);
        output_directions.noalias() =
            random_normals *
            random_normals.colwise().norm().cwiseInverse().asDiagonal();
    }
}

inline void SamplingHelper::get_random_integers(
    IndexVector& output_integers,
    const Index min_value,
    const Index max_value,
    const size_t num_values)
{
    std::uniform_int_distribution<> distribution(min_value, max_value);
    output_integers =
        IndexVector::NullaryExpr(num_values, [&]() { return distribution(generator); });
}

template <typename Scalar>
inline Eigen::Index SamplingHelper::sample_index_with_weights(
    const Eigen::Ref<const Vector<Scalar>>& index_weights)
{
    static_assert(
        std::is_same<Scalar, double>::value || std::is_same<Scalar, float>::value,
        "Unsupported scalar type");
    const Scalar weights_sum = index_weights.sum();
    Scalar sample;
    if constexpr (std::is_same<Scalar, double>::value) {
        sample = uniform_double_distribution_(generator) * weights_sum;
    }
    else {
        sample = uniform_float_distribution_(generator) * weights_sum;
    }

    // STL's discrete_distribution is too slow as it allocates new vectors, so we use
    // our own allocation-free version.
    Scalar sum = 0.0;
    for (Eigen::Index i = 0; i < index_weights.size(); i++) {
        sum += index_weights(i);
        if (sample <= sum)
            return i;
    }

    throw std::runtime_error("The sampled value is outside the weights range");
}

template <typename Scalar>
inline Scalar SamplingHelper::get_random_truncated_normal(
    const Scalar mean,
    const Scalar sigma,
    const Scalar lower_bound,
    const Scalar upper_bound)
{
    return static_cast<Scalar>(
        rtnorm(generator, lower_bound, upper_bound, mean, sigma));
}

template <typename Scalar>
inline Scalar SamplingHelper::get_normal_cdf(const Scalar b) const
{
    // https://en.cppreference.com/w/cpp/numeric/math/erfc
    return std::erfc(-b * Scalar(sqrt2_inv_)) * Scalar(0.5);
}

template <typename Scalar>
inline auto SamplingHelper::get_normal_cdf_interval(
    const Vector<Scalar>& a, const Vector<Scalar>& b) const
{
    return b.unaryExpr([this](const Scalar x) { return get_normal_cdf(x); }) -
           a.unaryExpr([this](const Scalar x) { return get_normal_cdf(x); });
}

template <typename Scalar>
inline void SamplingHelper::get_normal_cdf_interval(
    Eigen::Ref<Vector<Scalar>> result_cdf,
    const Eigen::Ref<const Vector<Scalar>>& a,
    const Eigen::Ref<const Vector<Scalar>>& b,
    const Scalar mean,
    const Scalar std) const
{
    const Scalar std_inv = 1 / std;
    result_cdf = ((b.array() - mean) * std_inv).unaryExpr([this](const Scalar x) {
        return get_normal_cdf(x);
    }) - ((a.array() - mean) * std_inv).unaryExpr([this](const Scalar x) {
        return get_normal_cdf(x);
    });
}

} // namespace samply

#endif
