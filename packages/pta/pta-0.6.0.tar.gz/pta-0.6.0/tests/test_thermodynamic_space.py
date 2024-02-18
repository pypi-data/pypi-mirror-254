"""Unit tests for the thermodynamic_space module."""
import cobra
import numpy as np
import pytest
from enkie import CompartmentParameters, Metabolite
from enkie.estimators import EquilibratorGibbsEstimator

from pta.commons import Q
from pta.concentrations_prior import ConcentrationsPrior
from pta.thermodynamic_space import ThermodynamicSpace, ThermodynamicSpaceBasis
from pta.utils import get_candidate_thermodynamic_constraints, get_internal_reactions


def test_creation_cobra(
    e_coli_core: cobra.Model, equilibrator: EquilibratorGibbsEstimator
):
    """Verify that creation of the thermodynamic space from a cobrapy model works."""
    constraint_rxns = get_internal_reactions(e_coli_core)

    thermodynamic_space = ThermodynamicSpace.from_cobrapy_model(
        e_coli_core,
        "bigg.metabolite",
        constraint_rxns,
        equilibrator,
        CompartmentParameters(),
        None,
    )

    assert thermodynamic_space.drg0_prime_mean.size == len(constraint_rxns)


def test_creation_with_estimates():
    """Verify that creation of the thermodynamic space from given estimates works."""
    S = np.array(
        [
            [1, -1, 0],
            [0, 1, -1],
            [-1, 0, 1],
        ]
    )

    metabolites = [
        Metabolite("M_A", "c", 11, -2),
        Metabolite("M_B", "c", 11, -2),
        Metabolite("M_C", "c", 11, -2),
    ]

    constraint_rxn_ids = ["R1", "R2", "R3"]

    dfg0_estimate = (
        Q(np.array([0, 1, 2]).T, "kJ/mol"),
        Q(np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), "kJ**2/mol**2"),
    )

    thermodynamic_space = ThermodynamicSpace(
        S,
        constraint_rxn_ids,
        metabolites,
        CompartmentParameters(),
        ConcentrationsPrior(),
        dfg0_estimate=dfg0_estimate,
    )

    assert thermodynamic_space.drg0_prime_mean.size == len(constraint_rxn_ids)


@pytest.mark.parametrize(
    "S, metabolites, constraint_rxn_ids, explicit_conc, dimensions",
    [
        (
            np.array(
                [
                    [1, -1, 0],
                    [0, 1, -1],
                    [-1, 0, 1],
                ]
            ),
            [
                Metabolite("g1p_c", "bigg.metabolite:g1p", "c", 11, -2),
                Metabolite("g6p_c", "bigg.metabolite:g6p", "c", 11, -2),
                Metabolite("f6p_c", "bigg.metabolite:f6p", "c", 11, -2),
            ],
            ["A", "B", "C"],
            False,
            2,
        ),
        (
            np.array(
                [
                    [1, -1, 0],
                    [0, 1, -1],
                    [-1, 0, 1],
                ]
            ),
            [
                Metabolite("g1p_c", "bigg.metabolite:g1p", "c", 11, -2),
                Metabolite("g6p_c", "bigg.metabolite:g6p", "c", 11, -2),
                Metabolite("f6p_c", "bigg.metabolite:f6p", "c", 11, -2),
            ],
            ["A", "B", "C"],
            True,
            5,
        ),
    ],
)
def test_minimal_basis(
    equilibrator, S, metabolites, constraint_rxn_ids, explicit_conc, dimensions
):
    """Verify that the minimal basis has correct dimensionality."""
    thermodynamic_space = ThermodynamicSpace(
        S, constraint_rxn_ids, metabolites, estimator=equilibrator
    )

    minimal_basis = ThermodynamicSpaceBasis(
        thermodynamic_space, explicit_conc, False, True
    )

    assert np.size(minimal_basis.to_drg_transform[0], 1) == dimensions
    assert explicit_conc != (minimal_basis.to_log_conc_transform is None)


def test_large_minimal_basis(
    e_coli_core: cobra.Model, equilibrator: EquilibratorGibbsEstimator
):
    """Verify that a minimal basis can be constructed for the E. coli core model."""
    constraint_rxns = get_internal_reactions(e_coli_core)

    thermodynamic_space = ThermodynamicSpace.from_cobrapy_model(
        e_coli_core,
        "bigg.metabolite",
        constraint_rxns,
        equilibrator,
        CompartmentParameters(),
        None,
    )

    minimal_basis = ThermodynamicSpaceBasis(thermodynamic_space, True, True, True)
    assert minimal_basis is not None


def test_get_candidate_thermodynamic_constraints(e_coli_core: cobra.Model):
    """Verify that candidate thermodynamic constraints are found correctly."""
    candidates = get_candidate_thermodynamic_constraints(
        e_coli_core,
        "bigg.metabolite",
    )

    assert "H2Ot" not in candidates
    assert "BIOMASS_Ecoli_core_w_GAM" not in candidates
    assert all("EX_" not in c for c in candidates)
    assert (
        len(candidates) == len(e_coli_core.reactions) - len(e_coli_core.exchanges) - 2
    )
