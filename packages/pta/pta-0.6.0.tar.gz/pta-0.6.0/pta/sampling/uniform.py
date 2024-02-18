"""Uniform sampling of the flux space of a metabolic network."""

import logging
from typing import Union

import _pta_python_binaries as pb
import cobra
import numpy as np
import pandas as pd
from PolyRound.api import StoichiometryParser
from pta.sampling.primitives import FluxSpaceSamplingModel

from ..constants import (
    default_flux_bound,
    default_max_psrf,
    default_max_threads,
    default_num_samples,
)
from .commons import (
    SamplingResult,
    apply_to_chains,
    fill_common_sampling_settings,
    sample_from_chains,
    split_R,
)
from .convergence_manager import ConvergenceManager

logger = logging.getLogger(__name__)


class UniformSamplingModel(FluxSpaceSamplingModel):
    """Object holding the information necessary to run uniform sampling on a flux space.

    Parameters
    ----------
    polytope : Polytope
        Polytope object describing the flux space.
    reaction_ids : List[str]
        Identifiers of the reactions in the flux space.
    """

    @classmethod
    def from_cobrapy_model(
        cls, model: cobra.Model, infinity_flux_bound: float = default_flux_bound
    ) -> "UniformSamplingModel":
        """Builds a uniform sampler model from a cobrapy model.

        Parameters
        ----------
        model : cobra.Model
            The input cobra model.
        infinity_flux_bound : float, optional
            Default bound to use for unbounded fluxes.

        Returns
        -------
        UniformSamplingModel
            The constructed model.
        """
        polytope = StoichiometryParser.extract_polytope(model, infinity_flux_bound)
        return cls(polytope, [r.id for r in model.reactions])

    def simulate(
        self,
        settings: pb.SamplerSettings,
        initial_points: np.ndarray,
        directions_transform: np.ndarray,
    ) -> np.ndarray:
        """Run the sampler with the given parameters.

        Parameters
        ----------
        settings : pb.SamplerSettings
            Sampling settings.
        initial_points : np.ndarray
            The initial points for the chains.
        directions_transform : np.ndarray
            The transform for the directions sampler.
        """

        chains = pb.sample_flux_space_uniform(
            self.G,
            self.h,
            directions_transform,
            initial_points,
            settings,
        )
        return chains

    def compute_psrf(self, result: np.ndarray) -> pd.Series:
        """Compute the potential scale reduction factors for the variables of interest
        on a given set of chains.

        Parameters
        ----------
        result : np.ndarray
            The result of the sampling function.

        Returns
        -------
        pd.Series
            The computed potential scale reduction factors.
        """
        logger.debug("Computing PSRFs.")
        psrf_var_names = [
            "var" + str(i) for i in range(self.dimensionality)
        ] + self.reaction_ids
        psrf = np.hstack(
            [split_R(result), split_R(apply_to_chains(result, self.to_fluxes))]
        )
        return pd.Series(psrf, index=psrf_var_names)

    def get_chains(self, result: np.ndarray) -> np.ndarray:
        """Extract the simulated chains from a given result.

        Parameters
        ----------
        result : np.ndarray
            The result of the native sampling function.

        Returns
        -------
        np.ndarray
            The simulated chains.
        """

        return result


def sample_flux_space_uniform(
    model: Union[cobra.Model, "UniformSamplingModel"],
    num_samples: int = default_num_samples,
    max_steps: int = -1,
    max_psrf: float = default_max_psrf,
    num_chains: int = -1,
    initial_points: np.array = None,
    num_initial_steps: int = -1,
    max_threads: int = default_max_threads,
    convergence_manager: ConvergenceManager = None,
) -> SamplingResult:
    """Sample steady state fluxes in the given model. The sampler run until either
    max_steps or max_psrf is reached.

    Parameters
    ----------
    model : Union[cobra.Model, UniformSamplingModel]
        The model to sample.
    num_samples : int, optional
        Number of samples to draw.
    max_steps : int, optional
        The maximum number fo steps to simulate.
    max_psrf : float, optional
        Maximum value of the PSRFs for convergence.
    num_chains : int, optional
        The number of chains to simulate.
    initial_points : np.array, optional
        The initial points for the chains.
    num_initial_steps: int, optional
        Initial chains length.
    max_threads : int, optional
        The maximum number of parallel threads to use.
    convergence_manager : ConvergenceManager, optional
        The object to use to monitor and improve convergence.

    Returns
    -------
    SamplingResult
        The sampling result.

    Raises
    ------
    SamplingException
        If sampling fails.
    """
    # Validate and process input settings.
    if isinstance(model, cobra.Model):
        model = UniformSamplingModel.from_cobrapy_model(model)
    assert num_samples > 0
    max_steps = max_steps if max_steps >= 1 else 2**63
    assert max_psrf > 1.0
    if initial_points is not None and num_chains < 0:
        num_chains = initial_points.shape[1]
    num_initial_steps = (
        num_initial_steps
        if num_initial_steps > 0
        else model.dimensionality**2 + num_samples
    )
    assert max_threads > 0
    convergence_manager = ConvergenceManager(model, num_initial_steps, False)

    # Construct auxiliary functions.
    settings = pb.UniformSamplerSettings()
    update_settings_function = lambda s, steps: fill_common_sampling_settings(
        s, num_samples, steps, num_chains, 2, max_threads
    )
    update_settings_function(settings, num_initial_steps)
    make_sampling_result_function = lambda r: _make_sampling_result(
        model, r, num_samples
    )

    # Generate the initial points if needed.
    if initial_points is None:
        initial_points = model.get_initial_points(settings.num_chains)

    # Run the sampler.
    result = convergence_manager.run(
        settings,
        update_settings_function,
        make_sampling_result_function,
        initial_points,
        max_steps,
        max_psrf,
    )
    return result


def _make_sampling_result(
    model: "UniformSamplingModel", result: np.ndarray, num_samples: int
) -> SamplingResult:
    basis_var_names = ["var" + str(i) for i in range(model.dimensionality)]
    basis_samples = sample_from_chains(result, num_samples)
    samples = model.to_fluxes(basis_samples.T).T

    return SamplingResult(
        pd.DataFrame(samples, columns=model.reaction_ids),
        model.compute_psrf(result),
        pd.DataFrame(basis_samples, columns=basis_var_names),
        result,
    )
