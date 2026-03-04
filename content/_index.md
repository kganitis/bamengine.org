---
title: BAM Engine
---

## Why BAM Engine?

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
All agent operations use NumPy arrays — no Python loops over agents.
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
Morris screening, grid search, and tiered stability testing — all accessible
from the same high-level API. Reproducible parameter estimation out of the box.
'''

{{< /grid >}}

## Quick Start

```bash
pip install bamengine
```

```python
import bamengine as bam

sim = bam.Simulation.init(n_firms=100, n_households=500, seed=42)
results = sim.run(n_periods=100, collect=True)
```

{{< blog >}}
