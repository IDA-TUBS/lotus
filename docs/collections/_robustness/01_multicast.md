---
layout: post
title:  "Reliable Multicast for Large Samples"
date:   2023-09-05 16:17:52 +0100
published: true
---

Unicast data dissemination in cooperative perception and similar applications is inefficient as it can be expected that data may be needed by multiple vehicles.
Hence, W2RP has been extended to support multicast resulting in WiMEP.
As errors can be individual per receiver, efficient backward error correction (BEC) is a challenging task.
For this purpose, WiMEP supports bundling of BEC for receivers with similar error patterns and offers means to prioritize receivers based on arbitrary conditions.
WiMEP's effectiveness has been demonstrated both in simulation as well as under real-world conditions using the IDA's wireless demonstrator setup.