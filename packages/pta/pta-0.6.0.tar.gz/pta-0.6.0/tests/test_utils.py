"""Test for PTA's utility functions."""
import cobra
import numpy as np
from pta.utils import find_rotation_matrix, get_internal_cycles

cobra_config = cobra.Configuration()
cobra_config.processes = 1


def test_get_internal_cycles(e_coli_core: cobra.Model):
    """Verify that the internal cycles of the core model are found."""
    cycles = get_internal_cycles(e_coli_core)
    assert cycles.shape[1] == 1


def test_get_rotation_matrix():
    """Verify that rotation matrices are correctly estimated."""
    x = np.array([[5, 0, 0, 0, 0, 0]]).T
    y = np.array([[1, 5, 4, 3.3, 2, -8]]).T

    R = find_rotation_matrix(x, y)

    assert np.allclose(R @ R.T, np.identity(len(x)))
    y2 = R @ x
    assert np.allclose(y / np.linalg.norm(y), y2 / np.linalg.norm(y2))
