---
layout: article
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

Let $m$ denote the multiplication map, then $f = m\circ (\id{G}\times \omega)$, computing the arguments to $m$ coordinate wise, and define the following inclusion maps

$$
\begin{align}
\iota_1: p\mapsto (p,e^{-1})\quad &d\iota_1(X) = (X,0)
\iota_2: q\mapsto (e,q)\quad &d\iota_2(Y) = (0,Y)
\end{align}
$$

It is clear that $(m\circ \iota_1) = \id{G} = (m\circ\iota_2)$. Now, $df\equiv 0$, since it is constant on $G$, hence

$$
\begin{align*}
df_{(e)}(X) &= dm_{(e,e^{-1})}(X,X)\\
&= dm_{(e,e^{-1})}(X,0)\\
&= d(m\circ \iota_1)_{(e)}(X) + d(m\circ \iota_2\circ \omega)_{(e)}(X) \\
&= \id{T_e G}(X) + \biggl(d(m\circ\iota_2)_{(e,e^{-1})}\biggr)\circ (d\omega)_{e}(X)\\
&= X + (\id{T_e(G)}(X))\circ (d\omega)_{e}(X)\\
&= X + d\omega_e(X)\\
&= 0
\end{align*}
$$

therefore $d\omega_e(X) = -X$.


