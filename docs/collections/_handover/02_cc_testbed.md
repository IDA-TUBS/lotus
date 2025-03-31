---
layout: post
title: "Continuous Connectivity Testbed"
date:   2025-03-25 14:00 +0100
published: true
youtubeId: EUOEarpHoD8
---


Autonomous mobile robots (AMRs) in the industrial domain and future connected vehicle use cases demand continuous, low-latency streaming of large (sensor) data. However, the inherent mobility of those systems causes handover delays, and thus connectivity issues, thereby leading to stream disruptions (deadline violations) and seriously compromising application performance. We present a physical testbed designed to demonstrate and evaluate such roaming situations. Furthermore, we show that continuous low-latency streaming is possible under such circumstances given proper choice of protocols, without relying on inefficient redundant data transmissions. <!--end_excerpt-->

The concept was previously published as part of the [2024 IEEE Intelligent Vehicles Symposium (IV)](https://ieeexplore.ieee.org/abstract/document/10588468) with a basic description found on the [LOTUS website](https://ida-tubs.github.io/lotus/handover/01_continuous_access/). To evaluate the concept's efficacy, we setup up a pyhsical demonstrator testbed which, by utilizing off-the-shelf 802.11 hardware and Linux-based systems, closely mimics the capabilities of state-of-the-art industrial wireless systems, providing valuable insights for practical deployment. Experimental results show that our approach, which combines low-overhead link monitoring, application-centric resource management and the use of [W2RP](https://github.com/IDA-TUBS/lwW2RP) on the data plane, achieves handovers in under 10 ms, thereby significantly outperforming existing handover mechanisms that can cause stream disruptions ranging from 100 ms to few seconds depending on the technology. In constrast, our continuous connectivity concept which includes the use of W2RP allows for continuous large data streaming without any deadline violations even in those challenging roaming situations, importantly without relying on redundant transmissions via multiple links. Thereby, the results highlight the feasibility of our approach for industrial applications.

The demonstrator evaluates the proposed continuous streaming solution in real-world conditions. It consists of four nodes, two Access Points (APs), an edge server and the model truck (mobile node). The two available modes of operation (up- and downlink streaming of large data) allow for enabling applications such as remote operation and cooperative perception. For this purpose, samples are generated using openCV, allowing for free configuration of the image data to be transferred. Importantly, either application requires constant and uninterrupted data streaming between truck and edge. The testbed replicates typical mobility scenarios in factory environments, including handovers and connectivity disruptions. <!-- A more detailed discussion on the functionality is provided in an accompanying [paper]()-->. The setup and configuration of the testbed is available on [github](https://github.com/IDA-TUBS/CC_Testbed).

### Testbed Demonstration
{% include youtubePlayer.html id=page.youtubeId %}