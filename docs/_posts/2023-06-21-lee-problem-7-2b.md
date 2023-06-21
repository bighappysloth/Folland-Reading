---
layout: post
title: Lee Problem 7.2b
date: 2023-06-21 02:36
category: math
tags: ['math','manifold']
---
Part A of this problem can be found here: [Product Manifolds]({{ site.baseurl }}{% post_url /math/2023-06-21-product-manifolds %}). We wish to show, if $\omega: G\to G$ is the inversion map, $g\mapsto g^{-1}$, then 

$$
d\omega\biggr|_{e}(X) = -X\quad\forall e\in G,\: X\in T_e G
$$

Let $f: G\to G$ be the trivial map, every element $g\in G$ gets sent to the identity element. $f(g) = e$ for every $g\in G$. Write $f$ as

$$
f: g\mapsto e\quad\text{by}\quad g\mapsto (g,g^{-1})\mapsto gg^{-1} = e
$$

Let $m$ denote the multiplication map, then $f = m\circ (\id{G}\times \omega)$, computing the arguments to $m$ coordinate wise, we see that

$$
\begin{cases}
(dm)\biggr|_{(e,e)}\circ (d\id{G}\times \omega)\biggr|_{e}(X) = df_e(X) = 0
\end{cases}
$$

Using the fact that $dm_{(e,e)}(X,Y) = X + Y$, and linearity. Will continue this post at a later date.