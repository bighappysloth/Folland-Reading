---
layout: post
title: Chapter 5 - Submanifolds
date: 2023-06-11 23:03
category: math
tags: ['math','manifold']
---
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


