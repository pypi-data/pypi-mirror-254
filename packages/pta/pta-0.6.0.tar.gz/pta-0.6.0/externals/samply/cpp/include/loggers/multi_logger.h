// Copyright(C) 2019 Mattia Gollub, mattia.gollub@bsse.ethz.ch
// Computational Systems Biology group, ETH Zurich
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef HYPERFLUX_MULTI_LOGGER_H
#define HYPERFLUX_MULTI_LOGGER_H

#include <helpers/tuple_helper.h>

#include <tuple>

namespace samply {

template <typename ChainState,
          typename DurationFormat,
          template <typename, typename>
          typename... Loggers>
class MultiLogger {
public:
    template <std::size_t LoggerIdx>
    using Logger = typename std::tuple_element<
        LoggerIdx,
        std::tuple<Loggers<ChainState, DurationFormat>...>>::type;

    MultiLogger(const Loggers<ChainState, DurationFormat>&... loggers)
        : loggers_(loggers...)
    {
    }

    MultiLogger(Loggers<ChainState, DurationFormat>&&... loggers) : loggers_(loggers...)
    {
    }

    void log(ChainState& chain_state,
             const DurationFormat total_time,
             const size_t step_idx)
    {
        for_each_in_tuple(loggers_, [&](auto& logger) {
            logger.log(chain_state, total_time, step_idx);
        });
    }

    void start()
    {
        for_each_in_tuple(loggers_, [](auto& logger) { logger.start(); });
    }

    void stop(const bool time_limit_reached = false)
    {
        for_each_in_tuple(loggers_, [](auto& logger) { logger.stop(); });
    }

    template <size_t LoggerIdx>
    auto& get()
    {
        return std::get<LoggerIdx>(loggers_);
    }

private:
    std::tuple<Loggers<ChainState, DurationFormat>...> loggers_;
};

}  // namespace samply

#endif