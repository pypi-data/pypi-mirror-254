// Copyright (c) 2021 ETH Zurich, Mattia Gollub (mattia.gollub@bsse.ethz.ch)
// Computational Systems Biology group, D-BSSE
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef PTA_FLUX_CONSTRAINTS_H
#define PTA_FLUX_CONSTRAINTS_H

#include <Eigen/Dense>

namespace pta {

struct FluxConstraints {
    Eigen::MatrixXd S;
    Eigen::VectorXd lower_bounds;
    Eigen::VectorXd upper_bounds;
};

} // namespace pta

#endif