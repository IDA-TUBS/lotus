---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---

The project **L**arge **O**bject **T**ransmission **U**nder **S**afety Constraints (LOTUS) addresses challenges in the communication of mobile systems, like Vehicle-to-Everything (V2X) or mobile robots.

Numerous roadmaps and surveys within the scope of Vehicle-to-Everything communication envision an increasing amount of demanding services.
Examples are cooperative perception and remote driving services, which are crucial to further enhance automated mobility (SAE Level 4+). 
These applications require the reliable exchange of large data objects in real-time, such as raw or preprocessed sensor data.

Wireless communication is inherently lossy due to fading effects like reflections, shadowing, and Doppler shift, impacting the signal-to-noise ratio (SNR) and causing bit errors. 
Additionally, vehicle mobility necessitates constant roaming - and thus frequent handovers - between access points (APs), disrupting data transmission and compromising reliability. 
Resilient and continuous application operation requires robustness against these failure modes.

Current Vehicle-to-Everything (V2X) standardization efforts mainly involve the exchange of small data for sharing status and intent information.
Hence, reliability and low-latency mechanisms are optimized for small, single-packet data. 
Such mechanisms are not able to consider a packet as part of a data object's context, and thus insufficiently address the constraints of large data object transmissions.
Consequently, novel solutions for a reliable transmission of large data objects under real-time constraints are needed.

For this purpose, we propose application-centric solutions that overcome the issues of state-of-the-art V2X/wireless technologies. 
Specifically, application-centric approaches allow for utilizing application-information/knowledge for sophisticated coordination, exploiting sample-level deadlines and inherent slack for robustness against various error sources.

This website provides a brief summary of [ongoing work]({{ site.baseurl }}{% link topics.md %}) and references to [publications]({{ site.baseurl }}{% link publications.md %}).
Additionally, current test setups and recent measurement and simulation data are reported.