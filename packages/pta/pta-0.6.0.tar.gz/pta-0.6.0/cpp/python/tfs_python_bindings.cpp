// Copyright (c) 2021 ETH Zurich, Mattia Gollub (mattia.gollub@bsse.ethz.ch)
// Computational Systems Biology group, D-BSSE
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#include <chord_samplers/mvn_pdf_sampler.h>
#include <hit_and_run_sampler.h>
#include <loggers/eigen_state_logger.h>
#include <loggers/multi_logger.h>
#include <pybind11/eigen.h>
#include <pybind11/iostream.h>
#include <pybind11/pybind11.h>
#include <thread>

#include "commons.h"
#include "direction_samplers/ellipsoid_direction_sampler.h"
#include "loggers/orthants_logger.h"
#include "python_helper.h"
#include "settings/free_energy_sampling_settings.h"
#include "steady_state_free_energies_descriptor.h"
#include "utilities.h"
#include <thread>

using namespace pta;
using namespace samply;

namespace py = pybind11;

typedef double Scalar;

template <typename ChainState, typename DurationFormat>
using Loggers =
    MultiLogger<ChainState, DurationFormat, EigenStateLogger, OrthantsLogger>;
using Sampler = HitAndRunSampler<
    Scalar,
    EllipsoidDirectionSampler,
    SteadyStateFreeEnergiesDescriptor,
    MvnPdfSampler,
    Loggers>;

struct TFSResult {
    py::array_t<double> chains;
    py::array_t<uint8_t> directions;
    py::array_t<uint32_t> direction_counts;
};

TFSResult sample_free_energies(
    const py::EigenDRef<Eigen::MatrixXd> flux_S,
    const py::EigenDRef<Eigen::MatrixXd> flux_lb,
    const py::EigenDRef<Eigen::MatrixXd> flux_ub,
    const py::EigenDRef<Eigen::Matrix<uint32_t, -1, 1>> constrained_rxns_ids,
    const py::EigenDRef<Eigen::MatrixXd> initial_state,
    const FreeEnergySamplingSettings& settings,
    const py::EigenDRef<Eigen::MatrixXd> thermo_G,
    const py::EigenDRef<Eigen::MatrixXd> thermo_h,
    const py::EigenDRef<Eigen::MatrixXd> basis_to_drg_T,
    const py::EigenDRef<Eigen::MatrixXd> basis_to_drg_shift,
    const py::EigenDRef<Eigen::MatrixXd> directions_transform_T)
{
    // Redirect stdout to the Python output.
    py::scoped_ostream_redirect stream(
        std::cout, py::module_::import("sys").attr("stdout"));

    // Distribute the chains among the available threads.
    const size_t max_threads = std::min(
        settings.max_threads, static_cast<size_t>(std::thread::hardware_concurrency()));
    auto chains_per_thread =
        utils::get_chains_per_thread(initial_state.cols(), max_threads);

    AffineTransform<double> basis_to_drg(basis_to_drg_T, basis_to_drg_shift);
    AffineTransform<double> directions_transform(
        directions_transform_T, Vector<double>::Zero(directions_transform_T.rows()));

    // Create the directions distribution for Hit-and-Run.
    EllipsoidDirectionSampler<Scalar> proposal{directions_transform};

    // Create the descriptor for the space of steady state free energies.
    FluxConstraints flux_constraints{flux_S, flux_lb, flux_ub};
    ThermodynamicSpace thermodynamic_space{
        thermo_G, thermo_h, basis_to_drg, constrained_rxns_ids.cast<Eigen::Index>(),
        settings.truncation_multiplier};
    SteadyStateFreeEnergiesDescriptor<Scalar> descriptor{
        flux_constraints, thermodynamic_space, settings};

    // Create PDF of the free energies.
    MvnPdfSampler<Scalar> chord_sampler{AffineTransform<double>::identity(
        static_cast<Index>(descriptor.dimensionality()))};

    // Initialize the state and orthant storages.
    const size_t preallocated_states = utils::estimate_num_states(settings);
    EigenStateStorage<double> states_storage{
        chains_per_thread, initial_state.rows(), initial_state.cols(),
        preallocated_states};
    OrthantsStorage<double> orthants_storage{chains_per_thread.size()};

    // Create and initialize a sampler for each thread.
    std::vector<Sampler> samplers;
    samplers.reserve(chains_per_thread.size());
    size_t state_idx = 0u;
    for (size_t thread_idx = 0; thread_idx < chains_per_thread.size(); ++thread_idx) {
        // Create the loggers, binding the state and orthant loggers to the common
        // storage.
        Sampler::LoggerType loggers{
            {states_storage, thread_idx, settings.steps_thinning,
             settings.num_skipped_steps},
            {orthants_storage, thread_idx, settings.steps_thinning_directions,
             settings.num_skipped_steps}};

        // Create the sampler object.
        samplers.emplace_back(proposal, descriptor, chord_sampler, loggers);
        samplers[thread_idx].get_logger().get<1>().set_descriptor(
            samplers[thread_idx].get_space_descriptor());
        samplers[thread_idx].get_logger().get<1>().set_sampler(
            samplers[thread_idx].get_chord_sampler());
        samplers[thread_idx].set_state(initial_state.block(
            0u, state_idx, initial_state.rows(), chains_per_thread[thread_idx]));
        state_idx += chains_per_thread[thread_idx];
    }

    {
        // Release the GIL so that any thread can print to the python console.
        py::gil_scoped_release gil_release;

        // Next start the simulations.
        std::vector<std::thread> threads;
        threads.reserve(chains_per_thread.size());
        for (auto& sampler : samplers) {
            threads.emplace_back(
                &Sampler::simulate<Sampler::DurationFormat>, &sampler,
                settings.num_steps, Sampler::DurationFormat::max());
        }

        // Wait for the simulations to complete.
        for (std::thread& t : threads) {
            if (t.joinable())
                t.join();
        }
    }

    // Copy back resulting samples.
    TFSResult result;
    result.chains = python_helper::vector_of_eigen_matrices_to_numpy_3d_array(
        states_storage.get_states());
    std::tie(result.directions, result.direction_counts) =
        python_helper::direction_counts_to_python(
            orthants_storage.get_aggregated_orthants_map());
    return result;
}

void add_tfs_python_bindings(py::module& m)
{
    py::class_<FreeEnergySamplingSettings, Settings>(m, "FreeEnergySamplerSettings")
        .def(py::init<>())
        .def_readwrite(
            "truncation_multiplier", &FreeEnergySamplingSettings::truncation_multiplier)
        .def_readwrite(
            "feasibility_cache_size",
            &FreeEnergySamplingSettings::feasibility_cache_size)
        .def_readwrite("drg_epsilon", &FreeEnergySamplingSettings::drg_epsilon)
        .def_readwrite("flux_epsilon", &FreeEnergySamplingSettings::flux_epsilon)
        .def_readwrite(
            "min_rel_region_length", &FreeEnergySamplingSettings::min_rel_region_length)
        .def_readwrite(
            "steps_thinning_directions",
            &FreeEnergySamplingSettings::steps_thinning_directions);

    py::class_<TFSResult>(m, "TFSResult")
        .def(py::init<>())
        .def_readwrite("chains", &TFSResult::chains)
        .def_readwrite("directions", &TFSResult::directions)
        .def_readwrite("direction_counts", &TFSResult::direction_counts);

    m.def("sample_free_energies", &sample_free_energies);
}