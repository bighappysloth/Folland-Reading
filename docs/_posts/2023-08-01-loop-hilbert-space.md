---
layout: post
title: loop hilbert space notes
date: 2023-08-01 02:51
category: 
author: 
tags: []
summary: 
---
## Proposition 5
We define the $L^2$ Sobolev spaces on $S^1$ in the notation of Hofer, 
- $$H^s = \bigset{f\in L^2(S^1,\real^{2n}),\: \sum_{k\in\mathbb{Z}} \vert k\vert^{2s}\vert\hat{f}(k)\vert^2<+\infty}$$
- $H^s$ is equipped with inner product
$$
\langle x,y\rangle_{(s)} = \langle x_0, y_0\rangle + 2\pi \sum_{k\in\mathbb{Z}}\vert k\vert^{2s}\langle x_k, y_k\rangle
$$

    and 

    $$\lVert x\rVert_{(s)}^2 = (\langle x,x\rangle)^{1/2} = \biggl(\lVert x_0 \rVert_{\real^{2n}}^2 + \biggl(2\pi\sum_{k\in\mathbb{Z}}\vert k\vert^{2s}\lVert x_k \rVert_{\real^{2n}}^2\biggr)\biggr)^{1/2}$$

Consider the inclusion map $j: H^{1/2}\to L^2$, where both are Hilbert Spaces (to be proven). Identifying their dual through the Riesz isomorphism, 

$$
j^*: L^2\to H^{1/2},\quad \langle j(x), y\rangle_{L^2} =\langle x, j^*(y)\rangle_{H^{1/2}}
$$

for every $x\in H^{1/2}$ and $y\in L^2$. The statement of Proposition 5 is as follows 