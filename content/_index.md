---
title: BAM Engine
description: "BAM Engine: a Python framework for agent-based macroeconomic simulation using the BAM model."
---

## What is BAM Engine?

Imagine a virtual economy where thousands of workers look for jobs,
companies compete for customers, and banks decide who gets a loan.
BAM Engine creates exactly that: a computer simulation where economic
patterns like unemployment, inflation, and business cycles emerge
naturally from these individual decisions, just as they do in the real
world. It is a Python framework that implements the BAM model from
[*Macroeconomics from the Bottom-up*](https://doi.org/10.1007/978-88-470-1971-3)
(Delli Gatti et al., 2011), designed for researchers in computational
economics and agent-based modeling.

{{< grid columns="1 2 2 3" >}}

[[item]]
type = 'card'
title = 'Complete BAM Model'
body = '''
Full implementation of the BAM model from Delli Gatti et al. (2011).
Firms, households, and banks interact across labor, credit, and goods markets.
Macroeconomic dynamics emerge from the bottom up.
'''

[[item]]
type = 'card'
title = 'ECS Architecture'
body = '''
Entity-Component-System design separates agent data (Roles) from behavior
(Events). Extend or override any aspect of the model without forking the core.
'''

[[item]]
type = 'card'
title = 'Vectorized Performance'
body = '''
All agent operations use NumPy arrays, with no Python loops over agents.
Simulate economies of 100+ firms and 500+ households at interactive speed.
'''

[[item]]
type = 'card'
title = 'Built-in Extensions'
body = '''
Activate R&D/Growth+, buffer-stock consumption, or taxation with a single
`sim.use(EXTENSION)` call. Extensible design for custom model components.
'''

[[item]]
type = 'card'
title = 'Validation Framework'
body = '''
Three scenario validators check unemployment, inflation, and firm-size
distributions against stylized facts. Robustness analysis and sensitivity
sweeps are built in.
'''

[[item]]
type = 'card'
title = 'Calibration Pipeline'
body = '''
Morris screening, grid search, and tiered stability testing, all accessible
from the same high-level API. Reproducible parameter estimation out of the box.
'''

{{< /grid >}}

<p align="center">
  <a href="/benchmarks/validation/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="/images/validation-card-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="/images/validation-card-light.svg">
      <img alt="Model Validation" src="/images/validation-card-light.svg" width="476">
    </picture>
  </a>
</p>

