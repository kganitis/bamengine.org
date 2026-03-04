---
title: "Growth+ Extension"
---

The Growth+ extension adds R&D investment, technology adoption, and
productivity growth to the baseline model.

![Growth+ scenario output](/images/gallery-growth-plus.png)

*Aggregate output grows as firms accumulate technology through R&D.*

**Enable Growth+ in one line:**

```python
from extensions.rnd import RND
sim = bam.Simulation.init(seed=42)
sim.use(RND)
results = sim.run(n_periods=1000, collect=True)
```

See the [full example](https://bam-engine.readthedocs.io/en/latest/auto_examples/extensions/example_growth_plus.html).
