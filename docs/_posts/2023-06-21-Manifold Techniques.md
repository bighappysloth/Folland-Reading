---
layout: post
title: Manifold Summary
toc: true
date: 2023-06-21 13:12
category: math
tags: ['manifolds','techniques','mechanisms']
---
## Control of coordinate domains
We can pass any topological argument to:
- countable basis of regular (precompact) coordinate balls or cubes
- every smooth atlas has a countable smooth subatlas
- abuse local compactness (see Rank Theorem Proof)

---

## Covering maps
- Fundamental Group: Prop 1.16, the fundamental group of a topological manifold is countable
- Smooth covering Maps: Prop 4.33-4.46
- Universal covering groups: Prop 7.7-7.10

---

## Derivations, pushforward, and differentials
Let $M$ be a smooth manifold and $p\in M$,

### Equality of derivations at $p$
If $$\nu = \nu^i\frac{\partial}{\partial x^i}\biggr|_{p}$$ and $$\omega = \omega^i\frac{\partial}{\partial x^i}\biggr|_{p}$$ are tangent vectors in $T_pM$, they are equal iff

- Their basis representations with respect to any (thus all) coordinate charts are equal, 

$$
\nu^i = \omega^i\quad\forall i = 1,\ldots, m
$$

- Their evaluations on all test functions $f\in C^\infty(M)$ are equal,

$$
\nu(f) = \omega(f)
$$

- Their evaluations on every algebra at $f\in C^\infty(U)$, where $U$ is an open neighbourhood of $p$, are equal

$$
\nu(f) = \omega(f)
$$

- Their difference is the zero tangent vector in $T_p M$: $\nu - \omega = 0\in T_p M$. 


### Differential mechanisms
Let $F: M \to N$ be a smooth map between smooth manifolds with or without boundary (See page 61 for a dicussion on boundary). Fix $p\in M$, $\nu\in T_pM$, a test function $f\in C^\infty(N)$, and a curve $\gamma: (-\varepsilon,+\varepsilon)\to M$ starting at $p$.  the differential of $F$ at $p$ has the following properties

# Pushforward derivation
It maps $\nu\in T_p M$ to $dF_p(\nu)\in T_{F(p)}N$,

# Pullback test functions
It pulls $f\in C^\infty(N)$ into $f\circ F\in C^\infty(M)$,

# Pushforward of curves
The composition $F\circ\gamma$ is a curve starting at $F(p)$ with velocity $dF_p(\gamma'(0))$.

# Computations of pushforward derivation on test functions
The pushforward derivation $dF_p(\nu)$ of a test function $f\in C^\infty(N)$ is the derivation $\nu$ applied to the pullback $f\circ F$.

$$
dF_p(\nu)f = \nu(f\circ F)
$$

# Computations involving shifting curves
Let $\tau_b: t\mapsto t+b$, then

$$
(d\tau_b)\biggr|_{t_0}\biggl(\dfrac{d}{dt}\biggr|_{t=t_0}\biggr) = \dfrac{d}{dt}\biggr|_{t=\tau_b(t_0)} = \dfrac{d}{dt}\biggr|_{t=t_0+b}
$$

# Local Coordinate Representation
Depending on the rank of $dF_p$, the Rank Theorem tells us there exists coordinate charts in the domain and codomain such that it behaves like a linear map. It either removes coordinates ($dF_p$ not injective), adds zeros ($dF_p$ not surjective), or is the identity ($dF_p$ is full rank). 

$$
\operatorname{matrix}(\hat{F}) = \begin{bmatrix} 1 & 0 \end{bmatrix},\quad \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \quad \begin{bmatrix} 1 \end{bmatrix}
$$
The differential of a linear map is again a linear map, with respect to these charts, the differential: linearly embeds / linearly injects / is a linearly isomorphism of $T_pM$ into $T_{F(p)}$.

---

# Vector Fields on Manifolds
Recall the tangent bundle $TM$ on $M$ is equipped with its canonical projection $\pi: TM\to M$, that sends $(p,\nu)\mapsto p$, where $p\in M$ and $\nu\in T_p M$. A vector field $X: M\to TM$ is a (continuous) section st each element $p\in M$ is sent to an element in $T_p M$. Equivalently:

$$
\pi\circ X = \id{M}
$$

It is called smooth if it is a smooth section of $TM$, that is for every point $p\in M$, there exists charts $p\in (U,\varphi)$, $X(U)\subseteq (\pi^{-1}{(V)}, \widetilde{\psi})$

$$
\hat{X} = \widetilde{\psi}\circ X\circ \varphi^{-1}: \varphi(U)\to \widetilde{\psi}(\pi^{-1})(V))\quad \text{is smooth}
$$

