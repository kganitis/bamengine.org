---
title: "Baseline Scenario"
---

The baseline scenario runs the core BAM model without extensions,
reproducing key stylized facts from Chapter 3 of Delli Gatti et al. (2011).

![Baseline scenario output](/images/gallery-baseline.png)

*8-panel macro dashboard: GDP, unemployment, price index, wages, firm
profits, bank equity, interest rates, and firm size distribution.*

**Run this yourself:**

```python
import bamengine as bam
sim = bam.Simulation.init(seed=42)
results = sim.run(n_periods=1000, collect=True)
```

See the [full example](https://bam-engine.readthedocs.io/en/latest/auto_examples/basic/example_baseline_scenario.html).
