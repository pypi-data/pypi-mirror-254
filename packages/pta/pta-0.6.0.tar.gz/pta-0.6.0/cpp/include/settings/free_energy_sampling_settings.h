// Copyright (c) 2021 ETH Zurich, Mattia Gollub (mattia.gollub@bsse.ethz.ch)
// Computational Systems Biology group, D-BSSE
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef PTA_FREE_ENERGY_SAMPLING_SETTINGS_H
#define PTA_FREE_ENERGY_SAMPLING_SETTINGS_H

#include <settings.h>

namespace pta {

struct FreeEnergySamplingSettings : public samply::Settings {
    FreeEnergySamplingSettings() = default;
    FreeEnergySamplingSettings(const FreeEnergySamplingSettings&) = default;

    FreeEnergySamplingSettings(const samply::Settings base_settings)
        : samply::Settings(base_settings)
    {}

    // Numerics and performance settings.
    double truncation_multiplier = 1.0;
    size_t feasibility_cache_size = 10'000;

    // Flux and free energy space definition.
    double drg_epsilon = 1e-3;
    double flux_epsilon = 1e-4;
    double min_rel_region_length = 1e-6;

    size_t steps_thinning_directions;
};

} // namespace pta

#endif