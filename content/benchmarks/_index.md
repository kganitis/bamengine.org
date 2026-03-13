---
title: Benchmarks
---

## [Validation Dashboard](/benchmarks/validation/)

Track accuracy and seed stability across releases. Per-metric charts
show how closely simulation results match calibration targets and how
consistently random seeds produce valid outcomes.

## [Benchmark List](/benchmarks/list/)

Flat table of all validation metrics across scenarios. Sortable by score,
stability, or weight — filterable by scenario and metric group.

## [Regressions](/benchmarks/regressions/)

All detected accuracy regressions across releases. Filterable by scenario,
metric group, and severity threshold.

## Performance (ASV)

Performance benchmarks tracked with
[ASV (Airspeed Velocity)](https://asv.readthedocs.io/).

View the [latest benchmark results](https://kganitis.github.io/bam-engine/).

### What is Benchmarked

- Baseline simulation throughput (periods/second)
- Economy scaling (100–500 firms)
- Extension overhead (Growth+, Buffer-Stock, Taxation)

### Running Locally

```bash
git clone https://github.com/kganitis/bam-engine.git
cd bam-engine/asv_benchmarks
asv run
asv publish
asv preview
```

