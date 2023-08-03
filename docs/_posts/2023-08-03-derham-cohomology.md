---
layout: article
title: deRham Cohomology
date: 2023-08-03 02:50
tags: ['deRham', 'cohomology','exact forms','closed forms']
---
# Definitions
Let $M$ be a smooth manifold and $\Omega^k(M)$ denote the space of $k$-forms on $M$. 

## Closed $k$-forms $Z^k$
A $k$-form $\beta\in\Omega^k(M)$ is *closed* if $d\beta = 0$. Denoted by

$$
Z^k = \operatorname{Ker}\bigset{d:\Omega^k(M)\to \Omega^{k+1}(M)}
$$

## Exact $k$-forms $B^k$
$\beta\in\Omega^k(M)$ is *exact* if $\beta=d\alpha$ for some $\alpha\in \Omega^{k-1}(M)$. Denoted by

$$
B^k = \operatorname{Im}\bigset{d: \Omega^{k-1}(M)\to\Omega^k(M)}
$$

## $H^k_{dR}(M)$ 
We define the $k$-th deRham cohomology group on $M$ 

$$
H^k_{dR}(M) = \dfrac{Z^k(M)}{B^k(M)}
$$


{{ site.baseurl }}