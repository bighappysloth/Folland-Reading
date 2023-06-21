---
layout: post
title: Chapter 6 - Sard's Theorem
date: 2023-06-15 16:24
category: math
tags: ['math','manifold']
---
## Measure Zero
Use the ordinary outer-measure definition. A subset $E\subseteq\realn$ has *measure zero* if 

$$
\mu(E) = \bigset{\sum \mu(U_{j\geq 1}),\quad E\subseteq\bigcup U_{j\geq 1}} = 0
$$

We sometimes call measure zero sets *null* sets.

# Properties of Measure zero
Subadditivity: the countable union of null sets is again a null set.

Monotonicity: If $E\subseteq N$ where $N$ is null, then $E$ is null (provided that $E$ is measurable, or the measure is *complete*).

Smooth maps send null sets to null sets: If $F:M\to N$ is a diffeomorphism, $F(E)$ is null iff $E$ is null.

Fubini's Condition: Let $A\subseteq\realn$. Suppose for every $c\in\real$, the set

$$
A_c = \bigset{x\in\real^{n-1},\: (c,x)\in A}
$$

is a null, then $A$ is null. Proof: apply Fubini's Theorem.


# Taylor's Theorem with Remainder
Let $F\in C^\infty(\realm,\realn)$, and define the $l$-th order expansion at $a$ by $P_l(\cdot, a)$

$$
P_l(x,a)\overset{\Delta}{=} F(a) + \sum_{1\leq\|\alpha\|\leq l}[\partial^\alpha F(a)][x-a]^{\alpha}(\|\alpha\|!)^{-1}
$$

Where $\alpha$ represents a $m$-[multindex](https://en.wikipedia.org/wiki/Multi-index_notation).

## Tubular Neighbourhood Issues
Let $M$ be an embedded submanifold of $\realn$. What exactly is $N_xM$? 

$$
T_x M\subseteq T_x\realn,\quad\text{and}\quad N_xM\subseteq T_x\realn
$$



where $N_xM$ consists of all vectors that are orthgonal to $T_xM$. (Is orthgonality basis independent?)

Normal bundle: $$NM = \bigset{(x,v)\in\realn\times\realn,\quad x\in M,\: v\in N_xM}$$

# Retracing from Chapter 3

Let $a\in\realn$, then the geometric tangent space $\real^n_a$ is the set $$\bigset{(a,v),\: v\in\realn}$$