// Copyright (c) 2021 ETH Zurich, Mattia Gollub (mattia.gollub@bsse.ethz.ch)
// Computational Systems Biology group, D-BSSE
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef PTA_THERMODYNAMIC_SPACE_H
#define PTA_THERMODYNAMIC_SPACE_H

#include <commons.h>
#include <transforms/affine_transform.h>

namespace pta {

struct ThermodynamicSpace {
    samply::Matrix<double> G;
    samply::Vector<double> h;
    samply::AffineTransform<double> basis_to_drg;
    Eigen::Matrix<Eigen::Index, -1, 1> constrained_reactions_ids;
    double confidence_radius;
};

} // namespace pta

#endif
