"""Common classes and methods for sampling algorithms."""

import abc
import datetime
import math
from typing import Any, Callable

import _pta_python_binaries as pb
import numpy as np
import pandas as pd
import psutil

from ..constants import (
    default_max_psrf,
    default_max_threads,
    default_min_chains,
    min_samples_per_chain,
)


class SamplingException(Exception):
    """Raised when an exception occurs during sampling."""


class SamplingResult:
    """Encapsulates the result of a sampler.

    Parameters
    ----------
    samples : pd.DataFrame
        Data frame containing the samples as rows.
    psrf : pd.Series
        Series containing the PSRF of each variable.
    basis_samples : pd.DataFrame, optional
        The samples in the basis.
    chains : np.ndarray, optional
        The simulated chains.
    """

    def __init__(
        self,
        samples: pd.DataFrame,
        psrf: pd.Series,
        basis_samples: pd.DataFrame = None,
        chains: np.ndarray = None,
    ):
        self._samples = samples
        self._psrf = psrf
        self._basis_samples = basis_samples
        self._chains = chains

    @property
    def basis_samples(self) -> pd.DataFrame:
        """Gets a data frame containing the samples in the basis."""
        return self._basis_samples

    @property
    def samples(self) -> pd.DataFrame:
        """Gets a data frame containing the samples."""
        return self._samples

    @property
    def chains(self) -> np.ndarray:
        """Get the simulated chains."""
        return self._chains

    @property
    def psrf(self) -> pd.Series:
        """Gets the Potential Scale Reduction Factor (PSRF) of each variable."""
        return self._psrf

    def check_convergence(self, max_psrf: float = default_max_psrf) -> bool:
        """Checks whether the chains converged according to the given criteria.

        Parameters
        ----------
        max_psrf : float, optional
            Maximum PSRF value for convergence.

        Returns
        -------
        bool
            True if the test succeeded, false otherwise.
        """
        return np.all(self.psrf <= max_psrf)


class SamplerInterface(metaclass=abc.ABCMeta):
    """Interface for an MCMC sampler."""

    @property
    @abc.abstractmethod
    def dimensionality(self) -> int:
        """Get the dimensionality of the sampling space."""

    @abc.abstractmethod
    def simulate(
        self,
        settings: pb.SamplerSettings,
        initial_points: np.ndarray,
        directions_transform: np.ndarray,
    ) -> Any:
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

    @abc.abstractmethod
    def compute_psrf(self, result: Any) -> pd.Series:
        """Compute the potential scale reduction factors for the variables of interest
        on a given set of chains.

        Parameters
        ----------
        result : Any
            The result of the sampling function.

        Returns
        -------
        pd.Series
            The computed potential scale reduction factors.
        """

    @abc.abstractmethod
    def get_chains(self, result: Any) -> np.ndarray:
        """Extract the simulated chains from a given result.

        Parameters
        ----------
        result : Any
            The result of the native sampling function.

        Returns
        -------
        np.ndarray
            The simulated chains.
        """


def sample_from_chains(chains: np.ndarray, num_samples: int) -> np.ndarray:
    """Draws samples from a given set of chains.

    Parameters
    ----------
    chains : np.ndarray
        Numpy 3D array containing the chains.
    num_samples : int
        Number of samples to draw.

    Returns
    -------
    np.ndarray
        Array of samples.
    """
    samples = np.hstack(chains)
    indices = np.random.choice(samples.shape[1], num_samples, False)
    return samples[:, indices].T


def split_chains(chains: np.ndarray) -> np.ndarray:
    """Split the chains in two, threating each half as a new chain. This is often used
    to detect systematic trends in a random walk.

    Parameters
    ----------
    chains : np.ndarray
        Numpy 3D array containing the input chains.

    Returns
    -------
    np.ndarray
        Numpy 3D array containing the resulting chains.
    """
    half_chain_idx = math.floor(chains.shape[0] / 2)
    return np.dstack(
        [
            chains[:half_chain_idx, :, :],
            chains[half_chain_idx : 2 * half_chain_idx, :, :],
        ]
    )


