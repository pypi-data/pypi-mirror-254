"""Unit tests for PTA's concentrations prior class."""
from enkie.distributions import LogNormalDistribution

from pta.concentrations_prior import ConcentrationsPrior


def test_different_namespaces():
    """Verify that the concentrations prior can handle metabolite identifiers from
    different namespaces."""
    distribution = LogNormalDistribution(-5, 1)
    prior = ConcentrationsPrior(
        metabolite_distributions={("bigg.metabolite:g6p", "c"): distribution},
    )

    kegg_distribution = prior.get("kegg.compound:C00092", "c")
    assert kegg_distribution.log_mean == distribution.log_mean
    assert kegg_distribution.log_std == distribution.log_std
