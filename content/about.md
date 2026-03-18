---
title: About
description: "History, academic context, and acknowledgments for the BAM Engine project."
---

BAM Engine is a high-performance Python implementation of the BAM
(Bottom-Up Adaptive Macroeconomics) model from
*[Macroeconomics from the Bottom-up](https://doi.org/10.1007/978-88-470-1971-3)*
(Delli Gatti et al., 2011). It simulates three agent types (households,
firms, and banks) interacting across labor, credit, and consumption goods
markets. Macroeconomic dynamics emerge entirely from individual agent
decisions.

## History

BAM Engine began as an MSc thesis at the Department of Informatics,
University of Piraeus, Greece, with the goal of producing a modern,
extensible Python implementation of the BAM model.

Development started in late 2024. The initial release (v0.1.0) delivered
the complete core model with an Entity-Component-System architecture,
vectorized NumPy operations, and YAML-configurable event pipelines.
Subsequent releases added validation and calibration frameworks (v0.2.0),
the buffer-stock consumption extension (v0.3.0), robustness analysis and
a rebuilt calibration pipeline (v0.4.0), and the Extension bundle system
with `sim.use()` (v0.5.0). Version 0.6.0 consolidated market-matching
logic into vectorized operations, delivering a ~30% performance
improvement. Version 0.7.0 replaced the batch-sequential goods market
with a pure sequential implementation, eliminating inventory collisions
and improving simulation speed by another 6.5%.

## Academic Context

| | |
|---|---|
| **Thesis** | Design and Implementation of a Modular Python Framework for Agent-Based Macroeconomic Simulations |
| **Author** | Konstantinos Ganitis |
| **Supervisor** | Dionysios Sotiropoulos |
| **Department** | Department of Informatics, University of Piraeus, Greece |
| **Degree** | MSc in Informatics |

If you use BAM Engine in your research, see [Citing BAM Engine](/cite/)
for citation information and BibTeX entries.

## License

BAM Engine is distributed under the [MIT License](https://opensource.org/licenses/MIT).
Copyright © 2026 Konstantinos Ganitis. See the full
[LICENSE](https://github.com/kganitis/bam-engine/blob/main/LICENSE) file
for details.

## Acknowledgments

BAM Engine would not exist without the foundational work of the original BAM
model authors:

- Domenico Delli Gatti
- Saul Desiderio
- Edoardo Gaffeo
- Pasquale Cirillo
- Mauro Gallegati

The project was developed at the **Department of Informatics, University of
Piraeus, Greece**.

BAM Engine is built on the Python scientific computing ecosystem, with
particular reliance on [NumPy](https://numpy.org/),
[SciPy](https://scipy.org/), [pandas](https://pandas.pydata.org/), and
[Matplotlib](https://matplotlib.org/). Documentation is powered by
[Sphinx](https://www.sphinx-doc.org/) with the
[PyData theme](https://pydata-sphinx-theme.readthedocs.io/). Testing uses
[pytest](https://docs.pytest.org/) and
[Hypothesis](https://hypothesis.readthedocs.io/).
