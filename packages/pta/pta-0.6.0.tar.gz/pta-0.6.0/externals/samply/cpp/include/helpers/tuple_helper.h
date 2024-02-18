// Copyright (c) 2020 ETH Zurich, Mattia Gollub (mattia.gollub@bsse.ethz.ch)
// Computational Systems Biology group, D-BSSE
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef SAMPLY_TUPLE_HELPER_H
#define SAMPLY_TUPLE_HELPER_H

#include <tuple>

namespace samply {
namespace detail {

/**
 * @brief Meta-container for a sequence of indices.
 *
 * @tparam Indices The indices stored in the container.
 */
template <int... Indices>
struct sequence {
};

/**
 * @brief Meta-generator for a sequence of numbers.
 *
 * @tparam N Length of the sequence left to generate.
 * @tparam Indices Indices that have already been generated.
 */
template <int N, int... Indices>
struct generate_sequence : generate_sequence<N - 1, N - 1, Indices...> {
};

/**
 * @brief Final case for the meta-generator.
 *
 * @tparam Is All generated indices of the sequence.
 */
template <int... Indices>
struct generate_sequence<0, Indices...> : sequence<Indices...> {
};

/**
 * @brief Apply a function on the elements of a tuple corresponding to the given
 * indices.
 *
 * @tparam Tuple Type of the tuple.
 * @tparam Func Type of the function.
 * @tparam Indices Indices of the elements to which the function must be
 * applied.
 * @param tuple Tuple containing the elements.
 * @param function Function to be applied on the selected elements of the tuple.
 */
template <typename Tuple, typename Func, int... Indices>
void for_each(Tuple&& tuple, Func function, sequence<Indices...>)
{
    const auto ignore = {(function(std::get<Indices>(tuple)), 0)...};
}

}  // namespace detail

/**
 * @brief Apply a function on all each element of the tuple.
 * @remark In the future this should be replaced by C++17's std::apply()
 *
 * @tparam Func Type of the function.
 * @tparam Ts Types of the elements of the tuple.
 * @param tuple The target tuple.
 * @param function The function to be applied on the elements of the tuple.
 */
template <typename Func, typename... Ts>
void for_each_in_tuple(std::tuple<Ts...>& tuple, Func function)
{
    detail::for_each(tuple, function, detail::generate_sequence<sizeof...(Ts)>());
}

}  // namespace samply

#endif