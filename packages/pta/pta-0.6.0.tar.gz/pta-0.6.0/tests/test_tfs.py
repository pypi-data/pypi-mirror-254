"""Unit tests for the thermodynamics-based sampling methods."""
import cobra
from enkie import CompartmentParameters
from enkie.estimators import EquilibratorGibbsEstimator

import pta
from pta.sampling.tfs import (
    TFSModel,
    sample_drg,
    sample_drg0_from_drg,
    sample_fluxes_from_drg,
    sample_log_conc_from_drg,
)

cobra_config = cobra.Configuration()
cobra_config.processes = 1


def test_tfs(e_coli_core: cobra.Model, equilibrator: EquilibratorGibbsEstimator):
    """Verify that the TFS methods work."""
    e_coli_core.reactions.BIOMASS_Ecoli_core_w_GAM.lower_bound = 0.5
    pta.prepare_for_pta(e_coli_core)
    thermodynamic_space = pta.ThermodynamicSpace.from_cobrapy_model(
        e_coli_core,
        parameters=CompartmentParameters.load("e_coli"),
        estimator=equilibrator,
    )

    num_chains = 4
    tfs_model = TFSModel(e_coli_core, thermodynamic_space, solver="GUROBI")

    points = tfs_model.get_initial_points(num_chains)

    assert points.shape[1] == num_chains

    result = sample_drg(
        tfs_model,
        initial_points=points,
        num_chains=num_chains,
    )

    assert result is not None
    assert result.check_convergence()

    _ = sample_drg0_from_drg(thermodynamic_space, result.samples)
    _ = sample_log_conc_from_drg(thermodynamic_space, result.samples)
    _ = sample_fluxes_from_drg(e_coli_core, result.samples, result.orthants)

    assert True
