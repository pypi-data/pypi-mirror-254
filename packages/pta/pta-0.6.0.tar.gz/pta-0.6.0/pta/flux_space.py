"""Description of the flux space of a metabolic network.
"""

import logging
from typing import List, Tuple

import numpy as np
import pandas as pd

import cobra
from cobra.util.array import create_stoichiometric_matrix
from PolyRound.api import PolyRoundApi, Polytope

logger = logging.getLogger(__name__)


class FluxSpace:
    """Description of the flux space of a metabolic network.

    Parameters
    ----------
    S : np.ndarray
        Stoichiometric matrix of the network.
    lb : np.ndarray
        Vector of lower bounds on the reaction fluxes.
    ub : np.ndarray
        Vector of upper bounds on the reaction fluxes.
    reaction_ids : List[str]
        Identifiers of the reactions in the network.
    metabolite_ids : List[str]
        Identifiers of the metabolites in the network.
    """

    def __init__(
        self,
        S: np.ndarray,
        lb: np.ndarray,
        ub: np.ndarray,
        reaction_ids: List[str],
        metabolite_ids: List[str],
    ):
        self._S = S
        self._lb = lb
        self._ub = ub
        self._reaction_ids = reaction_ids
        self._metabolite_ids = metabolite_ids

    @property
    def S(self) -> np.ndarray:
        """Gets the stoichiometric matrix of the network."""
        return self._S

    @S.setter
    def S(self, value: np.ndarray):
        """Sets the stoichiometric matrix of the network."""
        self._S = value

    @property
    def lb(self) -> np.ndarray:
        """Gets the vector of lower bounds on the reaction fluxes."""
        return self._lb

    @lb.setter
    def lb(self, value: np.ndarray):
        """Sets the vector of lower bounds on the reaction fluxes."""
        self._lb = value

    @property
    def ub(self) -> np.ndarray:
        """Gets the vector of upper bounds on the reaction fluxes."""
        return self._ub

    @ub.setter
    def ub(self, value: np.ndarray):
        """Sets the vector of upper bounds on the reaction fluxes."""
        self._ub = value

    @property
    def reaction_ids(self) -> List[str]:
        """Gets the IDs of the reactions in the flux space."""
        return self._reaction_ids

    @property
    def metabolite_ids(self) -> List[str]:
        """Gets the IDs of the metabolites in the flux space."""
        return self._metabolite_ids

    @property
    def n_metabolites(self) -> int:
        """Gets the number of metabolites in the network."""
        return self._S.shape[0]

    @property
    def n_reactions(self) -> int:
        """Gets the number of reactions in the network."""
        return self._S.shape[1]

    @property
    def n_reversible_reactions(self) -> int:
        """Gets the number of reversible reactions in the network."""
        return len(
            [i for i in range(self.n_reactions) if self.lb[i] < 0 and self.ub[i] > 0]
        )

    def copy(self) -> "FluxSpace":
        """Create a copy of this object.

        Returns
        -------
        FluxSpace
            A copy of this object.
        """
        return FluxSpace(
            self.S.copy(),
            self.lb.copy(),
            self.ub.copy(),
            self.reaction_ids.copy(),
            self.metabolite_ids.copy(),
        )

    @staticmethod
    def from_cobrapy_model(model: cobra.Model) -> "FluxSpace":
        """Creates an instance of this class from a cobrapy model.

        Parameters
        ----------
        model : cobra.Model
            The input model.

        Returns
        -------
        FluxSpace
            The constructed object.
        """
        return FluxSpace(
            create_stoichiometric_matrix(model),
            np.array([[r.lower_bound for r in model.reactions]]).T,
            np.array([[r.upper_bound for r in model.reactions]]).T,
            [r.id for r in model.reactions],
            [m.id for m in model.metabolites],
        )


class FluxSpaceBasis(object):
    """Full-dimensional basis of the flux space. The parametrization is automatically
    rounded using PolyRound.
    """

    def __init__(self, flux_space: FluxSpace):
        polytope = FluxSpaceBasis._make_polytools_polytope(flux_space)
        rounded_polytope = PolyRoundApi.simplify_transform_and_round(polytope)

        self._G = rounded_polytope.A.to_numpy()
        self._h = rounded_polytope.b.to_numpy()[:, np.newaxis]
        self._to_fluxes_transform = (
            rounded_polytope.transformation.to_numpy(),
            rounded_polytope.shift.to_numpy()[:, np.newaxis],
        )

        logger.info(
            f"Created flux space basis with {self.dimensionality} dimensions and "
            f"{self.h.size} constraints."
        )

    @property
    def G(self) -> np.ndarray:
        """Gets the left-hand side of the constraints of the flux space."""
        return self._G

    @property
    def h(self) -> np.ndarray:
        """Gets the right-hand side of the constraints of the flux space."""
        return self._h

    @property
    def to_fluxes_transform(self) -> Tuple[np.ndarray, np.ndarray]:
        """Gets the transform from a point in the model to a point in the flux space."""
        return self._to_fluxes_transform

    @property
    def dimensionality(self) -> int:
        """Gets the dimensionality of the flux space."""
        return self.G.shape[1]

    @staticmethod
    def _make_polytools_polytope(flux_space: FluxSpace):
        S_df = pd.DataFrame(
            data=flux_space.S,
            index=flux_space.metabolite_ids,
            columns=flux_space.reaction_ids,
        )
        n_react = len(flux_space.reaction_ids)
        A = pd.DataFrame(0.0, index=range(n_react * 2), columns=S_df.columns)
        b = pd.Series(0.0, index=range(n_react * 2))

        for i in range(len(flux_space.reaction_ids)):
            b[i] = flux_space.ub[i]
            b[i + n_react] = -flux_space.lb[i]
            A.iloc[i, i] += 1
            A.iloc[i + n_react, i] -= 1

        p = Polytope(A, b, S=S_df)

        return p
