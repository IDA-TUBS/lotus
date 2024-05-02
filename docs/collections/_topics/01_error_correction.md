---
layout: topic
title: Towards Reliable Sample Transmission
topic: error_correction
published: true
---

Wireless communication is an inherently lossy technology. When targeting the communication of large data objects under real-time and safety requirements, such as in cooperative perception, lost frames have to be retransmitted in time. The Wireless Reliable Real-Time protocol (W2RP) is the first protocol that specifically addresses the reliable and timely transmission of large application data objects, called samples, in V2X environments. In contrast to small awareness or notification messages, samples represent multi-frame data communication within an extended application-level deadline. By taking advantage of such larger deadlines, W2RP maximizes the efficiency of retransmissions, which improves reliability and minimizes the allocated resources of large V2X data streams.
Both reliability and resource efficiency are prerequisites for the communication of large data samples in safety-critical scenarios, such as collaborative perception. W2RP, as a middleware protocol, is integrated into the popular Data Distribution Service (DDS), which is the default communication middleware of the Robot Operating System (ROS) 2 and is also part of the AUTOSAR communication specification.
This makes W2RP easily accessible for robotic and automotive applications.

The basic principle of W2RP is depicted in Figure 1, which shows an infrastructure camera transmitting sensor data to an in-vehicle sensor fusion. To adapt to the wireless communication channel, samples are first divided into a number of smaller fragments.
<div class="figure">
<figure>
<img style="width:80%;" src="{{site.baseurl}}/topics/figures/01_single_link.png" alt="Figure 1: The high-level communication view between an external sensor application and the collaborative sensor fusion application using W2RP."/>
<figcaption>Figure 1: The high-level communication view between an external sensor application and the collaborative sensor fusion application using W2RP.</figcaption>
</figure>
</div>
Each of those fragments is subject to the deadline of its corresponding sample, which is typically equal to the sample period. Within the sample deadline W2RP implements two basic mechanisms:

* **Fragment shaping**: Fragments are passed to the lower MAC layer with a minimum distance time called *fragment shaping time*.
* **Bitmap-based backward error correction (BER)**: If transmitted successfully, the receiver answers each fragment with a bitmap-based acknowledgment to the sender, where each bit indicates the successful reception or loss of a fragment in the sample.

These two mechanisms enable an efficient and reliable communication within a shared wireless channel.
A concrete protocol example is depicted in Figure 2.
<div class="figure">
<figure>
<img style="width:80%;" src="{{site.baseurl}}/topics/figures/01_middleware_principle.png" alt="Figure 2: Example of the intelligent fragment transmission schedule of the W2RP middleware protocol and its corresponding bitmap-based backchannel."/>
<figcaption>Figure 2: Example of the intelligent fragment transmission schedule of the W2RP middleware protocol and its corresponding bitmap-based backchannel.</figcaption>
</figure>
</div>
In reference to this, the fragment shaping and backchannel mechanisms enable efficient and reliable communication within a shared wireless channel as follows:


* **Bounded interference**: By shaping the time between two successive fragment transmissions, the maximum load that can be inserted into the wireless channel over any time interval is bounded. This enables the predictable deployment of multiple large V2X data streams in a shared wireless channel.
* **Middleware-centric retransmission management**: The initialization of retransmission is managed by the middleware rather than by the MAC layer. 
* While Wifi and cellular limit the number of retransmissions per fragment, W2RP mitigates this restriction by interpreting the number of fragment retransmissions in the relevant sample context.
* **Intelligent selection of fragment retransmissions**: When a middleware transmits sample fragments, stalling and waiting for acknowledgments is not necessary at all.  Rather W2RP can continuously transmitting unsent or negatively acknowledged fragments while receiving backchannel information in parallel. This minimizes the speculative retransmissions to the last few unacknowledged fragments and, therefore, maximizes resource efficiency.
* **Protocol robustness**: Since each additional (negative) acknowledgment only costs one bit, answering each received fragment with a bitmap comes at a low cost. In case a bitmap is lost, W2RP can resume transmitting other fragments for which it has backchannel information and wait for the next bitmap to recover the lost one. Due to the shaping, the protocol does not rely on an ultra-low backchannel delay.

Figure 3 depicts a representative result from the basic [W2RP publication](https://leopard.tu-braunschweig.de/receive/dbbs_mods_00069882?q=Peeck), which is based on 10Hz 20KB sample communication over an IEEE 802.11p automotive Wifi channel. Here, only the raw transmission duration of 20KB with a sample period of 100ms accounts for approximately 6% of the overall channel utilization. The frame error rate (FER) describes the chance a fragment transmission has a non-recoverable bit error and the average arbitration time at the MAC layer is a measure of the overall channel utilization.

<div class="figure">
<figure>
<img style="width:80%;" src="{{site.baseurl}}/topics/figures/01_single_link.png" alt="Figure 3: W2RP link with a shaping time of 1400us, a sample size of 20kB, and a fragment size of 800 Byte. The deadline is 100ms."/>
<figcaption>Figure 3: W2RP link with a shaping time of 1400us, a sample size of 20kB, and a fragment size of 800 Byte. The deadline is 100ms.</figcaption>
</figure>
</div>

Interestingly, the shaping time determines the number of retransmissions within the deadline and, hence, also the addressable frame error rate, which is up to 50% in the example. Only after the channel load increases significantly, the frame blocking time at the Wifi MAC interface exceeds the shaping time, for which W2RP loses performance. However, this is no surprise since large data sample communication always relies on available resources. Within, W2RP maximizes the efficient use of resources and can be precisely configured to specific feasible channel conditions in terms of upper frame error rates. Simulations as well as proof-of-concept experiments based on a physical demonstrator setup validated W2RP's effectiveness in direct comparison to standard DDS as well as MAC-layer reliability mechanisms of existing (802.11) wireless technologies. Formal proof of reliability could be provided in a resource-managed environment, such as valet parking. To dynamically manage multiple W2RP links in a decentralized access scenario, a self-adaptive approach to the shaping time has been developed, as summarized in [this section](https://ida-tubs.github.io/lotus/robustness/03_decentral_coordination/).



