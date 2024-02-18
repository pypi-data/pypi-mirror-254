"""Unit tests for PTA's model assessment functions."""
import cobra
import pta

cobra_config = cobra.Configuration()
cobra_config.processes = 1


def test_structural_assessment(e_coli_core: cobra.Model):
    """Verify that structural assessment correctly finds forced internal cycles."""
    e_coli_core.reactions.BIOMASS_Ecoli_core_w_GAM.lower_bound = 0.5
    assessment = pta.StructuralAssessment(e_coli_core)
    assert len(assessment.forced_internal_cycles) == 1


def test_structural_assessment_no_cycles(e_coli_core: cobra.Model):
    """Verify that structural assessment correctly finds the absence of forced internal
    cycles."""
    e_coli_core.reactions.BIOMASS_Ecoli_core_w_GAM.lower_bound = 0.5
    e_coli_core.remove_reactions([e_coli_core.reactions.get_by_id("SUCDi")])
    assessment = pta.StructuralAssessment(e_coli_core)
    assert len(assessment.forced_internal_cycles) == 0
