"General utility functions."

import logging
import math
from pathlib import Path
from typing import List, Optional, Tuple, Union

import cobra
import efmtool
import numpy as np
import numpy.linalg as la
import pandas as pd
import pkg_resources
from cobra.flux_analysis.variability import (
    find_blocked_reactions,
    flux_variability_analysis,
)
from cobra.util import create_stoichiometric_matrix
from enkie.dbs import Metanetx
from enkie.io.cobra import parse_metabolite_id
from enkie.miriam_metabolite import MiriamMetabolite

from .constants import default_min_eigenvalue_tds_basis

logger = logging.getLogger(__name__)

WATER_OR_PROTON_IDS = {"WATER", "MNXM1", "MNXM01"}


def enable_all_logging(level: int = logging.INFO):
    """Enable detailed logging in PTA and its dependencies. This is useful to debug
    possible problems.

    Parameters
    ----------
    level : int, optional
        The desired logging level, by default logging.INFO
    """
    logging.basicConfig()
    logging.getLogger().setLevel(level)


def floor(value: float, decimals: int = 0) -> float:
    """Same as :code:`math.floor`, except that it rounds to a given number of decimals.

    Parameters
    ----------
    value : float
        Value to round.
    decimals : int, optional
        Number of decimals to round to, by default 0.

    Returns
    -------
    float
        The rounded value.
    """
    return math.floor(value * (10**decimals)) / (10**decimals)


def ceil(value: float, decimals: int = 0):
    """Same as :code:`math.ceil`, except that it rounds to a given number of decimals.

    Parameters
    ----------
    value : float
        Value to round.
    decimals : int, optional
        Number of decimals to round to, by default 0.

    Returns
    -------
    float
        The rounded value.
    """
    return math.ceil(value * (10**decimals)) / (10**decimals)


def get_internal_reactions(model: cobra.Model) -> List[str]:
    """Gets the identifiers of all internal (non boundary) reactions in the model.

    Parameters
    ----------
    model : cobra.Model
        The target model.

    Returns
    -------
    List[str]
        List of identifiers.
    """
    boundary_ids = {r.id for r in model.boundary}
    return model.reactions.query(lambda r: not r.id in boundary_ids)


def tighten_model_bounds(
    model: cobra.Model,
    margin: float = 1e-4,
    round_to_digits: int = 6,
    prevent_loops: bool = False,
    fva_result: pd.DataFrame = None,
):
    """Apply FVA to a model to reduce the range of the flux bounds. The FVA result (plus
    a margin) is applied to each reaction if it is tighter than the bounds in the model.

    Parameters
    ----------
    model : cobra.Model
        The model to analyze.
    margin : float, optional
        Margin to be applied to the FVA result when the computed bounds are tighter than
        the original ones. This avoids overconstraining the model in case of numerical
        inaccuracies in the solution. By default 1e-4.
    round_to_digits : int, optional
        Number of digits to which tighter bounds should be rounded to. This limits the
        range of the coefficients for optimization problems. By default 6.
    prevent_loops : bool, optional
        If no FVA solution is provided, determines whether regular or loopless FVA will
        be used.
    fva_result : pd.DataFrame, optional
        Precomputed FVA result. If specified, FVA will not be run again, by default
        None.
    """
    if fva_result is None:
        fva_result = flux_variability_analysis(
            model, loopless=prevent_loops, fraction_of_optimum=0.0
        )

    for r in model.reactions:
        lb = fva_result.loc[r.id, "minimum"]
        ub = fva_result.loc[r.id, "maximum"]

        if 0 <= lb <= margin:
            r.lower_bound = max(r.lower_bound, 0.0)
        else:
            r.lower_bound = max(r.lower_bound, floor(lb - margin, round_to_digits))

        if -margin <= ub <= 0:
            r.upper_bound = min(r.upper_bound, 0.0)
        else:
            r.upper_bound = min(r.upper_bound, ceil(ub + margin, round_to_digits))


def find_blocked_reactions_from_fva_solution(
    model: cobra.Model,
    prevent_loops: bool = False,
    zero_cutoff: Optional[float] = None,
    fva_result: pd.DataFrame = None,
) -> List[str]:
    """Similar to cobrapy's find_blocked_reactions(), but optionally takes a precomputed
    FVA solution as input.

    Parameters
    ----------
    model : cobra.Model
        The model to analyze.
    prevent_loops : bool, optional
        If no FVA solution is provided, determines whether regular or loopless FVA will
        be used.
    zero_cutoff : Optional[float], optional
        Flux value which is considered to effectively be zero. The default
        is set to use `model.tolerance` (default None).
    fva_result : pd.DataFrame, optional
        Precomputed FVA result. If specified, FVA will not be run again, by default
        None.

    Returns
    -------
    List[str]
        List of identifiers of the blocked reactions.
    """
    zero_cutoff = cobra.flux_analysis.helpers.normalize_cutoff(model, zero_cutoff)

    if fva_result is None:
        fva_result = flux_variability_analysis(
            model, loopless=prevent_loops, fraction_of_optimum=0.0
        )

    return fva_result[fva_result.abs().max(axis=1) < zero_cutoff].index.tolist()


