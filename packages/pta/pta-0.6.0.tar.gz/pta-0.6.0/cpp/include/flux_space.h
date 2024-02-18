// Copyright (c) 2018-2022 ETH Zurich, Mattia Gollub (mattia.gollub@bsse.ethz.ch)
// Computational Systems Biology group, D-BSSE
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef PTA_FLUX_SPACE_H
#define PTA_FLUX_SPACE_H

#include <commons.h>
#include <transforms/affine_transform.h>

namespace pta {

struct FluxSpace {
    samply::Vector<double> lower_bounds;
    samply::Vector<double> upper_bounds;
    samply::Matrix<double> G;
    samply::Vector<double> h;
    samply::AffineTransform<double> basis_to_fluxes;
};

} // namespace pta

#endif
