---
layout: post
title: "Continuous Multi-Access Communication for Large Object Streams"
date:   2024-04-24 14:00 +0100
published: true
---

To address the issues of traditional handover mechanisms and enable continuous connectivity for applications streaming large data objects a continuous connectivity approach has been developed.<!--end_excerpt--> The proposed approach is based upon the concept of multi-connectivity (cf. cell-free architecture) resulting in a node always being connected to multiple access points at the same time. So far, multi-connectivity for reliability purposes is primarily used to offer additional error protection for small timing- and safety-critical messages (cf. URLLC and wireless TSN) by means of redundant data transmissions via multiple paths. hence, if one path is blocked or connection to an access point is lost in a situations that would have traditionally resulted in a handover, reliable message exchange is made possible. For large object streams, however, such redundant transmissions become impractical as wireless channel bandwidth is already limited. Traditional handovers mechanisms introduce non-negligible connectivity interruptions, that may result in deadline violations. Consequently, novel solutions that specifically ensure continuous data exchange for large object streams are necessary.

<div style="text-align: center;">
<figure>
<img src="{{site.baseurl}}/handover/figures/segment_coordination_intersection.png" alt="Figure 1: Example of a TSN network that connects edge devices (e.g., cameras) and access points to allow for streaming of data to wirelessly connected nodes." style="zoom:15%;" />
<figcaption>Figure 1: Example of a node with two applications. The lower plot visualizes the budget usage of the node. After scheduling the periodic parts there is spare budget (shared slack) available for applications to use in case BEC needs increase dynamically.</figcaption>
</figure>
</div>
The proposed continuous connectivity approach is based on two principles: A heartbeat-based connection monitoring and low-latency backbone network reconfigurations.
In general, user-centric clustering is used to determine the set of access point a node is shall connect with. Data exchange is then only started using a single link. However, the node periodically sends heartbeat messages via all available links to the RM. This allows the RM to determine which links are usable for data exchange. If the link currently used for data exchange is degraded to a unacceptable degree a) connection loss is detected quickly, and more importantly, in a deterministic manner and b) the RM can quickly switch paths of data packets to be routed via a different access point in the node's cluster of connected access points. As a result the reconfiguration procedure is reduced to a  low-latency (single-digit milliseconds cf. [ref](https://doi.org/10.1016/j.sysarc.2021.102208)) reconfiguration of the backbone network (cf. Figure 2).  Consequently, data exchange interruptions are minimized enabling reliable sample exchange even such handover-like scenarios.

<div style="text-align: center;">
<figure>
<img src="{{site.baseurl}}/handover/figures/HO_Timing_Continuous.png" alt="Figure 2: Timing and sample transmission during the continuous connectivity approach. Compared to classic handover approaches, the timing of both the loss detection (heartbeat-based monitor) and the backbone reconfiguration can be bound from above, resulting in deterministic behavior." style="zoom:15%;" />
<figcaption>Figure 2: Timing and sample transmission during the continuous connectivity approach. Compared to classic handover approaches, the timing of both the loss detection (heartbeat-based monitor) and the backbone reconfiguration can be bound from above, resulting in deterministic behavior.</figcaption>
</figure>
</div>


Experimental results showed the continuous connectivity approach enabling continuous and reliable sample exchange in handover scenarios as stream interruptions are minimal. For more details we refer the reader to the [paper]().