---
layout: post
title:  "Application-centric Resource Management"
date:   2023-01-24 9:00:00 +0100
published: true
---

A centralized application-centric Resource Management (RM) approach that is based on Software Defined Networking (SDN) principles (communication divided into control and data plane) has been proposed to address the coordination of various wireless applications. Specifically, a hierarchical architecture is employed that allows for coordination across network segments.

The RM takes into account both application requirements and constraints as well as network properties. This is achieved by splitting the functionality into an application layer RM (aRM) and network layer RM (nRM). Thereby, the former is responsible for coordinating data exchange on an application level whereas the latter takes control of network components. Consequently, application requests are first handled by the aRM, which in turn coordinates all actions with the nRM through the shared aRM_nRM interface. This ensures that application requests and subsequent actions are in line with the underlying networks requirements and its capabilities. 

<div style="text-align: center;">
<figure>
<img src="{{site.baseurl}}/resource_management/figures/aRm_nRm.png" alt="Figure 1: Each network region comprises an RM and multiple applications connected to the RM. The RM is divided into two main parts (application layer RM and network layer RM). Both parts communicate with each other as well as with other RMs from other regions in the respective layer." style="zoom:15%;" />
<figcaption>Figure 1: Each network region comprises an RM and multiple applications connected to the RM. The RM is divided into two main parts (application layer RM and network layer RM). Both parts communicate with each other as well as with other RMs from other regions in the respective layer.</figcaption>
</figure>
</div>

The hierarchical nature allows for cascading network segments and cross network segment coordination. An exemplary use case is visualized in Figure 2. Vehicles (in an automated valet parking (AVP) scenario) connect wirelessly to the edge to stream camera data from the infrastructure that shall be used in each vehicles sensor fusion for enhanced awareness of their environments. As a result the data needs to be transmitted first via the wireless RAN to the vehicles, and then via the in-vehicle networks to the respective unit responsible for sensor fusion. Coordination must take account various aspects:
- Application constraints (deadlines) must not be violated. The deadline must include both the wireless data exchange as well as the forwarding within the in-vehicle network.
- Overload situation at the RAN must be avoided.
- Overload situation and/or buffer overflows at the in-vehicle network must be avoided.
- Network capabilities (packet sizes, data rates, ...) across network segments may differ.
- ...
The proposed application-centric RM provides basic protocol messages for coordinating actions across applications, the aRM and the nRM - even across different network segments.   

<div style="text-align: center;">
<figure>
<img src="{{site.baseurl}}/resource_management/figures/multisegmentUseCase.png" alt="Figure 2: Overview of an explemlary use case with two vehicles - each with its own RM - connected wirelessly to a camera. Data from camera application is send over the edge via the RAN to the in-vehicle network." style="zoom:15%;" />
<figcaption>Figure 2: Overview of an explemlary use case with two vehicles - each with its own RM - connected wirelessly to a camera. Data from camera application is send over the edge via the RAN to the in-vehicle network.</figcaption>
</figure>
</div>

First simulative experiments of the use case described above showed promising results for tightly coordinating data streams across multiple network segments (here RAN and in-vehicle network). More details on the application-centric RM can be found in the corresponding [paper](https://doi.org/10.1145/3528411).