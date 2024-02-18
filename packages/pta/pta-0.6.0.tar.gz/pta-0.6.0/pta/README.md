# Probabilistic Thermodynamic Analysis of metabolic networks.

Probabilistic Thermodynamic Analysis (PTA) is a framework for the exploration of
the thermodynamic properties of a metabolic network. In PTA, we consider the 
*steady-state thermodynamic space* of a network, that is, the space of standard reaction 
energies and metabolite concentrations that are compatible with steady state
flux constraints. The uncertainty of the variables in the thermodynamic space is 
modeled with a probability distribution, allowing analysis with optimization and
sampling approaches:
- **Probabilistic Metabolic Optimization (PMO)** aims at finding the most probable 
values of reaction energies and metabolite concentrations that are compatible 
with the steady state constrain. This method is particularly useful to identify
features of the network that are thermodynamically unrealistic. For example, PMO
can identify substrate channeling, incorrect cofactors or inaccurate 
directionalities.
- **Thermodynamic and Flux Sampling (TFS)** allows to sample the 
thermodynamic and flux spaces of a network. The method provides estimates of 
metabolite concentrations, reactions directions, and flux distributions.

## Installation and usage

Please see the online [documentation](https://probabilistic-thermodynamic-analysis.readthedocs.io/en/latest/).

## Cite us

If you use PTA in a scientific publication, please cite our paper:

Gollub, M.G., Kaltenbach, H.M., Stelling, J., 2021. "Probabilistic Thermodynamic 
Analysis of Metabolic Networks". *Bioinformatics*. - 
[DOI](https://doi.org/10.1093/bioinformatics/btab194)
