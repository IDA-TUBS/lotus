---
layout: post
title: "Continuous Connectivity Testbed"
date:   2025-03-25 14:00 +0100
published: true
youtubeId: EUOEarpHoD8
---

Industrial automation demands continuous, low-latency streaming for mobile robots, yet mobility often causes handover delays and connectivity issues.
We present a physical testbed designed to demonstrate and evaluate continuous low-latency streaming in roaming scenarios, without relying on redundant data transmissions.<!--end_excerpt-->
The concept was previously publised in the [2024 IEEE Intelligent Vehicles Symposium (IV)](https://ieeexplore.ieee.org/abstract/document/10588468).
By utilizing off-the-shelf 802.11 hardware and Linux-based systems, our approach closely mirrors the capabilities of industrial systems, providing valuable insights for practical deployment.
Our approach achieves seamless handovers in under 10 ms without redundant transmissions, confirming its feasibility for industrial applications.

The demonstrator evaluates the proposed continuous streaming solution in real-world conditions.
It consists of four nodes, two Access Points (APs), an edge server and the model truck (mobile node).
The two available modes of operation (up- and downlink streaming of large data) allow for enabling applications such as remote operation and cooperative perception. 
For this purpose samples are generated using openCV, allowing for free configuration of the image data to be transferred. 
Importantly, either application requires constant and uninterrupted data streaming between truck and edge.
The testbed replicates typical mobility scenarios in factory environments, including handovers and connectivity disruptions.
A more detailed discussion on the functionality is provided in an accompanying [paper]().
The setup and configuration of the testbed is available on [github](https://github.com/IDA-TUBS/CC_Testbed).


### Testbed Demonstration
{% include youtubePlayer.html id=page.youtubeId %}