---
title: "Buffer-Stock Consumption"
---

The buffer-stock extension (section 3.9.4) replaces the baseline mean-field
MPC with an individual adaptive rule based on buffer-stock saving theory.

![Buffer-stock wealth CCDF](/images/gallery-buffer-stock-1.png)

*Complementary CDF of household wealth on log-log axes, fitted against
Singh-Maddala, Dagum, and GB2 distributions (Figure 3.8).*

**Run this yourself:**

```python
import bamengine as bam
from extensions.rnd import RND
from extensions.buffer_stock import BUFFER_STOCK

sim = bam.Simulation.init(seed=42)
sim.use(RND)
sim.use(BUFFER_STOCK)
results = sim.run(n_periods=1000, show=True)
```

See the [full example](https://bam-engine.readthedocs.io/en/latest/auto_examples/extensions/example_buffer_stock.html).
