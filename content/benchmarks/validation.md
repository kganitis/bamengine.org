---
title: Validation Dashboard
description: "Validation dashboard — accuracy and stability metrics across scenarios and releases."
url: /benchmarks/validation/
green_score_threshold: 0.85
yellow_score_threshold: 0.80
green_pass_threshold: 0.97
yellow_pass_threshold: 0.96
---

The validation dashboard tracks two complementary metrics across releases:

- **Accuracy** (0–1) — how closely simulation results match calibration targets
  from the original BAM model (Delli Gatti et al., 2011). Higher is better.
- **Stability** (%) — how consistently random seeds produce valid results.
  A seed "passes" when all its metric scores exceed the tolerance threshold.

Card border colors reflect the **accuracy**:

- **Green**: accuracy ≥ 0.85
- **Yellow**: accuracy 0.80–0.85 — marginal
- **Red**: accuracy < 0.80 — regression

Stability is shown inline with its own coloring (green ≥ 97%, yellow ≥ 96%).

Click a scenario card to drill down into per-metric charts. Click any chart to
expand it.

{{< validation-dashboard >}}
