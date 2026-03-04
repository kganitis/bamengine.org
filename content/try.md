---
title: Try BAM Engine
---

Use the interactive shell to try BAM Engine in the browser. Type code
and press Shift+Enter to execute.

{{< jupyterlite src="/try/lite/repl/?toolbar=1&kernel=python&code=import%20micropip%0Aawait%20micropip.install%28%27bamengine%27%29%0A%0Aimport%20bamengine%20as%20bam%0A%0Asim%20%3D%20bam.Simulation.init%28seed%3D42%2C%20logging%3D%7B%22default_level%22%3A%20%22ERROR%22%7D%29%0Aresults%20%3D%20sim.run%28n_periods%3D100%2C%20collect%3DTrue%29%0A%0Aavg_price%20%3D%20results.economy_data%5B%22avg_price%22%5D%0Ainflation%20%3D%20results.economy_data%5B%22inflation%22%5D%0A%0Aprint%28f%27Final%20Average%20Market%20Price%20at%20period%20%7Bsim.t%7D%3A%20%7Bavg_price%5B-1%5D%3A.2%7D%27%29" height="700px" >}}

For serious work, [install locally](/install/).