def get_candidate_thermodynamic_constraints(
    model: cobra.Model,
    metabolites_namespace: str = None,
    exclude_compartments: List[str] = None,
) -> List[str]:
    """Selects reactions in the flux space that are suitable to be used as thermodynamic
    constraints. By default this method selects all internal reactions, excluding water
    transport all boundary and exchange reactions. Optionally, it can exclude reactions
    where at least one metabolite belongs to certain compartments.

    Parameters
    ----------
    model : Union[FluxSpace, cobra.Model]
        The target model.
    metabolite_interpreter : MetaboliteInterpreter, optional
        Specifies how to parse metabolite identifiers.
    exclude_compartments : List[str], optional
        List of identifiers of the compartment to exclude from the candidates.
    ccache : CompoundCache, optional
        eQuilibrator's :code:`CompoundCache` object, used to identify compounds using
        identifiers from different namespaces. For performance reasons, it is
        recommended to use a single instance of `CompoundCache` for all functions in
        PTA.

    Returns
    -------
    List[str]
        The identifiers of the candidate reactions.
    """
    candidate_ids: List[str] = []
    exclude_compartments = exclude_compartments or list()
    unknown_compounds_found = False
    metanetx = Metanetx()

    for r in model.reactions:
        # Ignore reactions that have no product or no substrate.
        S = np.array(list(r.metabolites.values()))
        is_candidate = not np.all(S >= 0) and not np.all(S <= 0)

        # Ignore potential biomass reactions.
        is_candidate = is_candidate and not "biomass" in r.id.lower()
        is_candidate = is_candidate and not "growth" in r.id.lower()

        # Ignore reactions with metabolites in the excluded compartments.
        is_candidate = is_candidate and all(
            m.compartment not in exclude_compartments for m in r.metabolites
        )

        # Ignore reactions including only H2O and/or protons, as their free energy is
        # fixed to zero.
        metabolite_ids = [
            parse_metabolite_id(m, metabolites_namespace) for m in r.metabolites
        ]
        metabolite_mnx_ids = [metanetx.to_mnx_compound(id, "") for id in metabolite_ids]
        unknown_compounds_found = unknown_compounds_found or any(
            [id == "" for id in metabolite_mnx_ids]
        )
        is_h2o_or_proton = [id in WATER_OR_PROTON_IDS for id in metabolite_mnx_ids]
        is_candidate = is_candidate and not all(is_h2o_or_proton)

        if is_candidate:
            candidate_ids.append(r.id)

    if unknown_compounds_found:
        logger.warning(
            "One or more metabolites were not found in the compound cache. Automated "
            "selection of thermodynamically constrained reactions may be unreliable."
        )
    return candidate_ids


def get_reactions_in_internal_cycles(
    model: cobra.Model, biomass_name: Optional[str] = None, atpm_name: str = "ATPM"
) -> List[str]:
    """Find all the reactions in a model involved in one or more internal cycles.

    Parameters
    ----------
    model : cobra.Model
        The target model.
    biomass_name : Optional[str], optional
        Identifier of the biomass reaction.
    atpm_name : str, optional
        Identifier of the ATP maintenance reaction.

    Returns
    -------
    List[str]
        The identifiers of the reactions involved in internal cycles.
    """
    if biomass_name is None:
        results = model.reactions.query(
            lambda r: "biomass" in r.id.lower() or "growth" in r.id.lower()
        )
        assert len(results) == 1, (
            f"Found {len(results)} candidate biomass "
            "reactions, but need exactly one. Please specify the name of the "
            "biomass reaction."
        )
        biomass_name = results[0].id
    assert model.reactions.has_id(biomass_name), (
        f"Reaction {biomass_name} " "not found in the model"
    )
    assert model.reactions.has_id(atpm_name), (
        f"Reaction {atpm_name} " "not found in the model"
    )

    # Find reactions that can have flux in the model even if the exchanges are
    # set to zero.
    with model as internal_model:
        for reaction in internal_model.boundary:
            reaction.lower_bound = 0
            reaction.upper_bound = 0
        atpm = internal_model.reactions.get_by_id(atpm_name)
        atpm.lower_bound = 0
        atpm.upper_bound = 0
        biomass = internal_model.reactions.get_by_id(biomass_name)
        biomass.lower_bound = 0
        biomass.upper_bound = 0

        try:
            internal_model.remove_reactions(find_blocked_reactions(internal_model))
            return [r.id for r in internal_model.reactions]
        except cobra.exceptions.Infeasible:
            print(
                "prepare_for_pta() requires the model to be feasible when "
                "boundary reactions, ATP maintenance and biomass are set to "
                "zero."
            )
            raise


