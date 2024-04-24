---
layout: post
title: Continuous multi-access communication
date:   2023-24-04 11:00 +0100
published: true
---

To address the issues of traditional handover mechanisms, a continuous connectivity approach has been developed. It utilizes multi-connectivity (cf. cell-free architecture) and wireless link monitoring in combination with low-latency TSN-backbone network reconfiguration to enable fast switching between object streams routes to a different APs that still maintains a good connection to the vehicle requiring the data. As the backbone network has a fixed topology, safe alternative routes can be determined in advance, thereby taking this route determination out of the critical path. Consequently, the reconfiguration time is bounded from above by the deterministic connection loss detection and switching of routes. Experimental results showed enabling continuous and reliable sample exchange in handover scenarios as stream interruption are minimal.

...