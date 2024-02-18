// Copyright (c) 2021 ETH Zurich, Mattia Gollub (mattia.gollub@bsse.ethz.ch)
// Computational Systems Biology group, D-BSSE
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef PTA_UTILITIES_H
#define PTA_UTILITIES_H

#include "settings.h"
#include <algorithm>
#include <vector>

namespace pta {
namespace utils {

template <class InputIt, class UnaryPredicate>
constexpr InputIt find_if_precedent(InputIt first, InputIt last, UnaryPredicate p)
{
    for (; first != last; ++first) {
        if (p(*(first - 1), *first)) {
            return first;
        }
    }
    return last;
}

template <class ForwardIt, class UnaryPredicate>
inline ForwardIt remove_if_precedent(ForwardIt first, ForwardIt last, UnaryPredicate p)
{
    ++first;
    first = find_if_precedent(first, last, p);
    if (first != last)
        for (ForwardIt i = first; ++i != last;)
            if (!p(*(i - 1), *i))
                *first++ = std::move(*i);
    return first;
}

inline std::vector<size_t>
get_chains_per_thread(const size_t num_chains, const size_t num_threads)
{
    const size_t min_chains_per_thread = num_chains / num_threads;
    const size_t reminder = num_chains - min_chains_per_thread * num_threads;

    if (min_chains_per_thread == 0u) {
        return std::vector<size_t>(reminder, 1u);
    }
    else {
        std::vector<size_t> result(num_threads, min_chains_per_thread);
        for (size_t i = 0u; i < reminder; ++i)
            result[i]++;
        return result;
    }
}

inline size_t estimate_num_states(const samply::Settings& settings)
{
    return (settings.num_steps - settings.num_skipped_steps) / settings.steps_thinning;
}

} // namespace utils
} // namespace pta

#endif