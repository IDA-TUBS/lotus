---
layout: post
title:  "Reliable Multicast for Large Samples"
date:   2023-09-05 16:17:52 +0100
published: true
---

Unicast data dissemination in cooperative perception and similar applications is inefficient as it can be expected that data may be needed by multiple vehicles/nodes. Hence, W2RP has been extended to support multicast resulting in WiMEP. As errors can be individual per receiver, efficient backward error correction (BEC) is a challenging task. For this purpose, WiMEP supports bundling of BEC for receivers with similar error patterns and offers means to prioritize receivers based on arbitrary conditions. WiMEP's effectiveness has been demonstrated both in simulation as well as under real-world conditions using the IDA's wireless demonstrator setup.

The effectiveness of WiMEP has been demonstrated using simulations as well as a physical demonstrator setup. For the former, the [IDA Wireless Simulator](https://github.com/IDA-TUBS/IDAWirelessSimulator) has been used. As expected, our simulations showed WiMEP clearly outperforming standard DDS, e.g., with respect to reliable throughput at a given error rate (cf. Figure 1) or enabling more receivers to receive the sample reliably. For both experiments, LIDAR samples (cf. [3GPP TR22.886](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=3108)) have been exchanged.

<div style="text-align: center;">
<figure>
<img src="{{site.baseurl}}/robustness/figures/error_rate.png" alt="Figure 1: WiMEP enables far reliable transmission of larger samples at higher error rates compared to using multiple W2RP unicast streams or standard DDS multicast." style="zoom:15%;" />
<figcaption>Figure 1: WiMEP enables far reliable transmission of larger samples at higher error rates compared to using multiple W2RP unicast streams or standard DDS multicast.</figcaption>
</figure>
</div>

WiMEP's prioritization mechanism, that is specifically design to address the issue of receivers being subject to different error patterns (e.g., due to independent signal paths), also proved highly effective. Without any prioritization, all receiving nodes are subject to occasional deadline violation (cf. Figure 2). With safety-critical applications relying on the respective cooperative perception data, however, even those rare deadline violations are unacceptable. The prioritization mechanism enables most of the receivers (here four out of five) to receive the sample completely (cf. Figure 3)., thereby enabling continuous and safe operation of cooperative perception applications on those nodes. Note that vehicles are always equipped with a fallback mechanism that still ensures safety in case of deadline violations, however at a degraded service quality due to missing out on cooperative perception data.

<div style="text-align: center;">
<figure>
<img src="{{site.baseurl}}/robustness/figures/noprio.png" alt="Figure 2: Deadline violation rates of different nodes without prioritization." style="zoom: 15%;">
<figcaption>Figure 2: Deadline violation rates of different nodes without prioritization.</figcaption>
</figure>
<figure>
<img src="{{site.baseurl}}/robustness/figures/prio.png" alt="Figure 3: Deadline violation rates of different nodes with prioritization being used." style="zoom:15%;" />
<figcaption>Figure 3: Deadline violation rates of different nodes with prioritization being used.</figcaption>
</figure>
</div>

Finally, we build a physical demonstrator setup that uses commercial-of-the-shelf hardware to test WiMEP in a real wireless environment. We transmitted scaled down, real-world camera data (cf. [A2D2 dataset](https://www.a2d2.audi/a2d2/en.html)) between our nodes. Thereby, the physical experiments verified the experimental results. More details on the proposed mechanism, experiments and results can be found in the corresponding [paper](https://doi.org/10.1145/3617126).