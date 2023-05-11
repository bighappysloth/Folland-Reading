---
layout: post
title: Notes on Smooth Manifolds
date: 2023-05-10 18:23
tags: ['manifolds','john lee', 'smooth manifolds']
---
Rough draft, do not expect anything or everything below to be correct.

An $n$-dimensional topological manifold is a $T_2$, second-countable, 'locally Euclidean of dimension $n$' topological space.

Every $p\in M$ induces an open neighbourhood and a homeomorphism that bijects this open neighbourhood to some open subset of $\realn$.

## Exercise 1.1

Show that equivalent definitions of manifolds are obtained if instead of allowing $U$ to be homeomorphic to any open subset of $\realn$, we require it to be homeomorphic to an open ball in $\realn$, or to $\realn$ itself.

If $M$ is a topological manifold (of dim $n$) as defined above. Fix a point $p\in M$. so
- Since the range of the map $\phi: U_M\to \phi(U_M)$ is open in $\realn$. We can wrap $\phi(p)$ in an open ball.
- $\phi(p)\in B(\varepsilon, \phi(p))\subseteq U_{\realn}$
- By Munkres 18.2, the restriction of a continuous function is again continuous. To obtain a new homeomorphism, we can 'restrict' the coordinate map $\phi$ onto $\phi^{-1}B$ where $B$ denotes the ball (at this point, do we really care about the radius and the center of the ball?)
- The map 

$$
\phi|\phi^{-1}(B): \phi^{-1}(B)\to B = \text{ball in }\realn
$$

is a homeomorphism.

- Conversely, every ball is an open set in $\realn$. So $2/3$ of the definitions are equivlant.

- Finally, $\realn$ is homeomorphic to an open ball centered at the origin, if we consider equivalent metrics,

$$
d'(x,y) = \dfrac{d(x,y)}{1 + d(x,y)}
$$

the proof for this is in any undergraduate analysis text.

- therefore the three definitions are equivalent.

# coordinate charts
We dump all the relevant definitions

- coordinate chart is a pair, $(U,\phi)$, the domain and the homeomorphism
- coordinate domain, is the domain
- coordinate ball, if the **range** of a coordinate chart, is an open ball in $\realn$, then we call $U$ a coordinate ball. This roughly means that every point in this ball has 'Euclidean ball-like structure, like connectedness, etc'
- coordinate cube, same thing
- if $p$ is a point in the manifold, it induces some chart, and the vector it generates in $\realn$ are called **local coordinates**

$$
\phi(p) = \underbrace{\begin{bmatrix}x^1 & \ldots & x^n\end{bmatrix}^T}_{\text{local coordinates}}
$$

# Lemma 1.10
Every topological manifold has a countable basis of pre-compact coordinate balls.

The outline for the proof runs as follows:
- first we zoom in on a chart in the manifold. why? Because the subspace topology inherits hausdorff, and second-countable. and we can pick the subspace chart itself, so **every chart is itself a manifold**.
- There exists a coordinate map $\psi: M\to V$, $V$ is open in $\realn$.
- because $\realn$ is second countable, let $$\{ B_{j\geq 1} \}$$ be the countable collection of open balls, at *rational centers and with rational radius* whose union is $V$. (this already implies $B_j\subseteq V$ at each $j\geq 1$)
- Take the inverse image of such balls, and

$$
\{\psi^{-1}(B_j)\} \text{ forms an open cover for one chart }(U,\psi) 
$$

this holds for any chart $M$. If $M$ possesses a collection of charts $$\{(U_\alpha,\: \psi_{\alpha})\}$$

- Let $\alpha$ run through all the charts. So that 

$$
\bigset{\psi_\alpha^{-1}(B_j),\: j\geq 1,\: \alpha\in A} \text{ covers each } U_\alpha \text{ hence covers } M
$$

- $M$ is a manifold, so it is second countable. Every open cover for $M$ posses a countable subcover. To see this, let $$\{E_k\}_{k\geq 1}$$ be a countable basis for $M$. Each **non-empty** element in the open cover $\psi^{-1}_\alpha(B_j)$ has some basis element $E_k$ as an open subset, in symbols:

$$
E_k\subseteq \psi_\alpha^{-1}(B_j)
$$

Hence, there is a subcollection of indices taken from $\nat^+$, and it suffices to choose the $\alpha$'s that have a corresponding $k$ that lands in the subcollection. 

Why is this true? Fix a point $x\in \bigcup_{\alpha,j} \psi^{-1}_\alpha(B_j)$, because $E_k$ is a basis, there exists a basis element $E_k$ has to 'squeeze' in between $$\{x\}$$ and $$\psi^{-1}_{\alpha}(B_j)$$

$$
x\in E_k\subseteq \psi^{-1}_{\alpha}(B_j)
$$

and these $E_k$ are precisely the ones in the subcollection of indices, hence we can find some $\beta$ and a $j\geq 1$ (not necessarily equal), $x\in E_k\subseteq \psi_\beta^{-1}(B_j)$.

# Proposition 1.11

The book introduces the notion of local finiteness. We will instead substitute this section with the relevant Chapters from Munkres [here]({% post_url 2023-05-10-munkres-chap-39-42 %}).