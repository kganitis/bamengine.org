---
title: Installation
---

## Requirements

- Python 3.11 or later
- NumPy >= 1.26 (installed automatically)
- PyYAML >= 6.0.2 (installed automatically)

## Install with pip

```bash
pip install bamengine
```

### Optional extras

```bash
pip install bamengine[pandas]       # DataFrame export
pip install bamengine[viz]          # Matplotlib plotting
pip install bamengine[validation]   # Validation framework
pip install bamengine[extensions]   # All extensions
pip install bamengine[dev]          # Development dependencies
```

## Install from source

```bash
git clone https://github.com/kganitis/bam-engine.git
cd bam-engine
pip install -e ".[dev]"
```

## Verify

```python
import bamengine as bam
print(bam.__version__)
```
