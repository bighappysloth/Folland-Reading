---
layout: post
title: Product Manifolds
date: 2023-06-21 01:11
category: math
tags: ['math','manifold']
---
We will group some of the key results concerning product manifolds.

## Mechanisms


# Construction of the product manifold (Examples 1.8, 1.34, 1.45, 2.13)
Let $M_1,\ldots M_k$ be a collection of smooth manifolds (without boundary). Define their product

$$
\prod M_j = M_1\times \cdots \times M_j
$$

is another smooth manifold with dimension $\dim \prod M_j = \sum \dim M_j$, equipped with the product topology. It has a unique smooth struture induced by charts on each $M_j$. The finite product of second-countable (resp. Hausdorff, locally compact) topological spaces is again second-countable (resp. Hausdorff, locally compact).

Denote the projection maps $\pi_i: \prod M_j \to M_i$. We will not make the distinction between the direct product and the cartesian product, as they are identical for our current purposes. If $p = (p^1,\cdots, p^k)\in \prod M_j$, then $\pi_i(p) = p_i\in M_i$. For each $i = 1, \ldots, k$, $\pi_i(p)\in M_i$ induces a chart $(U_i, \varphi_i)\in\mathcal{A}_{M_i}$. Where $$\mathcal{A}_{M_i}$$ denotes the (maximal) smooth atlas on $M_i$. And

$$
\Biggl(U_1\times \cdots \times U_k, \quad \varphi_1\times\cdots\times \varphi_k\Biggr)\quad\text{is a chart on }\prod M_j\:\text{containing }p
$$

The finite product of diffeomorphisms is again a diffeomorphism, if 

$$
\Biggl(V_1\times \cdots \times V_k, \quad \psi_1\times\cdots\times \psi_k\Biggr)\quad\text{is another chart on }\prod M_j
$$

then they are smoothly compatible, and determines a *unique maximal smooth atlas* hence a smooth structure containing an atlas consisting of products of charts of this form. As

$$
\begin{align*}
\Biggl(\psi_1\times\cdots\times \psi_k\Biggr)\circ \Biggl(\varphi_1\times\cdots\times \varphi_k\Biggr)^{-1} &= \Biggl(\psi_1\times\cdots\times \psi_k\Biggr)\circ \Biggl(\varphi^{-1}_1\times\cdots\times \varphi^{-1}_k\Biggr)\\[2ex]
&=\Biggl(\psi_1\circ\varphi^{-1}_k\times\cdots\times\psi_k\circ\varphi^{-1}_k\Biggr) 
\end{align*}
$$

is a diffeomorphism from $\varphi_1(U_1)\times\cdots\times\varphi_k(U_k)\to\psi_1(V_1)\times\cdots\times\psi_k(V_k)$

# Smoothness Criterion (Prop 2.12)
Let $N$ be another smooth manifold, then $F: N\to \prod M_j$ is smooth map between manifolds iff for every $\pi_i$, 

$$
\pi_i\circ F \in C^\infty(N,\: M_i)
$$

# Inclusion into a slice: $p\mapsto (p,q)$
We will focus on the two manifold case. Let $M$ and $N$ be smooth manifolds, and let $q\in N$ be fixed. 

- The slice $M\times \{q\}$ is a properly embedded submanifold of $M\times N$ (Proposition 5.12). 

- The inclusion map $\iota_M: M\to M\times N$, that maps $p\mapsto (p,q)\in M\times N$ is a smooth embedding. (Example 4.17)

## Products of Tangent Spaces
The **direct sum** of a finite collection of finite-dimensional vector spaces $\{V_i\}$ is the space of $k$-tuples, whose entries are elements of $V_i$, 

$$
\oplus V_i = \bigset{(v^1, \ldots, v^k),\: v^i\in V_i}\quad\text{with vector operations defined coordinatewise}
$$

# Linear isomorphism of tangent spaces (Prop 3.14)
Let $\prod M_i$ be a product of smooth manifolds (without boundary), and $p\in \prod M_i$, we claim the tagent space $T_p \biggl(\prod M_j\biggr)$ is linearly isomorphic with $\oplus T_{p_j}M_j$, with the map

$$
\alpha: T_p \biggl(\prod M_j\biggr)\to \oplus T_{p_j}M_j\quad  T_p (\prod M_j)\Isomor{L} \oplus T_{p_j}M_j
$$

where we construct $\alpha$ st it **sends the derivations $\nu\in T_p(\prod M_j)$ to each $T_p M_j$ through (the differential of) each $\pi_j$**. 

$$
\alpha(\nu) = \biggl(d\pi_1\biggr|_{p}(\nu),\:\cdots\:, d\pi_k\biggr|_{p}(\nu)\biggr)
$$

We will construct its explicit inverse, let $\nu_j\in T_{p_j} M_j$, for $j = 1,\ldots k$. 

$$
\tau_p(\nu_1,\cdots,\nu_k) = \sum_{i=1}^k (d\iota_j\biggr|_{p_j})(\nu_j)
$$

where the 'slice inclusion map' $\iota_l: M_j\to \prod M_j$ is a **smooth embedding** that 'puts' each coordinate back into place. More precisely:

$$
\iota_l(q) = (p_1,\ldots,p_{l-1},\underbrace{q}_{\text{extra term}}, p_{l+1},\ldots,p_k)
$$

The differential of this slice inclusion map $\iota_l$ onto $\biggl(p_1\times\cdots p_{l-1}\times M_l\times p_{l+1}\times\cdots p_k\biggr)$ acts as the inverse of the differential of $\pi_l$.

