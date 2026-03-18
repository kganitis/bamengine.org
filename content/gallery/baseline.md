---
title: "Baseline Scenario"
description: "Baseline scenario output: GDP, unemployment, inflation, and stylized facts from default parameters."
weight: 1
---

The baseline scenario reproduces section 3.9.1 of Delli Gatti et al. (2011)
with default parameters.

![Baseline scenario output](/images/gallery-baseline.png)

*Eight panels: Real GDP, unemployment rate, inflation, productivity vs real
wage, Phillips curve, Okun curve, Beveridge curve, and firm size distribution.*

**Run this yourself:**

```python
import bamengine as bam

sim = bam.Simulation.init()
results = sim.run(n_periods=1000, collect=True)
```

See the [full example](https://bam-engine.readthedocs.io/en/latest/auto_examples/basic/example_baseline_scenario.html).
