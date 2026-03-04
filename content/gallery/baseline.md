---
title: "Baseline Scenario"
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
results = sim.run(n_periods=1000, show=True)
```

See the [full example](https://bam-engine.readthedocs.io/en/latest/auto_examples/basic/example_baseline_scenario.html).
