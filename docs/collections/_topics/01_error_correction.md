---
layout: topic
title: Towards Reliable Sample Transmission
topic: error_correction
published: true
---

Wireless Reliable Real-Time protocol (W2RP)  is the first protocol that specifically addresses the reliable and timely exchange of large, fragmented samples in V2X environments. W2RP is based on the popular DDS middleware and its wire-protocol RTPS, which are widely deployed in robotics applications due to DDS being used for communication by ROS2 and is also specified for use in in-vehicle networks in AUTOSAR. The middleware nature of W2RP allows for consideration and exploitation of application-level constraints such as sample deadlines - which are notably missing from existing packet-focused V2X standards.

To cope with the challenging channel conditions in wireless communication W2RP employs different mechanisms: Minimum distance shaping is used to allow for low-interference coexistence with other wireless applications. Furthermore, W2RP adopts the sample-level backward error correction (BEC) of RTPS that utilizes acknowledgment bitmaps to inform senders of missing parts of a sample (fragments). Given a certain shaping time and the sample deadline, the remaining slack is used for scheduling retransmission based on the feedback. Thereby, W2RP is not limited to a fixed number of retransmissions per fragments as it is the case for state-of-the-art wireless (802.11 and cellular) standards. Simulations as proof-of-concept experiments using a physical demonstrator setup validated W2RP's effectiveness in direct comparison to only relying on MAC-layer reliability mechanisms of existing (802.11) wireless technologies. Formal proofs of reliability have also been provided.