Given a chart $(U,\varphi)$ on $M$, we can write $X\|U$ in its component functions:

$$
    X_p = X^{i}(p)\dfrac{\partial}{\partial x^i}\Biggr|_p
$$

where $\hat{X} = (x^1,\ldots, x^m, X^{1},\ldots, X^{m})$

Proposition 8.1 gives us an equivalent condition for smoothness. It suffices to check on the 'last $m$ coordinates' of $\hat{X}$. $X$ is smooth on $U$ if and only if its component functions $X^i$ are smooth.

---

### Extensions of Smooth Functions and Maps

- Lemma 2.26: Extension of smooth functions 

$A\subseteq M$ is closed, on a smooth manifold with or without boundary. Extend a vector valued function $f: A\to \real^k$. onto any open subset $U$ contianing $A$, with support contained in $U$. 

- Lemma 5.34: Extension of Functions on submanifolds

a) Require embedded submanifolds, any test function can be smoothly extended from $f\in C^\infty(S)$ to $\wig{f}\in C^\infty(U)$, where $U$ is an open subset containing $U$ (Rel $M$ of course). 

b) Require properly embedded, then we can take $U = M$.

- Technique: We can realize extensions, by multiplying $f$ with a suitable bump function, and using extension by zero.

---

### Restriction of Domain of Smooth Functions and Maps
- Prop 2.6: The restriction of a smooth function or map to every open subset is again smooth (with the open subset being considered as an open submanifold with codimension $0$).

- Theorem 5.27: Restricting the domain to submanifold, whether immersed or embedded submanifold, it is again smooth.

- Technique: We can realize restrictions by composting $F$ with an inclusion map.

---

### Gluing Lemmas
- Lemma A.20: Gluing Lemma for Continuous Maps
- Corollary 2.8: Gluing Lemma for Smooth Maps $M\to N$.


### Extensions of Frames and Fields

- Lemma 8.6: Extension Lemma for Vector Fields from closed sets

- Lemma 10.12: Extension Lemma for Vector Bundles

### Completions of Frames and Fields

- Prop 8.11: Completion of Local Frames for Tangent Bundles

- Prop 10.15: Completion of Local Frames for Vector Bundles


### Smoothness Criterion 

- Prop 8.1: Upgrade rough vector field using component functions of charts

- Prop 10.22: Upgrade rough sections using local frames


### Construction of Charts Lemmas

- Lemma 1.35: Smooth Manifold Chart Lemma

- Lemma 3.18: TM is a smooth $2n$-manifold

- Theorem 5.31: Uniqueness of the smooth structure on embedded submanifolds

- Lemma 10.6: Vector Bundle Chart Lemma

### Something acts locally

- Fix $\sigma_1$ and $\sigma_2$ and suppose $\sigma_1\vert_{U} = \sigma_2\vert_{U}$, subtract over, and extension by zero by a bump function $\theta\in C^\infty(M)$ where $\theta(p)=1$ and $\supp \theta\subseteq U$ . Define $\tau = \sigma_1-\sigma_2$. The resulting section

$$
(\theta\tau)(q)=\begin{cases}\theta(q)\tau(q)=0 & q\in U\\ \theta(q)\tau(q)=0 & q\notin U\end{cases}
$$

since $\tau\vert_{U}=0$ and $\theta\vert_{U^c}=0$, and $(\theta\tau)(p)=\theta(p)\tau(p)=\tau(p) = 0$. 

---

### Local Properties of Maps
- Lemma A.19: Continuity is Local.

- Prop 2.6: Smoothness is Local.

- Theorem 4.5: Inverse Function Theorem for Manifolds, if $dF_p$ invertible, then diffeomorphic on open connected nbhds.

