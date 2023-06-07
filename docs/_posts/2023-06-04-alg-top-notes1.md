---
layout: post
title: Notes on Algebraic Topology
date: 2023-06-04 19:12
category: math
tags: ['algebraic topology']
---

Is the product of continuous functions again continuous? Yes, here is the proof

Let $F = \prod_{\alpha\in A}f_\alpha$, where each $f_\alpha\in C(\xx_\alpha,\: \yy_\alpha)$. By definition of the product topology, $F$ is continuous iff for every $\alpha\in A$, the map  $\pi_\alpha^\yy\circ F$ is in $C(\xx,\: \yy_\alpha)$. Notice 

$$
\pi_\alpha^\yy\circ F = f_\alpha\circ\pi_\alpha^\xx
$$

the right member is a composition of continuous functions, hence $F$ is continuous.



The following family of maps form a semigroup with the composition operation.

- Quotient maps
- Open maps
- Closed maps
- Homeomorphisms
- Topological Embedding (?)
- Topological Submersion (?)