The projection map is a **smooth embedding**,

$$
\pi_l: \prod M_j\to M_l\quad \pi_l(p_1,\ldots p_l\ldots p_k) = p_l
$$

# Coordinate representations of $\pi_l$ and $\iota_l$

We will focus on the $M\times N$ case. Let $(p,q)\in M\times N$, and $\pi_1$, and $\pi_2$ be the projection maps onto the first and second coordinate. The slice inclusion maps

$$
\begin{align*}
\iota_q: M\to M\times N,\quad & x\mapsto (x,q)\\
\iota_p: N\to M\times N,\quad & y\mapsto (p,y)
\end{align*}
$$

By the rank theorem, there exists smooth charts that realize the following coordinate representations for the maps:

$$
\begin{alignat}{2}
\hat{\pi}_1 &= \begin{bmatrix}1 & 0\end{bmatrix}\quad &&d\pi_1  = \begin{bmatrix}1 & 0\end{bmatrix}\\[2ex]
\hat{\pi}_2 &= \begin{bmatrix}0 & 1\end{bmatrix}\quad &&d\pi_2  = \begin{bmatrix}0 & 1\end{bmatrix}\\[2ex]
\hat{\iota}_q &= \begin{bmatrix}1 \\ 0\end{bmatrix}\quad &&d\iota_q  = \begin{bmatrix}1 \\ 0\end{bmatrix}\\[2ex]
\hat{\iota}_p &= \begin{bmatrix}0 \\ 1\end{bmatrix}\quad &&d\iota_p  = \begin{bmatrix}1 \\ 0\end{bmatrix}\\
\end{alignat}
$$

# Example of pushfoward derivation: $T_p S\to T_p M$
Let $S$ be an embedded submanifold of $M$, then its inclusion map $\iota: S\hookrightarrow M$ (no longer a slice inclusion map) has coordinate representation $\begin{bmatrix} 1\\ 0\end{bmatrix}$. In coordinates,

$$
\iota(x) = (x,0)\quad\text{or}\quad \iota(x^1,\ldots, x^k) = (x^1,\ldots, x^k,0\ldots, 0)
$$

in some neighbourhood about each point $p\in S$, then

$$
\mcal[d\iota_p] = \begin{bmatrix}1 \\ 0\end{bmatrix}\quad d\iota_p \biggl(\sum_{i=1}^k \nu^i\frac{\partial}{\partial x^i}\biggr|_{p}\biggr) = \sum_{i=1}^m \nu^i\frac{\partial}{\partial x^i}\biggr|_{\iota(p) = p}
$$

where $\nu^{k+1}=\nu^{k+2} =\cdots = \nu^m = 0$. In coordinates,

$$
d\iota_p(\nu) = (\nu,0)\quad \nu\in T_p S
$$

We usually identify the tangent space $T_p S$ with the pushforward tangent space $\iota(T_p S)$ (which is a linear subspace of $T_p M$).

# Problem 7.2: Lie Groups, smoothness of multiplication maps
Let $G$ be a Lie group with $m(\cdot,\cdot):G\times G\to G$ be its defining action. Let $e$ be the identity element of $G$. We wish to show 

$$
\mathrm{d}m_{(e,e)}(X,Y) = X + Y,\quad X\in T_eG,\: \text{and} \: Y\in T_eG
$$

Since we can identify $T_{(e,e)}G\times G\cong T_e G\oplus T_e G$ by Prop 3.14. We define

$$
\begin{alignat}{2}
\iota_1: G\to G\times G,\quad & p\mapsto (p,e) && d\iota_1(X) = (X,0)\\[2ex]
\iota_2: G\to G\times G,\quad & q\mapsto (e,q) && d\iota_2(Y) = (0,Y)
\end{alignat}
$$

See Proposition 2.12 for the step-by-step calculations for the differentials above, or scroll up and find *'Coordinate representations of $\pi_l$ and $\iota_l$'*. Since we are including $G$ into a slice of $G\times G$. Continuing with the Problem, notice $m\circ \iota_1: G\to G$, and $m\circ \iota_2: G\to G$ is the identity on $G$, since

$$
\begin{alignat}{2}
(m\circ \iota_1)(p) &= m(p,e) = pe = p,\quad\quad && p\mapsto (p,e)\mapsto pe = p\\[2ex]
(m\circ \iota_2)(q) &= m(e,q) = eq = q,\quad\quad && p\mapsto (e,q)\mapsto eq = q
\end{alignat}
$$

Identifying any tangent vector $\nu\in T_{(e,e)}G\times G$ by its direct sum decomposition; $\nu = (\nu_1,\nu_2)$. Linearity of $\mathrm{d}m_{(e,e)}(X,Y)$ reads:

$$
\begin{align*}
\mathrm{d}m_{(e,e)}(X,Y) &= \mathrm{d}m_{(e,e)}(X,0) + \mathrm{d}m_{(e,e)}(0,Y)\\[2ex]
&= (\mathrm{d}m\circ\mathrm{d}\iota_1)(X) + (\mathrm{d}m\circ\mathrm{d}\iota_2)(Y)\\[2ex]
&= (\mathrm{d}\id{G})(X) + (\mathrm{d}\id{G})(Y)\\[2ex]
&= \id{T_e G}(X) + \id{T_e G}(Y)\\[2ex]
&= X + Y
\end{align*}
$$

[Lee Problem 7.2b]({% post_url /math/2023-06-21-lee-problem-7-2b %})