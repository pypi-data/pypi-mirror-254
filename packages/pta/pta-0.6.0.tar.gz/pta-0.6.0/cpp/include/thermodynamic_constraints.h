// Copyright (c) 2021 ETH Zurich, Mattia Gollub (mattia.gollub@bsse.ethz.ch)
// Computational Systems Biology group, D-BSSE
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef PTA_THERMODYNAMIC_CONSTRAINTS_H
#define PTA_THERMODYNAMIC_CONSTRAINTS_H

#include <transforms/transforms.h>

#include <Eigen/Dense>

namespace pta {

struct ThermodynamicConstraints {
    Eigen::Matrix<Eigen::Index, -1, 1> constrained_reactions_ids;
    samply::AffineTransform<double> vars_to_constrained_drg;
};

} // namespace pta

#endif