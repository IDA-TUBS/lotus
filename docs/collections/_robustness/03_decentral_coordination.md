---
layout: post
title:  "Enabling Multi-Link Data Transmissions"
date:   2023-06-07 10:00:00 +0100
published: true
---

Sending fragments periodically with a static *shaping time* can reach its limits in case the channel utilization is extremely high. Obviously, it is not possible to support unlimited numbers of high-volume V2X collaborative sensing links within limited channel capacity. Instead, link access to resources has to be managed. <!--end_excerpt-->

One solution that targets closed and centrally resource managed environments has been proposed for a valet parking use case [paper](https://doi.org/10.24355/dbbs.084-202405030723-0). However, central resource management can not be assumed to be available in any traffic scenario. It might be too costly to be deployed and maintained on a given road, can break down, be too complex due to the high dynamism of vehicular environments, or is simply not deployed yet. Hence, it is favorable to provide a basic mechanism that lets links find a resource access schedule in a decentralized way.

<div class="figure">
<figure>
<img style="width:80%;" src="{{site.baseurl}}/robustness/figures/03_use_case_setup.png" alt="An open road scenario of an intersection with Infrastructure to Vehicle (V2I) and Vehicle to Vehicle (V2V) communication. An infrastructure camera captures a critical roadwork site."/>
<figcaption>Figure 1: An open road scenario of an intersection with Infrastructure to Vehicle (V2I) and Vehicle to Vehicle (V2V) communication. An infrastructure camera captures a critical roadwork site.</figcaption>
</figure>
</div>

In our [paper](https://dl.acm.org/doi/abs/10.1145/3575757.3593652) we consider the challenging scenario of an urban intersection as depicted in Figure 1. Here, either vehicles share sensor data samples (V2V) or receive image samples from infrastructure cameras (I2V). Thereby, the infrastructure camera covering the roadwork site is the most important one with the highest priority (link 5). It follows the infrastructure cameras covering the space behind obstacles (links 2 and 4). One priority below is the V2V communication related to two driving vehicles (links 3). The least important connections are those between cars waiting at the traffic lights (links 1 and 6).

<div class="figure">
<figure>
<img style="width:80%;" src="{{site.baseurl}}/robustness/figures/03_prioritized_adaptive_shaping.png" alt="Figure 2: Based on the RTT-based feedback and the prioritization represented by the scaling factor $k_i$, the shaping time adapts differently for links of different prioritizations."/>
<figcaption>Figure 2: Based on the RTT-based feedback and the prioritization represented by the scaling factor $$k_i$$, the shaping time adapts differently for links of different prioritizations.</figcaption>
</figure>
</div>

The overall challenge is to allocate the resources in such a way that higher priority links have access to more resources to meet their sample deadlines and lower priority links disconnect in case the remaining resources are not sufficient for their timing requirements. The proposed decentralized solution originates in the ability of the Wireless Reliable Real-Time Protocol (W2RP) to avoid queuing of fragments in the MAC Wifi interface due to *fragment shaping*. This enables W2RP to estimate the current channel load via the bitmap feedback of the backchannel. Specifically, the measured blocking time $$t^{meas.}_b$$ of a fragment, describing its arbitration and transmission at the MAC interface, represents the channel interference in the context of the Wifi CSMA/CA arbitration protocol. Then, higher blocking times represent a higher interference and, hence, a higher channel load. Due to the multi-fragment nature of samples, this load estimation is robust against frame losses of the wireless channel. Figure 2 shows how the blocking time is used to control a link's resource allocation. Based on its prioritization, a link has access to a maximum amount of resources (minimum shaping time $$t^{min}_{sh,i}$$). If the measured channel load increases, links also increase their shaping time and, hence, reduce their resource consumption. Thereby, a factor $$k_i$$ lets lower priorities (here: blue link $$l_2$$) degrade faster. Since all links sense the same channel load, all links adapt their resource share proportionally to $$k_i$$.

<div class="figure">
<figure>
<img style="width:80%;" src="{{site.baseurl}}/robustness/figures/03_adaptive_sample_latencies.png" alt="FFigure 3: Sample latencies of the links depicted in Figure 1 over time. Following the links' starting and ending times, the links adapt their resource shares in a way to grant more resources to higher priority links."/>
<figcaption>Figure 3: Sample latencies of the links depicted in Figure 1 over time. Following the links' starting and ending times, the links adapt their resource shares in a way to grant more resources to higher priority links.</figcaption>
</figure>
</div>

Figure 3 shows the evaluation of the intersection use case from above. Each link corresponds to the link number in Figure 1. On the x-axis, starting and ending times are denoted. We assume a latency requirement of 100 milliseconds for each link, which leads to a disconnection if violated. The low priority *Link 1*, which connects two vehicles waiting at the traffic lights, breaks down and disconnects after the initialization of the high priority *Link 5*, which covers the critical roadwork site for a passing vehicle. This disconnection of the lower priority link represents its release of resources that are then used by the remaining higher priority links to support their latency requirements. Interestingly, the robustness of links is also ordered by the prioritization as it corresponds to the resource share. For instance, the higher priority I2V links 2 and 4 have more time slack between their achieved latencies and their deadlines than the lower priority link 3.

Overall, the proposed decentralized resource management approach is a very effective protocol to instantly manage collaborative sensing applications. This plug-and-play approach makes it possible to use collaborative sensing in any given traffic scenario with regard to the available resources and thus represents a basic mode of operation. Moreover, it maintains full interoperability with existing V2X traffic.