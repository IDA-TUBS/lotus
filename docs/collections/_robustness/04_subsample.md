---
layout: post
title:  "Improving Robustness by Means of Data Optimization"
date:   2024-10-04 10:00:00 +0100
published: true
---

Despite previous works on improving reliability and robustness for large data transmissions, the high data rates produced by (high definition) sensor data are still a challenge. With the data rates ranging from 10-1000 Mbit/s per application, depending on the type of sensor and whether raw or preprocessed data is used, transmission of such data while adhering to stringent timing and safety constraints via state-of-the-art wireless technologies is not viable. While commodity 802.11ac/be and 5G cellular solutions can achieve multi-Gbit/s data rates, there are no appropriate mechanism to ensure reliability for large data streams. On the other end of the spectrum there are dedicated V2X protocols and ultra reliability and low latency solutions (URLLC and wireless TSN) only manage small data rates that are insufficient for large data streams. Still, such high-definition are deemed essential in enabling higher levels of automations in the future. Consequently, different solutions for robust sensor streaming and collaboration, such as loss-less application-centric data optimization schemes, are required.  <!--end_excerpt-->

| Data                               | Data Rates        |
| ---------------------------------- | ----------------- |
| Cooperative Awareness Message      | 32 Kbit/s         |
| Cooperative Perception Message     | 120 Kbit/s        |
| Small control data                 | 2.5 Mbit/s        |
| H.265 FullHD Video                 | (avg.) ~10 Mbit/s |
| (extended) Local Dynamic Map (LDM) | Up to 25 Mbit/s   |
| LIDAR                              | 25-120 Mbit/s     |
| Raw camera data                    | 250+ Mbit/s       |


Roadmaps already recognized this stark contrast between application data rates and what can be offered by state-of-the-art wireless technology. To address this issue there is the proposal to, e.g., use H.265 encoded video data. However, the lossy codec nature that extensively makes use of interpolation in combination with inherently lossy wireless communication and insufficient error correction mechanisms of SotA standards can lead to persistent visual artifacts that make use of such in safety-critical applications impractical. Nevertheless, the idea of reducing data size (ideally in a loss-less manner) in order to make reliable transmission of large data possible can also be applied to W2RP. By reducing the data size, directly increases the sample-level slack, which in turn allows for better robustness to higher error rates.

<div class="figure">
<figure>
<img style="width:80%;" src="{{site.baseurl}}/robustness/figures/04_slackIncrease.png" alt="Using W2RP, decreasing the data size increases sample-level slack. This slack can the be used for additional error correction, thus allowing for higher robustness in general."/>
<figcaption>Figure 1: Using W2RP, decreasing the data size increases sample-level slack. This slack can the be used for additional error correction, thus allowing for higher robustness in general.</figcaption>
</figure>
</div>

To determine how lossless data optimization can be achieved multiple real-world camera datasets ([DVS](https://ziyang.eecs.umich.edu/tools.html) and [A2D2](https://www.a2d2.audi/a2d2/en.html) dataset) have been analyzed. The DVS dataset comprises a feed from a static infrastructure camera. Looking at two consecutive frame it seems like not much changes. In depth analysis confirms this assumption, with differences typically being distributed across 20-50% of the image only. Consequently, using incremental updates could drastically reduce the data rate in a lossless manner.

<div class="figure">
<figure>
<img style="width:80%;" src="{{site.baseurl}}/robustness/figures/04_dvs.png" alt="Differences between two consecutive frames of a static infrastructure camera covering an intersection."/>
<figcaption>Figure 2: Differences between two consecutive frames of a static infrastructure camera covering an intersection. Given the static nature of the camera, only parts of the image change.</figcaption>
</figure>
</div>

In contrast, using the same approach for a camera mounted to a vehicle would not be advantageous, as basically all parts of an image change marginally for each frame. As such, different means of data optimization are needed.

<div class="figure">
<figure>
<img style="width:80%;" src="{{site.baseurl}}/robustness/figures/04_a2d2.png" alt="Differences between two consecutive frames of a camera mounted to a moving vehicle."/>
<figcaption>Figure 3: Differences between two consecutive frames of a camera mounted to a moving vehicle. Changes are always distributed across the whole image.</figcaption>
</figure>
</div>

Instead, clues from the perception pipeline of the [Autoware](https://autoware.org/) software stack showed perception often relying on certain "*Regions of Interest*" (RoIs) that only cover small portions of an image, e.g. a traffic light or sign. Thus, only transmitting these RoIs can drastically reduce data size in order to increase slack.

<div class="figure">
<figure>
<img style="width:80%;" src="{{site.baseurl}}/robustness/figures/04_roi.png" alt="Regions of Interest (RoIs) in a capture from the Autoware simulator."/>
<figcaption>Figure 4: Regions of Interest (RoIs) in a capture from the Autoware simulator. The RoI size is only a fraction of the original size at a maximum of 13KB compared to the 2.76MB of the original camera image.</figcaption>
</figure>
</div>

Most notably, there is no single solution that can be applied to all use cases. Instead, the most useful optimization approach is highly dependent on the specific use case, sensor and data configuration.

Low-overhead mechanisms to allowing handling of both incremental updates and RoI have been added to W2RP. A visual representation can be found in Figure 5.

<div class="figure">
<figure>
<img style="width:80%;" src="{{site.baseurl}}/robustness/figures/04_mechanisms.png" alt="Incremental update mechanism and means to transmit RoIs via W2RP."/>
<figcaption>Figure 5: Schematic visualization of the incremental update mechanism and means to transmit RoIs via W2RP.</figcaption>
</figure>
</div>

Simulations (cf. Figure 6) as well as physical experiments highlight the effectiveness of either mechanisms in improving robustness (increasing capability to cope with higher error rates) for their corresponding use case. Again, as shown in previous works, packet-level backward error correction (BEC) as used in 802.11 and cellular wireless standards is not up to the task, failing to enable robust sample exchange. Furthermore, the results highlight that there is no single solution, instead the most robust mechanism is highly data and use case dependent. 

<div class="figure">
<figure>
<img style="width:80%;" src="{{site.baseurl}}/robustness/figures/04_results.png" alt="Simulation results for incremental update and RoI mechanisms in thwo different scenarios."/>
<figcaption>Figure 6: Simulation results for incremental update and RoI mechanisms in thwo different scenarios. Depending on the use case and the data, different mechanisms lead to optimal robustness. There is no single solution.</figcaption>
</figure>
</div>

More details on the proposed mechanism, experiments and results can be found in the corresponding [paper]() (link TBD).