def get_internal_cycles(
    model: cobra.Model, biomass_name: Optional[str] = None, atpm_name: str = "ATPM"
) -> np.ndarray:
    """Uses :code:`efmtool` to enumerate all the internal cycles in the network.

    model : cobra.Model
        The target model.
    biomass_name : Optional[str], optional
        Identifier of the biomass reaction.
    atpm_name : str, optional
        Identifier of the ATP maintenance reaction.

    Returns
    -------
    np.ndarray
        A n-by-e matrix, where e in the number of EFMs and n is the number of reactions,
        where each column is an EFM representing an internal cycle.
    """
    if biomass_name is None:
        results = model.reactions.query(
            lambda r: "biomass" in r.id.lower() or "growth" in r.id.lower()
        )
        assert len(results) <= 1, (
            f"Found {len(results)} candidate biomass "
            "reactions, but need at most one. Please specify the name of the "
            "biomass reaction."
        )
        if len(results) == 1:
            biomass_name = results[0].id

    internal_model = model.copy()
    for reaction in internal_model.boundary:
        reaction.lower_bound = 0
        reaction.upper_bound = 0
    if model.reactions.has_id(atpm_name):
        atpm = internal_model.reactions.get_by_id(atpm_name)
        atpm.lower_bound = 0
        atpm.upper_bound = 0
    if model.reactions.has_id(biomass_name):
        biomass = internal_model.reactions.get_by_id(biomass_name)
        biomass.lower_bound = 0
        biomass.upper_bound = 0

    # Find reactions that can have flux in the model even if the exchanges are
    # set to zero.
    try:
        internal_model.remove_reactions(
            find_blocked_reactions(internal_model), remove_orphans=True
        )
    except cobra.exceptions.Infeasible:
        print(
            "prepare_for_pta() requires the model to be feasible when "
            "boundary reactions, ATP maintenance and biomass are set to "
            "zero."
        )
        raise

    # If the internal model contains no reaction then there is no cycle and we are done.
    if len(internal_model.reactions) == 0:
        return np.empty((0, 0))

    # First tighten the model bounds to discover all the true reversibilities. Since
    # efmtool assumes irreversibility only in the forward direction we must reverse th
    # reactions that only operate in the backward direction.
    tighten_model_bounds(internal_model)
    S = create_stoichiometric_matrix(internal_model)
    lb = np.array([r.lower_bound for r in internal_model.reactions])
    ub = np.array([r.upper_bound for r in internal_model.reactions])
    to_reverse = ub <= 0
    S[:, to_reverse] *= -1
    lb[to_reverse] *= -1
    is_reversible = [1 if b < 0 else 0 for b in lb]

    efms = efmtool.calculate_efms(
        S,
        is_reversible,
        [r.id for r in internal_model.reactions],
        [m.id for m in internal_model.metabolites],
    )

    # Finally, we map the EFMs to the original model.
    efms[to_reverse, :] = -efms[to_reverse, :]
    cycles = np.zeros((len(model.reactions), efms.shape[1]))
    for i, r in enumerate(internal_model.reactions):
        cycles[model.reactions.index(r.id), :] = efms[i, :]

    return cycles


def to_reactions_idxs(
    reactions: Union[List[int], List[str], cobra.DictList, List[cobra.Reaction]],
    model: cobra.Model,
) -> List[int]:
    """Utility function to obtain a list of reaction indices from different
    representations.

    Parameters
    ----------
    reactions : Union[List[int], List[str], cobra.DictList, List[cobra.Reaction]]
        Input list of reactions. Reactions can be defined through their index in the
        model, their identifiers, or with the reactions themselves.
    model : cobra.Model
        The model in which the reactions are defined.

    Returns
    -------
    List[int]
        List of reaction indices.

    Raises
    ------
    Exception
        If the list is not of one of the expected formats.
    """
    if len(reactions) == 0:
        return []
    if isinstance(reactions, list) and isinstance(reactions[0], int):
        return reactions  # type: ignore
    if isinstance(reactions, list) and isinstance(reactions[0], str):
        return [model.reactions.index(r) for r in reactions]
    if isinstance(reactions, cobra.DictList) or (
        isinstance(reactions, list) and isinstance(reactions[0], cobra.Reaction)
    ):
        return [model.reactions.index(r) for r in reactions]
    raise Exception("Unsupported reaction list format")