- Theorem 4.12: Rank Theorem.

- Theorem 4.25: Local Embedding Theorem, smooth immersion iff every $p\in M$ has a nbhd st $F\vert_{U}:U\to N$ is a smooth embedding.

- Theorem 4.26: Local Section Theorem, smooth submersion iff every $p\in M$ is in the image of a smooth local section $\pi: U\to M$, where $U$ is an open subset of $N$.

---

## Submanifolds

# Embedded submanifold
- Subset $S\subseteq M$, endowed with subspace topology,

- Inclusion map is a smooth embedding.

# Immersed submanifold
- Subset $S\subseteq M$, endowed with an arbitrary topology,

- Inclusion map is a smooth immersion.

# Properly embedded submanifold
- Inclusion map is proper. $\iota^{-1}(K)$ is compact for every compact $K\subseteq M$.

We can manufacture embedded manifolds as follows:
If $F: N\to M$ is a smooth embedding, the range is a embedded submanifold of $M$. (Proposition 5.2)

Furthermore: $S = F(N)$, then $N$ is diffeomorphic with $S$, with dimension $\dim N$.

$$N\overset{\mathcal{D}}{\rightleftharpoons} S$$

# Critical and Regular Values
Let $F:M\to N$ be a smooth map. $p\in M$ is a *regular point* if $dF_p$ is a surjection. It is called a *critical point* if $dF_p$ is not a surjection.

Further, $q\in N$ is a *regular value* of $F$ if each point $p\in F^{-1}(q)$ in its (possibly empty) fiber is a regular value. $q\in N$ is a *critical value* of $F$ if there exists a point $p\in F^{-1}(q)$ whose differential $dF_p$ is not a surjection.

# Local k-slice condition

If $S\subseteq U$, and $S$ is some kind of level set with the last $n-k$ coordinates held fixed, then $S$ is a $k$-slice of $U$.

$$S = \pmap{\leq k}{U}\times c^{k+1}\times\cdots\times c^n$$

If $S$ is a subset of $M$, and 


# Local defining map
Given a embedded submanifold $S\subseteq M$, open subset $U\subseteq M$. A smooth map $\Psi\in C^\infty(U,N)$ is called a *local defining map* for $S$ if $U\cap S$ is a regular level set for $\Psi$ (with respect to charts on $M$).

If $N = \real^{m-k}$, then $\Psi$ is called a local defining function. If $U = M$, then it is called a *defining map* (resp. *defining function*).

Corollary: if $\Psi$ is a local defining function by vanishing $k$ coordinates in a slice chart $(U,\varphi)$ in $M$. We can restrict its domain from $U\mapsto U\cap S$, since $S$ is endowed with the subspace topology, and by Proposition 5.27, the resulting smooth map $\Psi\|_{U\cap S}$ is smooth. The differential of 

$$
d\Psi|_{U\cap S} = d\Psi|_{\iota(p)}\circ d\iota|_p\quad\text{is identically }0
$$

because $\Psi$ is constant on $U\cap S$. However, the differential of $\Psi$ on $U$ (with respect to the smooth structure on $M$) is not

$$
d\varphi|_p = \begin{bmatrix}
            \begin{array}{c|c}
                1_k & 0 \\
                \hline
                0 & 1_{m-k} \\
            \end{array}
        \end{bmatrix}\quad\text{and}\quad d\Psi|_p = \begin{bmatrix}
            \begin{array}{c|c}
                0 & 1_{m-k} \\
            \end{array}
        \end{bmatrix}
$$


# Immersed Manifolds Technique
The following is a technique to obtain slice charts for immersed manifolds. 

Let $S$ be an immersed manifold, by Proposition 5.22 (Immersed Submanifolds are Locallly Embedded), every point $p\in S$, has a neighbourhood $U$ Rel $S$, that is an embedded submanifold of $M$. 

This means $U$, endowed with the subspace topology, is an embedded manifold.

Using the local k-slice criterion on $U$, there exists a slice chart $(V,\varphi)$ in the smooth structure of $M$, such that $U$ is exactly a $k$-slice of $V$. 

This technique is used in Theorem 5.29 (Restricting Codomain)

---


# Proof Techniques

