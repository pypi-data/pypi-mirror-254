"""Description of the space of thermodynamics-related quantities of a metabolic network.
"""

import logging
from typing import Dict, List, Optional, Set, Tuple, Union

import cobra
import numpy as np
import numpy.linalg as la
import scipy.linalg
from cobra.util.array import create_stoichiometric_matrix
from component_contribution.linalg import LINALG
from enkie import CompartmentParameters, Metabolite
from enkie.constants import R
from enkie.estimators import (EquilibratorGibbsEstimator,
                              GibbsEstimatorInterface)
from enkie.io.cobra import parse_metabolites
from enkie.utils import qrvector, qvector

from .commons import Q
from .concentrations_prior import ConcentrationsPrior
from .constants import default_min_eigenvalue_tds_basis
from .utils import (apply_transform, covariance_square_root,
                    get_candidate_thermodynamic_constraints, to_reactions_ids,
                    to_reactions_idxs)

logger = logging.getLogger(__name__)


class ThermodynamicSpace:
    """
    Construction, description and manipulation of the thermodynamic space of
    a metabolic network.

    Parameters
    ----------
    S_constraints : np.ndarray
        Stoichiometric matrix of the reactions covered by thermodynamic constraints.
    reaction_ids : List[str]
        Identifiers of the reactions covered by thermodynamic constraints.
    metabolites : List[Metabolite]
        List describing the metabolites in the network.
    parameters : CompartmentParameters, optional
        The physiological parameters (pH, ionic strength, ...) of each compartment.
    concentrations : ConcentrationsPrior, optional
        Prior distributions for the metabolite concentrations.
    estimator : GibbsEstimatorInterface, optional
        Object used to estimate Gibbs free energies.
    dfg0_estimate : Optional[Tuple[Q, Q]], optional
        Estimate of formation energies (mean and a square root of the covariance matrix)
        in case the user wants to specify them manually. This is only used if
        :code:`estimator` is :code:`None`.
    """

    def __init__(
        self,
        S_constraints: np.ndarray,
        reaction_ids: List[str],
        metabolites: List[Metabolite],
        parameters: CompartmentParameters = None,
        concentrations: ConcentrationsPrior = None,
        estimator: GibbsEstimatorInterface = None,
        dfg0_estimate: Optional[Tuple[Q, Q]] = None,
    ):
        self._S_constraints = S_constraints
        self._reaction_ids = reaction_ids
        self._metabolites = metabolites
        self._parameters = parameters or CompartmentParameters.load("default")

        if estimator is None and dfg0_estimate is not None:
            self._dfg0_prime_mean, self._dfg0_prime_cov_sqrt = dfg0_estimate
        else:
            if dfg0_estimate is not None:
                logger.warning(
                    "dfg0_estimate ignored, since an estimator has "
                    "has been passed to ThermodynamicSpace."
                )

            estimator = estimator or EquilibratorGibbsEstimator()
            self._dfg0_prime_mean, self._dfg0_prime_cov_sqrt = estimator.get_dfg0_prime(
                self.S_constraints, metabolites, self._parameters
            )

        concentrations = concentrations or ConcentrationsPrior()
        self._concentrations = concentrations

        (
            self._log_conc_mean,
            self._log_conc_cov,
        ) = self._make_concentrations_distribution(metabolites, concentrations)

    @property
    def dfg0_prime_mean(self) -> Q:
        """Gets the mean of the corrected standard formation energies."""
        return self._dfg0_prime_mean

    @property
    def dfg0_prime_cov(self) -> Q:
        """Gets the covariance of the corrected standard formation energies."""
        return self._dfg0_prime_cov_sqrt @ self._dfg0_prime_cov_sqrt.T

    @property
    def dfg0_prime_cov_sqrt(self) -> Q:
        """Gets a square root of the covariance of the corrected standard
        formation energies.
        """
        return self._dfg0_prime_cov_sqrt

    @property
    def drg0_prime_mean(self) -> Q:
        """Gets the mean of the corrected standard reaction energies."""
        return self.S_constraints.T @ self.dfg0_prime_mean

    @property
    def drg0_prime_cov(self) -> Q:
        """Gets the covariance of the corrected standard reaction energies."""
        return self.drg0_prime_cov_sqrt @ self.drg0_prime_cov_sqrt.T

    @property
    def drg0_prime_cov_sqrt(self) -> Q:
        """Gets a square root of the covariance of the corrected standard
        reaction energies.
        """
        return self.S_constraints.T @ self.dfg0_prime_cov_sqrt

    @property
    def log_conc_mean(self):
        """Gets the mean of the log-concentrations."""
        return self._log_conc_mean

    @property
    def log_conc_cov(self):
        """Gets the covariance of the log-concentrations."""
        return self._log_conc_cov

    @property
    def dfg_prime_mean(self):
        """Gets the mean of the formation energies."""
        return self.dfg0_prime_mean + self.log_conc_mean * R * self.parameters.T()

    @property
    def dfg_prime_cov(self):
        """Gets the covariance of the formation energies."""
        return self.dfg0_prime_cov + self.log_conc_cov * (R * self.parameters.T()) ** 2

    @property
    def drg_prime_mean(self):
        """Gets the mean of the reaction energies."""
        return self.S_constraints.T @ self.dfg_prime_mean

    @property
    def drg_prime_cov(self):
        """Gets the covariance of the reaction energies."""
        return self.S_constraints.T @ self.dfg_prime_cov @ self.S_constraints

    @property
    def parameters(self) -> CompartmentParameters:
        """Gets the compartment parameters of the system."""
        return self._parameters

    @property
    def metabolites(self) -> List[Metabolite]:
        """Gets the list of metabolites in the thermodynamic space."""
        return self._metabolites

    @property
    def S_constraints(self) -> np.ndarray:
        """Gets stoichiometric matrix of the reactions with thermodynamic
        constraints."""
        return self._S_constraints

    @property
    def metabolite_ids(self) -> List[str]:
        """Gets the IDs of the metabolites in the thermodynamic space."""
        return [m.id for m in self.metabolites]

    @property
    def reaction_ids(self) -> List[str]:
        """Gets the IDs of the reactions with thermodynamic constraints."""
        return self._reaction_ids

    def subspace(
        self, reaction_ids: Set[str], metabolite_ids: Set[str]
    ) -> "ThermodynamicSpace":
        reaction_idxs = [
            i for i, r in enumerate(self.reaction_ids) if r in reaction_ids
        ]
        metabolite_idxs = [
            i for i, m in enumerate(self.metabolites) if m.id in metabolite_ids
        ]

        return ThermodynamicSpace(
            self.S_constraints[np.ix_(metabolite_idxs, reaction_idxs)].copy(),
            [self.reaction_ids[i] for i in reaction_idxs],
            [self.metabolites[i] for i in metabolite_idxs],
            self.parameters,
            self._concentrations,
            dfg0_estimate=(
                Q(self.dfg0_prime_mean.m[metabolite_idxs,:], "kJ/mol"),
                Q(LINALG.qr_rank_deficient(self.dfg0_prime_cov_sqrt.m[metabolite_idxs, :].T).T, "kJ/mol"),
            ),
        )

    @staticmethod
    def from_cobrapy_model(
        model: cobra.Model,
        metabolites_namespace: str = None,
        constrained_rxns: Union[List[int], List[str], cobra.DictList] = None,
        estimator: GibbsEstimatorInterface = None,
        parameters: CompartmentParameters = None,
        concentrations: ConcentrationsPrior = None,
        dfg0_estimate: Optional[Tuple[Q, Q]] = None,
    ) -> "ThermodynamicSpace":
        """Constructs a thermodynamic space from a cobrapy model.

        Parameters
        ----------
        model : cobra.Model
            Cobra model describing the metabolic network.
        metabolites_namespace : str, optional
            Specifies the name to use when reading metabolite identifiers from the SBML
            model annotations.
        constrained_rxns : Union[List[int], List[str], cobra.DictList], optional
            The reactions that should be modeled with thermodynamic constraints. Usually
            this list should contain all reactions except biomass and boundary
            reactions. The list can contain either the reactions themselves, their
            indices or they identifiers.
        estimator : GibbsEstimatorInterface, optional
            Object used to estimate Gibbs free energies.
        parameters : CompartmentParameters, optional
            The physiological parameters (pH, ionic strength, ...) of each compartment.
        concentrations : ConcentrationsPrior, optional
            Prior distributions for the metabolite concentrations.

        Returns
        -------
        ThermodynamicSpace
            The thermodynamic space for the specified model.
        """
        if constrained_rxns is None:
            constrained_rxns = get_candidate_thermodynamic_constraints(
                model,
                metabolites_namespace,
            )

        constrained_rxn_ids = to_reactions_ids(constrained_rxns, model)
        constrained_rxn_idxs = to_reactions_idxs(constrained_rxns, model)

        S_constraints = create_stoichiometric_matrix(model)[:, constrained_rxn_idxs]
        is_metabolite_needed = np.sum(np.abs(S_constraints), axis=1) > 0
        needed_metabolites_ids = [
            model.metabolites[i].id for i in np.where(is_metabolite_needed)[0]
        ]
        S_constraints = S_constraints[is_metabolite_needed, :]

        # Parse metabolites from the model.
        metabolites = parse_metabolites(
            model, needed_metabolites_ids, metabolites_namespace
        )

        return ThermodynamicSpace(
            S_constraints,
            constrained_rxn_ids,
            list(metabolites.values()),
            parameters,
            concentrations,
            estimator,
            dfg0_estimate,
        )

    def _make_concentrations_distribution(
        self,
        metabolites: List[Metabolite],
        concentrations: ConcentrationsPrior,
    ) -> Tuple[Q, Q]:
        """Construct the distribution over metabolite concentrations."""
        log_conc_mean = qvector(
            [
                Q(concentrations.get(m.miriam_id, m.compartment).log_mean)
                for m in metabolites
            ]
        )
        log_conc_cov = Q(
            np.diag(
                np.square(
                    qrvector(
                        [
                            Q(concentrations.get(m.miriam_id, m.compartment).log_std)
                            for m in metabolites
                        ]
                    ).m
                )
            )
        )

        return log_conc_mean, log_conc_cov


