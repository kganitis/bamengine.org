---
title: Community
description: "Get involved with BAM Engine: report bugs, share feedback, and explore the CATS model family."
---

## Get Involved

Contributions to BAM Engine are welcome. Bug fixes, documentation, tests,
performance work, and new extensions are all appreciated. For substantial
or model-behavior changes, please
[open an issue](https://github.com/kganitis/bam-engine/issues) first to
discuss the approach. See the
[contributing guide](https://github.com/kganitis/bam-engine/blob/main/CONTRIBUTING.md)
for the full guidelines and quality bar.

You can also participate without writing code:

- **Bug reports & feature requests**: found a bug or have an idea?
  Open an issue on the [issue tracker](https://github.com/kganitis/bam-engine/issues)
- **Documentation feedback**: spotted an error, unclear explanation,
  or missing topic? Let us know via an
  [issue](https://github.com/kganitis/bam-engine/issues)
- **Testing & reporting**: try the framework, run simulations, and
  report any unexpected behavior
- **Questions & discussions**: ask questions or start a discussion on
  [GitHub Discussions](https://github.com/kganitis/bam-engine/discussions)
- **Spread the word**: star the
  [repository](https://github.com/kganitis/bam-engine) or share the
  project with colleagues

**Source code:** [github.com/kganitis/bam-engine](https://github.com/kganitis/bam-engine)
| **Citing BAM Engine:** [How to cite](/cite/) BAM Engine in your research

## Related Projects: The CATS Family

The BAM (Bottom-Up Adaptive Macroeconomics) model from Delli Gatti et al.
(2011) has inspired several implementations and extensions within the CATS
(Complex Adaptive Trivial Systems) lineage.

### BAMmodel (NetLogo)

A NetLogo implementation of the BAM model, and the first publicly
documented implementation available. Developed by Platas-López et al.
using the ODD (Overview, Design concepts, and Details) protocol for
standardized model description. The model reproduces the three core agent
types (households, firms, banks) interacting in three markets (labor,
credit, goods) and validates against stylized facts including unemployment
around 10%, inflation in the 1–6% range, and positively skewed wealth
distributions. The authors also explore shock sensitivity and the effect
of varying market sizes on emergent dynamics.

- **Citation:** Platas-López, A., Guerra-Hernández, A., Cecconi, F.,
  Paolucci, M., & Grimaldo, F. (2019). Micro-Foundations of
  Macroeconomic Dynamics: The Agent-Based BAM Model. Pages 319–328.
  DOI: [10.3233/FAIA190141](https://doi.org/10.3233/FAIA190141)
- **Repository:**
  [github.com/alexplatasl/BAMmodel](https://github.com/alexplatasl/BAMmodel)

### ABCredit (Julia)

A Julia implementation of the CC-MABM (Macroeconomic Agent-Based Model
with Capital and Credit), developed at the Banca d'Italia (Bank of Italy).
CC-MABM extends the BAM model with a two-sector supply chain: upstream
K-firms produce capital goods that downstream C-firms use for production.
This adds investment decisions, capital depreciation, and explicit financial
frictions to the original BAM framework. A key finding is that both capital
accumulation *and* credit mechanisms are necessary for endogenous crisis
emergence; neither alone is sufficient. The two-way feedback between the
capital-goods and consumption-goods sectors generates realistic business
cycle dynamics.

- **Citation:** Assenza, T., Delli Gatti, D., & Grazzini, J. (2015).
  Emergent dynamics of a macroeconomic agent based model with capital and
  credit. *Journal of Economic Dynamics and Control*, 50, 5–28.
  DOI: [10.1016/j.jedc.2014.07.001](https://doi.org/10.1016/j.jedc.2014.07.001)
- **Repository:**
  [github.com/bancaditalia/ABCredit.jl](https://github.com/bancaditalia/ABCredit.jl)

### R-MABM (Python + Julia)

A multi-agent reinforcement-learning extension of ABCredit, written in
Python with Julia interoperability via `juliacall`. R-MABM replaces the
heuristic decision rules of C-firms with tabular Q-learning agents that
operate over discrete state and action spaces. The RL agents discover
three emergent strategies depending on the level of market competition:
market power exploitation, dumping (aggressive price-cutting), and perfect
competition. Agents with independent policies spontaneously segregate into
distinct strategic groups. A notable macro-level result is that only the
perfect-competition strategy stabilizes the economy as a whole.

- **Citation:** Brusatin, S., Padoan, T., Coletta, A., Delli Gatti, D., &
  Glielmo, A. (2024). Simulating the Economic Impact of Rationality
  through Reinforcement Learning and Agent-Based Modelling. *ICAIF '24*,
  159–167.
  DOI: [10.1145/3677052.3698621](https://doi.org/10.1145/3677052.3698621)
- **Repository:**
  [github.com/Brusa99/R-MABM](https://github.com/Brusa99/R-MABM)

## Other ABM Frameworks

- [Mesa](https://github.com/projectmesa/mesa): General-purpose ABM in Python
- [AgentPy](https://github.com/JoelForamitti/agentpy): Agent-based modeling in Python
