---
title: "Growth+ Extension"
---

The Growth+ extension adds R&D investment and endogenous productivity growth
to the baseline model (chapter 3.8).

![Growth+ macro dynamics](/images/gallery-growth-plus-1.png)

*Time series with recession bands (GDP, unemployment, inflation,
productivity-wage ratio), Phillips, Okun, and Beveridge curves, and firm
size distribution.*

![Growth+ financial dynamics](/images/gallery-growth-plus-2.png)

*Output and net-worth growth rate distributions, real interest rate,
bankruptcies, financial fragility, price-clearing ratio, price dispersion,
and equity-sales dispersion.*

**Run this yourself:**

```python
import bamengine as bam
from extensions.rnd import RND

sim = bam.Simulation.init(seed=42)
sim.use(RND)
results = sim.run(n_periods=1000, show=True)
```

See the [full example](https://bam-engine.readthedocs.io/en/latest/auto_examples/extensions/example_growth_plus.html).
