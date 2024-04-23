---
layout: topic
title: Continuous Connectivity 
topic: handover
published: true
---

Handover situations, such as present in infrastructure-supported cooperative perception use cases such as automated valet parking (AVP) or camera-equipped intersections, are especially taxing with respect to enable reliable and timely data exchange.
The mobile nature of vehicles inherently leads to the need for roaming across multiple access points (APs), as shadowing by stationary (e.g., walls, vegetation, ...) and dynamic (e.g., other vehicles, ...) obstacles will occur frequently, especially in case high-data rate technologies are used.
This is already the case if small messages are exchanged, and becomes even more challenging if large object data streams with stringent real-time and reliability constraints are considered.
Nevertheless, reliable and continuous sample exchange needs to be ensured in order to enable the corresponding use cases.

For this purpose a continuous connectivity approach has been developed.
It utilizes multi-connectivity (cf. cell-free architecture) and wireless link monitoring in combination with low-latency TSN-backbone network reconfiguration to enable fast switching between object streams routes to a different APs that still maintains a good connection to the vehicle requiring the data.
As the backbone network has a fixed topology, safe alternative routes can be determined in advance, thereby taking this route determination out of the critical path.
Consequently, the reconfiguration time is bounded from above by the deterministic connection loss detection and switching of routes.
Experimental results showed enabling continuous and reliable sample exchange in handover scenarios as stream interruption are minimal.