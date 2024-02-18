"""Create a simple toy network with four phosphohexose species (g6p, f6p, g1p, f1p)."""

import os

import cobra

PHOSPHOHEXOSES_MODEL_PATH = os.path.join(
    os.path.dirname(__file__), "..", "pta", "data", "models", "phosphohexoses.xml"
)

if __name__ == "__main__":
    model = cobra.Model("test_model")

    g6p_c = cobra.Metabolite(
        "g6p_c",
        formula="C6H11O9P",
        name="glucose-6-phosphate",
        compartment="c",
        charge=-2,
    )
    f6p_c = cobra.Metabolite(
        "f6p_c",
        formula="C6H11O9P",
        name="fructose-6-phosphate",
        compartment="c",
        charge=-2,
    )
    g1p_c = cobra.Metabolite(
        "g1p_c",
        formula="C6H11O9P",
        name="glucose-1-phosphate",
        compartment="c",
        charge=-2,
    )
    f1p_c = cobra.Metabolite(
        "f1p_c",
        formula="C6H11O9P",
        name="fructose-1-phosphate",
        compartment="c",
        charge=-2,
    )

    A = cobra.Reaction("A", lower_bound=-1000.0, upper_bound=1000.0)
    B = cobra.Reaction("B", lower_bound=-1000.0, upper_bound=1000.0)
    C = cobra.Reaction("C", lower_bound=-1000.0, upper_bound=1000.0)
    D = cobra.Reaction("D", lower_bound=-1000.0, upper_bound=1000.0)
    E = cobra.Reaction("E", lower_bound=-1000.0, upper_bound=1000.0)
    EX_g6p = cobra.Reaction("EX_g6p", lower_bound=-1000.0, upper_bound=1000.0)
    EX_f1p = cobra.Reaction("EX_f1p", lower_bound=-1000.0, upper_bound=1000.0)
    A.add_metabolites({g6p_c: -1.0, g1p_c: 1.0})
    B.add_metabolites({g1p_c: -1.0, f1p_c: 1.0})
    C.add_metabolites({f1p_c: -1.0, f6p_c: 1.0})
    D.add_metabolites({f6p_c: -1.0, g6p_c: 1.0})
    E.add_metabolites({g1p_c: -1.0, f6p_c: 1.0})
    EX_g6p.add_metabolites({g6p_c: -1.0})
    EX_f1p.add_metabolites({f1p_c: -1.0})

    model.add_reaction(A)
    model.add_reaction(B)
    model.add_reaction(C)
    model.add_reaction(D)
    model.add_reaction(E)
    model.add_reaction(EX_g6p)
    model.add_reaction(EX_f1p)

    cobra.io.write_sbml_model(model, PHOSPHOHEXOSES_MODEL_PATH)
