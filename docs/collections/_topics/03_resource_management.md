---
layout: topic
title:  Coordination by Means of Resource Management
topic: resource_management
published: true
---

Due to its shared nature, the wireless channel is used by various applications of different criticalities and with different requirements and constraints.
This makes timing guarantees impractical, as long as no coordination is used.
A centralized application-centric Resource Management (RM) approach that is based on Software Defined Networking (SDN) principles (communication divided into control and data plane) has been developed to address the coordination of various wireless applications.

A hierarchical architecture is employed that allows for coordination across network segments.
Thereby, the RM takes into account both application requirements and constraints as well as network properties.
A dedicated reconfiguration protocol hat takes into account the safety constraints required to ensure safety in a system where the RM coordinates safety-critical systems is currently being developed.
<!-- A dedicated reconfiguration protocol that takes into account the safety constraints required to ensure safety in a system where the RM coordinates safety-critical systems has been developed. 
The combination of heartbeat-based connection monitoring, protection against inherent message loss, node-level fail-silent behavior and synchronized mode changes the RM ensures safety by enforcing consistent application (and network) modes across the wireless network.
The coordination principles have further been extended with respect to letting applications on a single node share resources ('shared slack') to enable more efficient resource utilization and better cope with dynamic backward error correction (BEC) that are to be expected in wireless channels. -->