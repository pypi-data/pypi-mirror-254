# Probabilistic Thermodynamic Analysis of Metabolic Networks
[![Join the chat at https://gitter.im/CSB-ETHZ/PTA](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/CSB-ETHZ/PTA?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Documentation Status](https://readthedocs.org/projects/probabilistic-thermodynamic-analysis/badge/?version=latest)](https://probabilistic-thermodynamic-analysis.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/pta.svg)](https://badge.fury.io/py/pta)

Probabilistic Thermodynamic Analysis (PTA) is a framework for the exploration of
the thermodynamic properties of a metabolic network. In PTA, we consider the 
*thermodynamic space* of a network, that is, the space of standard reaction 
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
- **Thermodynamic and Flux Sampling (TFS)** allows to jointly sample the 
thermodynamic and flux spaces of a network. The method provides estimates of 
metabolite concentrations, reactions directions, and flux distributions.

## Installation

PTA is available as a Python package on the [Python Package
Index](https://pypi.org/project/pta/), see the
[documentation](https://probabilistic-thermodynamic-analysis.readthedocs.io/en/latest/getting_started.html)
for the installation instructions.

The MATLAB interface is now deprecated and not maintained anymore. It can still be found
in the [MATLAB branch](https://gitlab.com/csb.ethz/pta/-/tree/MATLAB ) and can be used
to reproduce the analysis presented in the PTA publication [[1](#references)]. See the
[README file](https://gitlab.com/csb.ethz/pta/-/blob/MATLAB/README.md) for installation
and usage instructions.

## Cite us

If you use PTA in a scientific publication, please cite our paper: 

Gollub, M.G., Kaltenbach, H.M., Stelling, J., 2021. "Probabilistic Thermodynamic 
Analysis of Metabolic Networks". *Bioinformatics*. - 
[DOI](https://doi.org/10.1093/bioinformatics/btab194)

## References

1. Gollub, M.G., Kaltenbach, H.M., Stelling, J., 2021. "Probabilistic Thermodynamic 
Analysis of Metabolic Networks". *Bioinformatics*.
2. Gerosa, L., van Rijsewijk, B.R.H., Christodoulou, D., Kochanowski, K., Schmidt, T.S., Noor, E. and Sauer, U., 2015. Pseudo-transition analysis identifies the key regulators of dynamic metabolic adaptations from steady-state data. *Cell systems*, 1(4), pp.270-282.
