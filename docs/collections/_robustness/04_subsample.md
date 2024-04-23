---
layout: post
title:  "Improving Robustness by Means of Data Optimization"
date:   2024-04-23 10:00:00 +0100
published: false
---

Finally, an analysis of camera data from in-vehicle and infrastructure sensors (cameras) and perception pipelines gave valuable insights into what parts of data are actually required to be exchanged for cooperative perception purposes:
Efficient in-vehicle perception is often performed on Regions of Interest (RoIs), smaller parts of an image that hold information that is of particular importance for autonomous driving (AD) applications.
Hence, if in-vehicle data is shared with other nodes (vehicles, remote operator, ...) it should be sufficient to share such RoIs in full resolution while scaling down fidelity of less important parts of the sample.
For static infrastructure-mounted (camera) sensors it become apparent, that typically only parts of an frame change, as typically on a selection of traffic participants is actually moving.
Therefore, only transmitting incremental updates would suffice for giving receivers a complete picture of their surroundings.
Both mechanisms can significantly decrease the size of samples exchanged wirelessly.
W2RP (and its extensions) have been extended to support the reliable exchange of such data, despite their dynamic data profiles that has not been supported by the underlying DDS/RTPS middleware.
Experimental evaluations validated the assumed advantages and showed improved robustness to higher error rates.