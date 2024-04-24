---
layout: post
title:  "Robustness to Burst Errors"
date:   2023-10-15 10:00:00 +0100
published: true
---

So far, previous works on [W2RP](https://ida-tubs.github.io/lotus/topics/01_error_correction/) (and [WiMEP](https://ida-tubs.github.io/lotus/robustness/01_multicast/)) assumed uniformly distributed (bit) errors. However, real-world scenarios can be subject to more sophisticated error conditions. For example, burst errors can occur that put additional strain on the backward error correction (BEC) mechanism of W2RP. 


Furhermore, previous W2RP works always assumed the sample period and sample (transmission) deadline to be equal (100ms). However, modern (camera) sensors enable higher sampling rates (period < 100ms), while the application constraints (deadline) remain unchanged. While this leads to deadlines larger than sampling periods, thereby resulting in potentially overlapping sample transmission and error correction of multiple frames, we exploit this fact to improve robustness to burst errors.

Generally, we assume a sample transmission can be finished prior to the next sample arriving (t < period). Nevertheless, with the sample deadline exceeding the period each sample transmission gains additional slack (cf. Figure 1). Hence, if a burst error occurs that affects many consecutive fragment transmissions, this slack can be used to perform additional retransmissions, thereby enabling reliable transmission of sample under such circumstances as well. However, complicating safety considerations is the fact that through usage of additional slack subsequent sample transmissions are delayed due to the resulting overlapping nature of samples. Assuming burst errors do not occur too close after one another burst effects on the sample transmissions decay until the additional slack usage returns to zero, i.e., the systems returned to its most robust state.

<div style="text-align: center;">
<figure>
<img src="{{site.baseurl}}/robustness/figures/Pipelining.png" alt="Figure 1: Additional slack from overlapping from overlapping sample transmissions can be exploited to cope with occasional burst errors." style="zoom:15%;" />
<figcaption>Figure 1: Additional slack from overlapping from overlapping sample transmissions can be exploited to cope with occasional burst errors.</figcaption>
</figure>
</div>

We have shown that for a given burst error model (here: [Gilbert](https://doi.org/10.1002/j.1538-7305.1960.tb03959.x)-[Elliot](https://doi.org/10.1002/j.1538-7305.1963.tb00955.x) model) and application (+ W2RP) parameters the propagation of burst effects can be bounded. Thereby, mathmatical bounds corresponded with measurements from our experiments.

Our experiments clearly showed that using stock W2RP (transmission deadline = period) for high rate sample exchange (30Hz) is not feasible (cf. Figure 2). Using the proposed mechanism and extending the transmission deadline significantly decreases deadline violation rates (down to 0% for deadlines > 88ms).
Consequently, reliable sample transmission in burst error scenarios is possible.

<div style="text-align: center;">
<figure>
<img src="{{site.baseurl}}/robustness/figures/violationRatesBursts.png" alt="Figure 3: Deadline violation rates for increasing sample periods." style="zoom:15%;" />
<figcaption>Figure 3: Deadline violation rates for increasing sample periods. Despite increasing the sample deadline leads to increasing sample overlap, reliability is significantly improved.</figcaption>
</figure>
</div>

We further showed that the proposed mechanism can be further used to improve robustness to longer or more frequent bursts. We refer to the proposed mechanisms as the Enhanced-W2RP protocol (E-W2RP). More details on the proposed mechanism, experiments and results can be found in the corresponding [paper](https://doi.org/10.1109/IECON51785.2023.10312061).