def apply_to_chains(
    chains: np.ndarray, f: Callable[[np.ndarray], np.ndarray]
) -> np.ndarray:
    """Apply a function to each sample of a group of chains.

    Parameters
    ----------
    chains : np.ndarray
        Numpy 3D array containing the input chains.
    f : Callable[[np.ndarray], np.ndarray]
        Function to apply to each sample.

    Returns
    -------
    np.ndarray
        Numpy 3D array containing the transformed samples.
    """
    n_chains = chains.shape[2]
    transformed_chains = []
    for i in range(n_chains):
        transformed_chains.append(f(chains[:, :, i].T).T)
    return np.dstack(transformed_chains)


def split_R(chains: np.ndarray) -> np.ndarray:
    """Compute the split-R  (or Potential Scale Reduction Factor) of each variable in
    the given chains.

    Parameters
    ----------
    chains : np.ndarray
        Numpy 3D array containing the input chains.

    Returns
    -------
    np.ndarray
        Vector containing the split-R value for each variable.
    """
    EPSILON = 1e8
    chains = split_chains(chains)
    n_steps, n_params, n_chains = chains.shape
    R = np.empty(n_params)

    # Iterate over parameters.
    for i in range(n_params):
        chain_means = np.mean(chains[:, i, :], axis=0, keepdims=True)
        sample_mean = np.mean(chain_means)
        sample_variance = (
            1 / (n_steps) * np.sum((chains[:, i, :] - chain_means) ** 2, axis=0)
        )

        # Compute between-chains variance.
        B = n_steps / (n_chains - 1) * np.sum((chain_means - sample_mean) ** 2)

        # Compute within-chain variance.
        W = 1 / n_chains * np.sum(sample_variance)

        if (
            np.all(np.abs(sample_variance / np.abs(chain_means) + EPSILON) < EPSILON)
            and np.abs(B / np.abs(sample_mean) + EPSILON) < EPSILON
        ):
            # If the variance-to-mean ratios within each chain and between all chains
            # are very low, we can assume that the variable is practically constant. Set
            # R to one in order to avoid numerical artifacts.
            R[i] = 1
        else:
            # Compute pooled variance.
            V = (n_steps - 1) / n_steps * W + 1 / n_steps * B

            # Compute potential scale reduction factor estimate.
            R[i] = np.sqrt(V / W)

    return R


def fill_common_sampling_settings(
    settings: pb.SamplerSettings,
    num_samples: int,
    num_steps: int,
    num_chains: int = -1,
    num_warmup_steps: int = -1,
    max_threads: int = default_max_threads,
):
    """Fills default values for common sampling settings.

    Parameters
    ----------
    settings : SamplerSettings
        The settings object to be filled.
    log_directory : str
        Directory in which the sampling logs should be stored.
    num_samples : int
        Number of samples to draw.
    num_steps : int
        Number of steps to take with each chain.
    num_chains : int, optional
        Number of chains to use. Will be set to the number of CPUs by default.
    num_warmup_steps : int, optional
        Number of burn-in steps to discard. Will be set to half the number of steps by
        default.
    log_interval : datetime.timedelta, optional
        Interval between each logging event.

    Raises
    ------
    ValueError
        If the inputs are inconsistent.
    """
    if num_samples < 0:
        raise ValueError("The number of samples must be positive")
    if num_chains == 0:
        raise ValueError("Sampling requires at least one chain")

    settings.max_threads = min(psutil.cpu_count(logical=False), max_threads)

    # If the number of chains is not specified, use at least as many as the number of
    # CPUs.
    if num_chains < 0:
        num_chains = max(settings.max_threads, default_min_chains)

    # If the number of warmup steps is not specified, set it to half the number of
    # steps.
    min_steps_per_chain = math.ceil(num_samples / num_chains)
    if num_warmup_steps < 0:
        num_warmup_steps = math.ceil(num_steps / 2)
    if num_warmup_steps + min_steps_per_chain > num_steps:
        raise ValueError(
            "The chosen number of steps is insufficient for the chosen number of "
            "samples"
        )

    # Compute the steps thinning and adjust the total steps count if needed.
    samples_per_chain = max(math.ceil(num_samples / num_chains), min_samples_per_chain)
    steps_thinning = math.ceil((num_steps - num_warmup_steps) / samples_per_chain)
    num_steps = num_warmup_steps + samples_per_chain * steps_thinning

    settings.num_steps = num_steps
    settings.num_chains = num_chains
    settings.steps_thinning = steps_thinning
    settings.num_skipped_steps = num_warmup_steps
    settings.log_interval = datetime.timedelta(seconds=1)
    settings.log_directory = ""
