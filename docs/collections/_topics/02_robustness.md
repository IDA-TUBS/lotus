---
layout: topic
title: Enhanced Robustness
topic: robustness
published: true
---

W2RP was further developed in multiple directions, focused on improving robustness under various scenarios and channel conditions.
First works always assumed the sample period and sample deadline to be equal (100ms).
However, modern (camera) sensors enable higher sampling rates, while the application constraints (deadline) remain unchanged.
This leads to deadlines larger than sampling periods resulting in potentially overlapping sample transmission and error correction of multiple frames. 
W2RP has been extended to allow for exploitation of those overlapping sample transmission for handling occasional burst errors (E-W2RP).

Unicast data dissemination in cooperative perception and similar applications is inefficient as it can be expected that data may be needed by multiple vehicles.
Hence, W2RP has been extended to support multicast resulting in WiMEP.
As errors can be individual per receiver, efficient backward error correction (BEC) is a challenging task.
For this purpose, WiMEP supports bundling of BEC for receivers with similar error patterns and offers means to prioritize receivers based on arbitrary conditions.
WiMEP's effectiveness has been demonstrated both in simulation as well as under real-world conditions using the IDA's wireless demonstrator setup.

Additionally, W2RP has been extended by means of a decentralized parameter selection to improve effectiveness in shared channels.

<!-- Finally, an analysis of camera data from in-vehicle and infrastructure sensors (cameras) and perception pipelines gave valuable insights into what parts of data are actually required to be exchanged for cooperative perception purposes:
Efficient in-vehicle perception is often performed on Regions of Interest (RoIs), smaller parts of an image that hold information that is of particular importance for autonomous driving (AD) applications.
Hence, if in-vehicle data is shared with other nodes (vehicles, remote operator, ...) it should be sufficient to share such RoIs in full resolution while scaling down fidelity of less important parts of the sample.
For static infrastructure-mounted (camera) sensors it become apparent, that typically only parts of an frame change, as typically on a selection of traffic participants is actually moving.
Therefore, only transmitting incremental updates would suffice for giving receivers a complete picture of their surroundings.
Both mechanisms can significantly decrease the size of samples exchanged wirelessly.
W2RP (and its extensions) have been extended to support the reliable exchange of such data, despite their dynamic data profiles that has not been supported by the underlying DDS/RTPS middleware.
Experimental evaluations validated the assumed advantages and showed improved robustness to higher error rates. -->