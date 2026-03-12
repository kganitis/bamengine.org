---
title: Seed Stability
---

The stability dashboard tracks seed-level validation pass rates across commits
for all three scenarios (Baseline, Growth+, Buffer-Stock). Each benchmark runs
1000 seeds with 10 parallel workers and reports per-metric statistics.

- **Green**: pass rate >= 95% (target)
- **Yellow**: pass rate 90-95% (marginal)
- **Red**: pass rate < 90% (regression)

Click a scenario card to drill down into per-metric charts. Click any chart to expand it.

{{< stability-dashboard >}}