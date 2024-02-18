// Copyright (c) 2021 ETH Zurich, Mattia Gollub (mattia.gollub@bsse.ethz.ch)
// Computational Systems Biology group, D-BSSE
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef PTA_UNIFORM_FLUX_SAMPLING_SETTINGS_H
#define PTA_UNIFORM_FLUX_SAMPLING_SETTINGS_H

#include <settings.h>

namespace pta {

struct UniformFluxSamplingSettings : public samply::Settings {
    UniformFluxSamplingSettings() = default;
    UniformFluxSamplingSettings(const UniformFluxSamplingSettings&) = default;

    UniformFluxSamplingSettings(const samply::Settings base_settings)
        : samply::Settings(base_settings)
    {}
};

} // namespace pta

#endif