def to_reactions_ids(
    reactions: Union[List[int], List[str], cobra.DictList, List[cobra.Reaction]],
    model: cobra.Model,
) -> List[str]:
    """Utility function to obtain a list of reaction identifiers from different
    representations.

    Parameters
    ----------
    reactions : Union[List[int], List[str], cobra.DictList, List[cobra.Reaction]]
        Input list of reactions. Reactions can be defined through their index in the
        model, their identifiers, or with the reactions themselves.
    model : cobra.Model
        The model in which the reactions are defined.

    Returns
    -------
    List[str]
        List of reaction identifiers.

    Raises
    ------
    Exception
        If the list is not of one of the expected formats.
    """
    if len(reactions) == 0:
        return []
    if isinstance(reactions, list) and isinstance(reactions[0], int):
        return [model.reactions[i].id for i in reactions]
    if isinstance(reactions, list) and isinstance(reactions[0], str):
        return reactions  # type: ignore
    if isinstance(reactions, cobra.DictList) or (
        isinstance(reactions, list) and isinstance(reactions[0], cobra.Reaction)
    ):
        return [r.id for r in reactions]
    raise Exception("Unsupported reaction list format")


def apply_transform(
    value: np.ndarray, transform: Tuple[np.ndarray, np.ndarray]
) -> np.ndarray:
    """Applies an affine transform to a matrix.

    Parameters
    ----------
    value : np.ndarray
        The matrix to be transformed.
    transform : Tuple[np.ndarray, np.ndarray]
        Tuple describing the linear (transformation matrix) and affine (translation
        vector) of the transform.

    Returns
    -------
    np.ndarray
        The transformed matrix.
    """
    return transform[0] @ value + transform[1]


def get_path(path: Union[Path, str]) -> Path:
    """Gets a :code:`Path` object from different representations.

    Parameters
    ----------
    path : Union[Path, str]
        A :code:`Path` object or a string describing the path.

    Returns
    -------
    Path
        A :code:`Path` object.

    Raises
    ------
    Exception
        If the type of the input is not supported.
    """
    if isinstance(path, Path):
        return path
    elif isinstance(path, str):
        return Path(path)
    else:
        raise Exception("Unsupported path type")


def covariance_square_root(
    covariance: np.ndarray, min_eigenvalue: float = default_min_eigenvalue_tds_basis
) -> np.ndarray:
    """Gets a full-rank square root of a covariance matrix.

    Parameters
    ----------
    covariance : np.ndarray
        The input covariance matrix.
    min_eigenvalue : float, optional
        Minimum eigenvalue to keep during the truncated EVD.

    Returns
    -------
    np.ndarray
        A full-rank square root of the covariance.
    """

    w, v = la.eigh(covariance)
    assert np.all(np.abs(np.imag(w)) < min_eigenvalue) and np.all(
        np.abs(np.imag(v * np.real(w))) < min_eigenvalue
    ), (
        "The eigenvalue decomposition of the covariance matrix has "
        "imaginary parts larger than the specified minimum eigenvalue."
    )
    assert np.min(w) > -min_eigenvalue, (
        "The covariance matrix has "
        "negative eigenvalues larger than the specified minimum eigenvalue."
    )

    w = np.real(w)
    v = np.real(v)
    selected_dims = w >= min_eigenvalue
    w = w[selected_dims]
    v = v[:, selected_dims]

    return v @ np.diag(np.sqrt(w))


def load_example_model(model_name: str) -> cobra.Model:
    """Load an example SBML model in cobrapy.

    Parameters
    ----------
    model_name : str
        Name of the model file (without extension). This can be any of the models in
        pta/data/models.

    Returns
    -------
    cobra.Model
        The loaded model in cobrapy format.
    """
    file_name = f"data/models/{model_name}.xml"
    if not pkg_resources.resource_exists("pta", file_name):
        logger.warning(f"Model {model_name} does not exist.")
        return None
    else:
        return cobra.io.read_sbml_model(
            pkg_resources.resource_filename("pta", file_name)
        )


def find_rotation_matrix(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Compute a matrix that rotates the vector x onto vector y (without scaling).

    Parameters
    ----------
    x : np.ndarray
        The starting vector.
    y : np.ndarray
        The destination vector.

    Returns
    -------
    np.ndarray
        The computed rotation matrix.
    """
    # pylint: disable=line-too-long
    # Adapted from:
    # https://math.stackexchange.com/questions/598750/finding-the-rotation-matrix-in-n-dimensions
    x = x.flatten()
    y = y.flatten()

    u = x / np.linalg.norm(x)
    v = y - np.dot(u, y) * u
    v = v / np.linalg.norm(v)

    cos_t = np.dot(x, y) / np.linalg.norm(x) / np.linalg.norm(y)
    sin_t = np.sqrt(1 - cos_t**2)

    return (
        np.identity(len(x))
        - np.outer(u, u)
        - np.outer(v, v)
        + np.vstack((u, v)).T
        @ np.array([[cos_t, -sin_t], [sin_t, cos_t]])
        @ np.vstack((u, v))
    )
