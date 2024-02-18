"""Unit tests for the uniform sampler."""
import cobra

from pta.sampling.uniform import sample_flux_space_uniform


def test_uniform_sampling(e_coli_core: cobra.Model):
    """Verify that the uniform sampler works and reaches the convergence criteria."""
    e_coli_core.reactions.BIOMASS_Ecoli_core_w_GAM.lower_bound = 0.5

    result = sample_flux_space_uniform(e_coli_core, 1000)
    assert result.check_convergence()
