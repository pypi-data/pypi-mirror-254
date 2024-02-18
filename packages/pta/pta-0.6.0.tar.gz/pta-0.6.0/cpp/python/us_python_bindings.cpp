// Copyright (c) 2021 ETH Zurich, Mattia Gollub (mattia.gollub@bsse.ethz.ch)
// Computational Systems Biology group, D-BSSE
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#include <chord_samplers/uniform_pdf_sampler.h>
#include <descriptors/polytope.h>
#include <hit_and_run_sampler.h>
#include <loggers/console_progress_logger.h>
#include <loggers/eigen_state_logger.h>
#include <loggers/multi_logger.h>
#include <pybind11/eigen.h>
#include <pybind11/iostream.h>
#include <pybind11/pybind11.h>
#include <thread>

#include "direction_samplers/coordinate_direction_sampler.h"
#include "python_helper.h"
#include "settings/uniform_flux_sampling_settings.h"
#include "utilities.h"

using namespace pta;
using namespace samply;

namespace py = pybind11;

typedef double Scalar;

template <typename ChainState, typename DurationFormat>
using UniformLoggers =
    MultiLogger<ChainState, DurationFormat, EigenStateLogger, ConsoleProgressLogger>;
using Sampler = HitAndRunSampler<
    Scalar,
    CoordinateDirectionSampler,
    Polytope,
    UniformPdfSampler,
    UniformLoggers>;

py::array_t<double> sample_flux_space_uniform(
    const py::EigenDRef<Eigen::MatrixXd> G,
    const py::EigenDRef<Eigen::MatrixXd> h,
    const py::EigenDRef<Eigen::MatrixXd> from_Fd_T,
    const py::EigenDRef<Eigen::MatrixXd> initial_state,
    const UniformFluxSamplingSettings& settings)
{
    // Redirect stdout to the Python output.
    py::scoped_ostream_redirect stream(
        std::cout, py::module_::import("sys").attr("stdout"));

    // Distribute the chains among the available threads.
    const size_t max_threads = std::min(
        settings.max_threads, static_cast<size_t>(std::thread::hardware_concurrency()));
    auto chains_per_thread =
        utils::get_chains_per_thread(initial_state.cols(), max_threads);

    // Initialize the components of the sampler.
    AffineTransform<double> from_Fd(from_Fd_T, Vector<double>::Zero(G.cols()));
    CoordinateDirectionSampler<Scalar> proposal(from_Fd);
    Polytope<Scalar> descriptor(G, h);
    UniformPdfSampler<Scalar> chord_sampler(G.cols());

    // Initialize the state storage.
    const size_t preallocated_states = utils::estimate_num_states(settings);
    EigenStateStorage<double> states_storage{
        chains_per_thread, initial_state.rows(), initial_state.cols(),
        preallocated_states};

    // Create and initialize a sampler for each thread.
    std::vector<Sampler> samplers;
    samplers.reserve(chains_per_thread.size());
    size_t state_idx = 0u;
    for (size_t thread_idx = 0; thread_idx < chains_per_thread.size(); ++thread_idx) {
        // Create the loggers, binding the state logger to the common storage.
        Sampler::LoggerType loggers{
            {states_storage, thread_idx, settings.steps_thinning,
             settings.num_skipped_steps},
            {settings.worker_id, settings.console_logging_interval_ms}};

        // Create the sampler object.
        samplers.emplace_back(proposal, descriptor, chord_sampler, loggers);
        samplers[thread_idx].set_state(initial_state.block(
            0u, state_idx, initial_state.rows(), chains_per_thread[thread_idx]));
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
    return python_helper::vector_of_eigen_matrices_to_numpy_3d_array(
        states_storage.get_states());
}

void add_us_python_bindings(py::module& m)
{
    py::class_<UniformFluxSamplingSettings, Settings>(m, "UniformSamplerSettings")
        .def(py::init<>());

    m.def("sample_flux_space_uniform", &sample_flux_space_uniform);
}