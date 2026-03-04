---
title: Try BAM Engine
---

Run BAM Engine simulations interactively without installing anything.
The console below uses [JupyterLite](https://jupyterlite.readthedocs.io/)
with [Pyodide](https://pyodide.org/) to run Python entirely in your browser.

{{< jupyterlite src="/try/repl/?toolbar=1&kernel=python&code=import%20micropip%0Aawait%20micropip.install('bamengine')%0A%0Aimport%20bamengine%20as%20bam%0Asim%20%3D%20bam.Simulation.init(seed%3D42)%0Aresults%20%3D%20sim.run(n_periods%3D100%2C%20collect%3DTrue)%0Aprint(f'Unemployment%3A%20%7Bsim.ec.unemp_rate_history%5B-1%5D%3A.2%25%7D')" height="650px" >}}

{{< admonition note >}}
The first load installs the `bamengine` package via `micropip` inside the
browser — this takes 10–20 seconds. Subsequent loads are faster.
{{< /admonition >}}

For serious work, [install locally](/install/).
