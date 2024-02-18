"""Abstract base class for sampling over the flux polytope."""

import logging
from typing import List, Tuple

import numpy as np
from PolyRound.api import PolyRoundApi, Polytope
from pta.utils import apply_transform

from .commons import SamplerInterface

logger = logging.getLogger(__name__)


class FluxSpaceSamplingModel(SamplerInterface):
    """Object holding the information necessary to sample a flux space.

    Parameters
    ----------
    polytope : Polytope
        Polytope object describing the flux space.
    reaction_ids : List[str]
        Identifiers of the reactions in the flux space.
    """

    # pylint: disable=abstract-method

    def __init__(self, polytope: Polytope, reaction_ids: List[str]):
        rounded_polytope = PolyRoundApi.simplify_transform_and_round(polytope)
        self._G = rounded_polytope.A.to_numpy()
        self._h = rounded_polytope.b.to_numpy()[:, np.newaxis]
        self._to_fluxes_transform = (
            rounded_polytope.transformation.to_numpy(),
            rounded_polytope.shift.to_numpy()[:, np.newaxis],
        )
        self._reaction_ids = reaction_ids
        logger.info(
            f"Created flux polytope with {self.dimensionality} dimensions and "
            f"{self.h.size} constraints."
        )

    @property
    def G(self) -> np.array:
        """Gets the left-hand side of the constraints of the flux space."""
        return self._G

    @property
    def h(self) -> np.array:
        """Gets the right-hand side of the constraints of the flux space."""
        return self._h

    @property
    def to_fluxes_transform(self) -> Tuple[np.array, np.array]:
        """Gets the transform from a point in the model to a point in the flux space."""
        return self._to_fluxes_transform

    @property
    def reaction_ids(self):
        """Gets the IDs of the reactions in the model."""
        return self._reaction_ids

    def to_fluxes(self, value: np.array) -> np.array:
        """Transform a point or matrix from the model to the flux space.

        Parameters
        ----------
        value : np.array
            Input values.

        Returns
        -------
        np.array
            The corresponding fluxes.
        """
        return apply_transform(value, self.to_fluxes_transform)

    @property
    def dimensionality(self) -> int:
        """Gets the dimensionality of the flux space."""
        return self.G.shape[1]

    def get_initial_points(self, num_points: int) -> np.array:
        """Gets initial points for sampling fluxes.

        Parameters
        ----------
        model : UniformSamplingModel
            The model to sample.
        num_points : int
            Number of initial points to generate.

        Returns
        -------
        np.array
            Array containing the initial points.
        """
        # Find the radius of the hypersphere inscribed in the polytope.
        distances = self.h / np.linalg.norm(self.G, axis=1)
        radius = np.min(distances)

        # Sample random directions and scale them to a random length inside the hypersphere.
        samples = np.random.rand(self.dimensionality, num_points)
        length = np.random.rand(1, num_points) ** (
            1 / self.dimensionality
        ) / np.linalg.norm(samples, axis=0)
        samples = samples * np.diag(length) * radius

        logger.info(f"Generated {num_points} initial points.")
        return samples
