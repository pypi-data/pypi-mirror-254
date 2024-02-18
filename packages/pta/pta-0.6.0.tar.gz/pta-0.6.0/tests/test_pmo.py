"""Unit tests for the PMO class."""
import math

import cobra
import numpy as np
from enkie import CompartmentParameters, Metabolite
from enkie.estimators import EquilibratorGibbsEstimator

import pta
from pta.commons import Q
from pta.concentrations_prior import ConcentrationsPrior
from pta.flux_space import FluxSpace
from pta.model_assessment import prepare_for_pta
from pta.pmo import PmoProblem
from pta.thermodynamic_space import ThermodynamicSpace

cobra_config = cobra.Configuration()
cobra_config.processes = 1


def test_pmo(equilibrator: EquilibratorGibbsEstimator):
    """Verify that PMO's results are consistent on a small toy model."""
    S = np.array(
        [
            [1, -1, 0],
            [0, 1, -1],
        ]
    )

    metabolites = [
        Metabolite("bigg.metabolite:g6p", "c", 11, -2),
        Metabolite("bigg.metabolite:f6p", "c", 11, -2),
    ]

    reaction_ids = ["R1", "R2", "R3"]

    dfg0_estimate = (
        Q(np.array([0, 1]).T, "kJ/mol"),
        Q(np.array([[0.1, 0], [0, 0.1]]), "kJ/mol"),
    )

    thermodynamic_space = ThermodynamicSpace(
        S[:, [1]],
        reaction_ids[1:2],
        metabolites,
        parameters=CompartmentParameters(),
        concentrations=ConcentrationsPrior(),
        dfg0_estimate=dfg0_estimate,
    )

    flux_space = FluxSpace(
        S,
        np.array([[0, 0, 1]]).T,
        np.array([[1000, 1000, 10]]).T,
        reaction_ids,
        [m.id for m in metabolites],
    )

    problem = PmoProblem(flux_space, thermodynamic_space, solver="GUROBI")
    status = problem.solve(verbose=True)

    assert status == "optimal"
    log_c = problem.log_c
    assert math.exp(log_c[0]) > math.exp(log_c[1])
    assert problem.v[1] >= 1 - 1e-8 and problem.v[1] <= 10 + 1e-8


def test_pmo_large(e_coli_core: cobra.Model, equilibrator: EquilibratorGibbsEstimator):
    """Verify that PMO can find a solution of the E. coli core model."""
    prepare_for_pta(e_coli_core)
    thermodynamic_space = pta.ThermodynamicSpace.from_cobrapy_model(
        e_coli_core,
        parameters=CompartmentParameters.load("e_coli"),
        estimator=equilibrator,
    )
    problem = PmoProblem(e_coli_core, thermodynamic_space, solver="GUROBI")

    status = problem.solve(verbose=True)
    assert status == "optimal"

    problem2 = problem.rebuild_for_directions(problem.d.value)
    status = problem2.solve(verbose=True)
    assert status == "optimal"
