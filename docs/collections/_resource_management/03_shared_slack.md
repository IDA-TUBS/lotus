---
layout: post
title:  "Shared Slack Budgeting for Ultra Reliable Hard Real-Time Streaming"
date:   2024-04-24 12:00:00 +0100
published: true
---

Applications with varying requirements and constraints are envisioned to share a wireless channel in order to enable improved cooperative behavior in autonomous systems. Most challenging in that regard are application exchanging large objects such as sensor data. So far the exchange of such data has not been addressed by wireless (V2X) standards. While W2RP and its extensions offer reliability mechanisms for such data exchange, so far only single applications are considered. <!--end_excerpt-->

In general, we assume a wireless channel to be shared by multiple nodes, with each node potentially hosting mutltiple applications. Therefore, not only nodes but also applications compete for resources. This is further complicated by the fact that packet losses in the inherently lossy wireless communication will result in dynamic backward error correction (BEC) needs (for additional information on error protection: [W2RP](https://ida-tubs.github.io/lotus/topics/01_error_correction/)). The combination of multiple applications being hosted by a given node, each with timevariant BEC needs leads to a non-standard shared-resource problem. Meanwhile there are still stringent timing and safety constraints that must be violated.

We propose a 2-level hierarchical resource reservation approach for W2RP - called Budget-based Server for Shared Slack (BS-SS) - that can be integrated with the other works on Resource Management (RM) described [here](https://ida-tubs.github.io/lotus/topics/03_resource_management/):

At the top level, the BS-SS concept is based on each node being assigned a certain set of channel resources - its budget - by a central orchestrator (RM) that it can use to communicate. This budget is determined by a RM based on the node's application requirements and channel conditions. Then each node can assign parts of its budget on its own. To allow for more efficient and dynamic resource utilization, we divide the sample transmission of a given application into two phases: First, the resources needed for the ’normal’ periodic transmission of a sample’s fragments that is static regardless of channel conditions, and second, the resources needed for the dynamic ’retransmission’ part for the inevitable retransmissions in a lossy wireless channel, whose needs change depending on the current channel conditions. With periodic parts being reserved, all remaining resources are available to applications as shared slack (cf. Figure 1). The shared slack is available to applications that dynamically need additional BEC resources, thereby enabling an increased robustness to ocassional error spikes. Being complemented by a prioritization mechanism that guarantee safety and can further improve reliability (of the most critical applications) in mixed-criticality environments as well as a safety gatekeeper that could integrate with the nRM, ultra reliable streaming of large data is feasible in complex multi-node and multi-application scenarios. 

<div class="figure">
<figure>
<img style="width:80%" src="{{site.baseurl}}/resource_management/figures/sharedSlack.png" alt="Figure 1: Example of a node with two applications. The lower plot visualizes the budget usage of the node. After scheduling the periodic parts there is spare budget (shared slack) available for applications to use in case BEC needs increase dynamically."/>
<figcaption>Figure 1: Example of a node with two applications. The lower plot visualizes the budget usage of the node. After scheduling the periodic parts there is spare budget (shared slack) available for applications to use in case BEC needs increase dynamically.</figcaption>
</figure>
</div>

Simulative evaluations have been performed to assess the effectiveness of BS-SS. Thereby, BS-SS has been compared to static configurations that assign each application a certain static slack based on the error rates at the time of issuing a request. It became apparent that this static slack was insufficient in offering robustness to occasional error spikes where as BS-SS as able to cope with these conditions without any applications experiencing deadline violations. While it would be possible to devise more conservative W2RP parameters that allow static slack configurations to cope with such spikes, the experiments showed a drastically worse resource reservation efficiency (cf. Figure 2). While BS-SS can dynamically reserve small chunks of shared slack that leads to near optimum resource reservation the conservative static configuration required huge overprovisioning in order to ensure that critical applications do not experience deadline violations. BS-SS would allow for that budget to be used by other low-criticality applications while still ensuring robustness to ocassional error spikes.

<div class="figure">
<figure>
<img style="width:80%" src="{{site.baseurl}}/resource_management/figures/channelUtilization.png" alt="Figure 2: Channel/Resource Reservations for different application classes for static and BS-SS policies. Static configurations require massive overprovisioning to reach similar robustness as the BS-SS. BS-SS in contrast reaches near optimum efficiency."/>
<figcaption>Figure 2: Channel/Resource Reservations for different application classes for static and BS-SS policies. Static configurations require massive overprovisioning to reach similar robustness as the BS-SS. BS-SS in contrast reaches near optimum efficiency..</figcaption>
</figure>
</div>

More details on BS-SS and further experiments can be found in the corresponding [paper](https://doi.org/10.24355/dbbs.084-202405020838-0).