class ThermodynamicSpaceBasis:
    """
    Full-dimensional basis of the thermodynamic space. It is possible to make only
    selected variables explicit in the basis, reducing its dimensionality.

    Parameters
    ----------
    thermodynamic_space : ThermodynamicSpace
        The target thermodynamic space.
    explicit_log_conc : bool, optional
        True if log-concentrations should be represented explicitly in the basis, false
        otherwise. By default True.
    explicit_drg0 : bool, optional
        True if standard reaction energies should be represented explicitly in the
        basis, false otherwise. By default True.
    explicit_drg : bool, optional
        True if reaction energies should be represented explicitly in the basis, false
        otherwise. By default True.
    min_eigenvalue : float, optional
        Minimum eigenvalue of for a vector to be part of the basis.
    """

    def __init__(
        self,
        thermodynamic_space: "ThermodynamicSpace",
        explicit_log_conc: bool = True,
        explicit_drg0: bool = True,
        explicit_drg: bool = True,
        min_eigenvalue: float = default_min_eigenvalue_tds_basis,
    ):
        self._to_log_conc_transform: Optional[Tuple[np.ndarray, np.ndarray]] = None
        self._to_drg0_transform: Optional[Tuple[np.ndarray, np.ndarray]] = None
        self._to_drg_transform: Optional[Tuple[np.ndarray, np.ndarray]] = None

        self._observables_ranges: Dict[str, List[int]] = {
            "drg": [],
            "drg0": [],
            "log_conc": [],
        }

        self._compute_basis(
            thermodynamic_space,
            explicit_log_conc,
            explicit_drg0,
            explicit_drg,
            min_eigenvalue,
        )

    @property
    def to_log_conc_transform(self) -> Optional[Tuple[np.ndarray, np.ndarray]]:
        """Gets the transformation from this space to log-concentrations. :code:`None`
        if concentrations are not represented explicitly."""
        return self._to_log_conc_transform

    @property
    def to_drg0_transform(self) -> Optional[Tuple[np.ndarray, np.ndarray]]:
        """Gets the transformation from this space to DrG'°. :code:`None`
        if standard reaction energies are not represented explicitly."""
        return self._to_drg0_transform

    @property
    def to_drg_transform(self) -> Optional[Tuple[np.ndarray, np.ndarray]]:
        """Gets the transformation from this space to DrG'. :code:`None`
        if reaction energies are not represented explicitly."""
        return self._to_drg_transform

    @property
    def to_observables_transform(self) -> Tuple[np.ndarray, np.ndarray]:
        """Gets the transformation from this space to the selected observables."""
        return self._to_observables_transform

    @property
    def observables_ranges(self) -> Dict[str, List[int]]:
        """The ranges of the different variables in a vector of observables."""
        return self._observables_ranges

    @property
    def sigmas(self) -> np.ndarray:
        """Gets a vector containing the standard deviation of each variable in
        the minimal basis."""
        return self._sigmas

    @property
    def dimensionality(self) -> int:
        """Gets the dimensionality of the basis."""
        return self._dimensionality

    def to_log_conc(self, basis_vars: np.ndarray) -> np.ndarray:
        """Transform a vector or matrix in the basis to a vector or matrix of
        log-concentrations.

        Parameters
        ----------
        basis_vars : np.ndarray
            The input vector or matrix.

        Returns
        -------
        np.ndarray
            The transformed vector or matrix. :code:`None` if concentrations are not
            represented explicitly.
        """
        if not self.to_log_conc_transform:
            return None
        else:
            return apply_transform(basis_vars, self.to_log_conc_transform)

    def to_drg0(self, basis_vars: np.ndarray) -> np.ndarray:
        """Transform a vector or matrix in the basis to a vector or matrix of
        standard reaction energies.

        Parameters
        ----------
        basis_vars : np.ndarray
            The input vector or matrix.

        Returns
        -------
        np.ndarray
            The transformed vector or matrix. :code:`None` if standard reaction energies
            are not represented explicitly.
        """
        if not self.to_drg0_transform:
            return None
        else:
            return apply_transform(basis_vars, self.to_drg0_transform)

    def to_drg(self, basis_vars: np.ndarray) -> np.ndarray:
        """Transform a vector or matrix in the basis to a vector or matrix of
        reaction energies.

        Parameters
        ----------
        basis_vars : np.ndarray
            The input vector or matrix.

        Returns
        -------
        np.ndarray
            The transformed vector or matrix. :code:`None` if reaction energies are not
            represented explicitly.
        """
        if not self.to_drg_transform:
            return None
        else:
            return apply_transform(basis_vars, self.to_drg_transform)

    def _compute_basis(
        self,
        thermodynamic_space: "ThermodynamicSpace",
        explicit_log_conc,
        explicit_drg0,
        explicit_drg,
        tolerance,
    ):
        """Compute the basis of the thermodynamic space, only making explicit the
        specified variables.
        """
        log_conc_mean = thermodynamic_space.log_conc_mean.m
        log_conc_cov = thermodynamic_space.log_conc_cov.m
        drg0_prime_mean = thermodynamic_space.drg0_prime_mean.m_as("kJ/mol")
        drg0_prime_cov_sqrt = thermodynamic_space.drg0_prime_cov_sqrt.m_as("kJ/mol")
        S_con_T = thermodynamic_space.S_constraints.T
        RT = (R * thermodynamic_space.parameters.T()).m_as("kJ/mol")
        n_mets = log_conc_mean.size
        n_rxns = drg0_prime_mean.size

        # Use the eigenvalue decomposition to find the minimal basis for the
        # log concentrations.
        log_conc_cov_sqrt = covariance_square_root(log_conc_cov, tolerance)

        # Combined mean and squared root of the covariance of log-concentrations
        # and DrG'°.
        log_conc_drg0_mean = np.block([[log_conc_mean], [drg0_prime_mean]])

        log_conc_drg0_cov_sqrt = scipy.linalg.block_diag(
            log_conc_cov_sqrt, drg0_prime_cov_sqrt
        )

        # Construct the transform from log-concentrations and DrG'° to the
        # variables that must be explicitly represented ("observables").
        mapping_blocks = []
        if explicit_log_conc:
            mapping_blocks.append([np.identity(n_mets), np.zeros((n_mets, n_rxns))])
        if explicit_drg0:
            mapping_blocks.append([np.zeros((n_rxns, n_mets)), np.identity(n_rxns)])
        if explicit_drg:
            mapping_blocks.append([RT * S_con_T, np.identity(n_rxns)])

        to_observables = np.block(mapping_blocks)
        observables_mean = to_observables @ log_conc_drg0_mean
        observables_cov_sqrt = to_observables @ log_conc_drg0_cov_sqrt

        # Find a square root for the covariance matrix with minimum
        # dimensionality using the QR decomposition.
        observables_cov_sqrt = LINALG.qr_rank_deficient(observables_cov_sqrt.T).T
        observables_cov_sqrt[np.abs(observables_cov_sqrt) < 1e-5] = 0
        self._to_observables_transform = (observables_cov_sqrt, observables_mean)
        self._dimensionality = observables_cov_sqrt.shape[1]
        self._sigmas = la.norm(observables_cov_sqrt, axis=0).T

        # Finally, identify the transforms from the basis to the single
        # observables.
        current_id = 0
        if explicit_log_conc:
            self._observables_ranges["log_conc"] = list(
                range(current_id, current_id + n_mets)
            )
            self._to_log_conc_transform = (
                observables_cov_sqrt[self.observables_ranges["log_conc"], :],
                observables_mean[self.observables_ranges["log_conc"]],
            )
            current_id += n_mets
        if explicit_drg0:
            self._observables_ranges["drg0"] = list(
                range(current_id, current_id + n_rxns)
            )
            self._to_drg0_transform = (
                observables_cov_sqrt[self.observables_ranges["drg0"], :],
                observables_mean[self.observables_ranges["drg0"]],
            )
            current_id += n_rxns
        if explicit_drg:
            self._observables_ranges["drg"] = list(
                range(current_id, current_id + n_rxns)
            )
            self._to_drg_transform = (
                observables_cov_sqrt[self.observables_ranges["drg"], :],
                observables_mean[self.observables_ranges["drg"]],
            )
