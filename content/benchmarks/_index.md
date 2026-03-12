---
title: Benchmarks
---

Performance benchmarks tracked with
[ASV (Airspeed Velocity)](https://asv.readthedocs.io/).

View the [latest benchmark results](https://kganitis.github.io/bam-engine/).

## What is Benchmarked

- Baseline simulation throughput (periods/second)
- Economy scaling (100–500 firms)
- Extension overhead (Growth+, Buffer-Stock, Taxation)

## Running Locally

```bash
git clone https://github.com/kganitis/bam-engine.git
cd bam-engine/asv_benchmarks
asv run
asv publish
asv preview
```
