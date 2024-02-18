"""Configuration and common fixtures for PTA's unit tests."""
import cobra
import pytest
from enkie.estimators import EquilibratorGibbsEstimator
from equilibrator_cache.compound_cache import CompoundCache

import pta


@pytest.fixture(scope="session", name="equilibrator")
def fixture_equilibrator() -> EquilibratorGibbsEstimator:
    """Global fixture for the equilibrator API."""
    return EquilibratorGibbsEstimator()


@pytest.fixture(scope="session")
def compound_cache(
    equilibrator: EquilibratorGibbsEstimator,
) -> CompoundCache:
    """Global fixture for equilibrator's compound cache'."""
    return equilibrator.eq_api.ccache


@pytest.fixture
def e_coli_core() -> cobra.Model:
    """Fixture for the E. coli core model."""
    return pta.utils.load_example_model("e_coli_core")


@pytest.fixture
def phosphohexoses_model() -> cobra.Model:
    """Fixture for a small model of phosphohexoses interconversion."""
    return pta.utils.load_example_model("phosphohexoses")
