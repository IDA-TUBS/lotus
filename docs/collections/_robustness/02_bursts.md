---
layout: post
title:  "Robustness to Burst Errors"
date:   2023-10-15 10:00:00 +0100
published: true
---

First works always assumed the sample period and sample deadline to be equal (100ms).
However, modern (camera) sensors enable higher sampling rates, while the application constraints (deadline) remain unchanged.
This leads to deadlines larger than sampling periods resulting in potentially overlapping sample transmission and error correction of multiple frames. 
W2RP has been extended to allow for exploitation of those overlapping sample transmission for handling occasional burst errors (E-W2RP).