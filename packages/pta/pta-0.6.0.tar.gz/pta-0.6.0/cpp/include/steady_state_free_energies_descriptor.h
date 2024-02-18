// Copyright (c) 2021 ETH Zurich, Mattia Gollub (mattia.gollub@bsse.ethz.ch)
// Computational Systems Biology group, D-BSSE
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef PTA_STEADY_STATE_FREE_ENERGIES_DESCRIPTOR_H
#define PTA_STEADY_STATE_FREE_ENERGIES_DESCRIPTOR_H

#include <descriptors/ellipsoid.h>
#include <descriptors/polytope.h>
#include <intersections_packet.h>
#include <rays_packet.h>
#include <reparametrized_object.h>

#include <Eigen/Dense>
#include <exception>
#include <utility>

#include "flux_constraints.h"
#include "settings/free_energy_sampling_settings.h"
#include "steady_state_verifier.h"
#include "thermodynamic_space.h"
#include "utilities.h"

namespace pta {

template <typename ScalarType> class SteadyStateFreeEnergiesDescriptor {
  public:
    typedef ScalarType Scalar;

    SteadyStateFreeEnergiesDescriptor(
        const FluxConstraints& flux_constraints,
        const ThermodynamicSpace& thermodynamic_space,
        const FreeEnergySamplingSettings& settings);

    SteadyStateFreeEnergiesDescriptor(
        const SteadyStateFreeEnergiesDescriptor<Scalar>& other);

    void initialize(const samply::Matrix<Scalar>& state);

    /**
     * @brief Find the intersections between the given rays and the ellipsoid.
     */
    void intersect(
        samply::IntersectionsPacket<Scalar>& output_intersections,
        const samply::RaysPacket<Scalar>& rays);

    void update_position(const samply::Vector<Scalar>& t);

    samply::ReparametrizedObject<SteadyStateFreeEnergiesDescriptor<Scalar>>
    get_optimally_reparametrized_descriptor() const;

    Eigen::Index dimensionality() const;

    const samply::Matrix<Scalar>
    evaluate_last_drg_rays_at(const samply::Vector<Scalar>& t) const;

  private:
    samply::AffineTransform<Scalar> make_thermo_vars_to_drg_rev_(
        const FluxConstraints& flux_constraints,
        const ThermodynamicSpace& thermodynamic_space);

    samply::Polytope<Scalar> thermo_vars_constraints_;
    samply::Ellipsoid<Scalar> thermo_vars_confidence_;

    const FluxConstraints flux_constraints_;
    const ThermodynamicSpace thermodynamic_space_;
    const FreeEnergySamplingSettings settings_;

    const samply::AffineTransform<Scalar> thermo_vars_to_drg_rev_;
    SteadyStateVerifier<Scalar> verifier_;
    samply::RaysPacket<Scalar> last_rev_drg_rays_;

    // Persistent temporary variables, to avoid reallocation at each call.
    samply::IntersectionsPacket<Scalar> intersections_polytope_;
    samply::IntersectionsPacket<Scalar> intersections_ellipsoid_;
    samply::IntersectionsPacket<Scalar> intersections_;
    samply::Matrix<Scalar> t_equienergy_;
    samply::RaysPacket<ScalarType> rev_drg_rays_;
    samply::Vector<Scalar> region_starts_;
    samply::Vector<Scalar> region_ends_;
    Eigen::VectorXi ray_indices_;
    std::vector<Scalar> ts_;
    std::vector<size_t> steady_state_orthants_ids_;
};

//==============================================================================
//	SteadyStateFreeEnergiesDescriptor public methods implementation.
//==============================================================================

template <typename ScalarType>
SteadyStateFreeEnergiesDescriptor<ScalarType>::SteadyStateFreeEnergiesDescriptor(
    const FluxConstraints& flux_constraints,
    const ThermodynamicSpace& thermodynamic_space,
    const FreeEnergySamplingSettings& settings)
    : thermo_vars_constraints_(thermodynamic_space.G, thermodynamic_space.h)
    , thermo_vars_confidence_(
          thermodynamic_space.G.cols(), thermodynamic_space.confidence_radius)
    , flux_constraints_(flux_constraints)
    , thermodynamic_space_(thermodynamic_space)
    , settings_(settings)
    , thermo_vars_to_drg_rev_(
          make_thermo_vars_to_drg_rev_(flux_constraints, thermodynamic_space))
    , verifier_(
          flux_constraints,
          thermodynamic_space.constrained_reactions_ids,
          settings.flux_epsilon,
          settings.feasibility_cache_size)
{}

template <typename ScalarType>
SteadyStateFreeEnergiesDescriptor<ScalarType>::SteadyStateFreeEnergiesDescriptor(
    const SteadyStateFreeEnergiesDescriptor<ScalarType>& other)
    : SteadyStateFreeEnergiesDescriptor(
          other.flux_constraints_, other.thermodynamic_space_, other.settings_)
{}

template <typename ScalarType>
void SteadyStateFreeEnergiesDescriptor<ScalarType>::intersect(
    samply::IntersectionsPacket<Scalar>& output_intersections,
    const samply::RaysPacket<ScalarType>& rays)
{
    thermo_vars_constraints_.intersect(intersections_polytope_, rays);
    thermo_vars_confidence_.intersect(intersections_ellipsoid_, rays);
    intersections_polytope_.intersect(intersections_, intersections_ellipsoid_);

    thermo_vars_to_drg_rev_.transform(rev_drg_rays_, rays);
    t_equienergy_ = -rev_drg_rays_.origins.cwiseQuotient(rev_drg_rays_.directions);

    Eigen::Index num_rays = rays.origins.cols();
    Eigen::Index num_regions = 0;
    region_starts_.resize(num_rays * (dimensionality() + 1));
    region_ends_.resize(num_rays * (dimensionality() + 1));
    ray_indices_.resize(num_rays * (dimensionality() + 1));

    for (Eigen::Index ray_idx = 0; ray_idx < num_rays; ray_idx++) {
        ts_.resize(t_equienergy_.rows() + 2);
        const Scalar min_t = intersections_.segment_starts(ray_idx);
        const Scalar max_t = intersections_.segment_ends(ray_idx);
        const Scalar min_region_span =
            (max_t - min_t) * settings_.min_rel_region_length;
        ts_[0] = min_t;
        ts_[1] = max_t;

        // Collect intersections laying on the intersection segment.
        auto ray_t_equienergy = t_equienergy_.col(ray_idx);
        auto ts_end = std::copy_if(
            ray_t_equienergy.begin(), ray_t_equienergy.end(), ts_.begin() + 2,
            [&](const Scalar t) { return min_t <= t && t <= max_t; });

        // Sort and remove duplicates or regions that have negligible size.
        std::sort(ts_.begin(), ts_end);

        ts_end = utils::remove_if_precedent(
            ts_.begin(), ts_end, [&](const Scalar t_predecessor, const Scalar t) {
                return (t - t_predecessor) < min_region_span;
            });
        ts_.resize(std::distance(ts_.begin(), ts_end));

        // Store the bounds of the regions for later processing.
        region_starts_.segment(num_regions, ts_.size() - 1) =
            Eigen::Map<samply::Vector<ScalarType>>(ts_.data(), ts_.size() - 1);
        region_ends_.segment(num_regions, ts_.size() - 1) =
            Eigen::Map<samply::Vector<ScalarType>>(ts_.data() + 1, ts_.size() - 1);
        ray_indices_.segment(num_regions, ts_.size() - 1).array() =
            static_cast<int>(ray_idx);
        num_regions += (ts_.size() - 1);
    }

    verifier_.get_steady_state_regions_ids(
        steady_state_orthants_ids_, rev_drg_rays_, region_starts_.head(num_regions),
        region_ends_.head(num_regions), ray_indices_.head(num_regions));
    const size_t num_segments = steady_state_orthants_ids_.size();

    // Manual copy is faster than Eigen's indexing as it avoids allocation of
    // temporaries.
    output_intersections.segment_starts.resize(num_segments);
    output_intersections.segment_ends.resize(num_segments);
    output_intersections.ray_indices.resize(num_segments);
    size_t j = 0;
    for (auto i : steady_state_orthants_ids_) {
        output_intersections.segment_starts(j) = region_starts_(i);
        output_intersections.segment_ends(j) = region_ends_(i);
        output_intersections.ray_indices(j) = ray_indices_(i);
        j++;
    }
    output_intersections.num_rays = num_rays;
    output_intersections.one_ray_one_intersection = false;

    last_rev_drg_rays_ = rev_drg_rays_;
}

template <typename ScalarType>
void SteadyStateFreeEnergiesDescriptor<ScalarType>::initialize(
    const samply::Matrix<Scalar>& state)
{
    thermo_vars_constraints_.initialize(state);
}

template <typename ScalarType>
void SteadyStateFreeEnergiesDescriptor<ScalarType>::update_position(
    const samply::Vector<Scalar>& t)
{
    thermo_vars_constraints_.update_position(t);
}

template <typename ScalarType>
samply::ReparametrizedObject<SteadyStateFreeEnergiesDescriptor<ScalarType>>
SteadyStateFreeEnergiesDescriptor<ScalarType>::get_optimally_reparametrized_descriptor()
    const
{
    return samply::ReparametrizedObject<SteadyStateFreeEnergiesDescriptor<ScalarType>>{
        SteadyStateFreeEnergiesDescriptor<ScalarType>{
            flux_constraints_, thermodynamic_space_, settings_},
        samply::AffineTransform<ScalarType>::identity(dimensionality()),
        samply::AffineTransform<ScalarType>::identity(dimensionality())};
}

template <typename ScalarType>
Eigen::Index SteadyStateFreeEnergiesDescriptor<ScalarType>::dimensionality() const
{
    return thermo_vars_to_drg_rev_.get_linear().cols();
}

//==============================================================================
//	SteadyStateFreeEnergiesDescriptor private methods implementation.
//==============================================================================

template <typename ScalarType>
inline samply::AffineTransform<ScalarType>
SteadyStateFreeEnergiesDescriptor<ScalarType>::make_thermo_vars_to_drg_rev_(
    const FluxConstraints& flux_constraints,
    const ThermodynamicSpace& thermodynamic_space)
{
    // Find the indices (in the thermodynamic space) of the reversible reactions with
    // thermodynamic constraints.
    std::vector<Eigen::Index> rev_constrained_rxns_idxs;
    for (Eigen::Index i = 0; i < thermodynamic_space.constrained_reactions_ids.size();
         i++) {
        const Eigen::Index reaction_idx =
            thermodynamic_space.constrained_reactions_ids(i);
        if (flux_constraints.lower_bounds[reaction_idx] < 0 &&
            flux_constraints.upper_bounds[reaction_idx] > 0) {
            rev_constrained_rxns_idxs.push_back(i);
        }
    }

    return {
        thermodynamic_space.basis_to_drg.get_linear()(
            rev_constrained_rxns_idxs, Eigen::all),
        thermodynamic_space.basis_to_drg.get_shift()(rev_constrained_rxns_idxs)};
}

template <typename ScalarType>
inline const samply::Matrix<ScalarType>
SteadyStateFreeEnergiesDescriptor<ScalarType>::evaluate_last_drg_rays_at(
    const samply::Vector<ScalarType>& t) const
{
    return last_rev_drg_rays_.at(t);
}

} // namespace pta

#endif
