---
layout: post
title: Notes on Smooth Manifolds
date: 2023-05-10 18:23
category: math
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

--- 

## smooth charts, structures, manifolds
Two charts are **smoothly compatible** if their domains are disjoint or 

$$
x_\beta\circ x_\alpha^{-1}\in C^{\infty}(\realn,\realn)
$$

where  $(U_\alpha, x_\alpha)$, $(U_\beta, x_\beta)$, $U_\alpha, U_\beta$ open in $\xx$, and $x_\alpha$ and $x_\beta$ are functions from $M\to \realn$ which are homeomorphisms between their domains and their ranges. 

**Sufficient condition** for two charts to be smoothly compatible: $x_beta\circ x_\alpha^{-1}$ is smooth and injective, and non-singular Jacobian at each point.

An **atlas** $\mathcal{A}$ is a collection of charts, whose domain form an open cover for $M$.

**Smooth atlas**: charts are pairwise smoothly compatible.

### motivation for smooth structure
Fix a topological manifold $M$, and with its charts. 

- A smooth atlas is called **maximal** if it is maximal by set inclusion, and is a smooth atlas. (lattice muscle).
- a **smooth structure** on $M$ is a maximal smooth atlas (not necessarily unique)
- a **smooth manifold** is a manifold + the smooth structure.

The choice of smooth atlases may not be unique. But we can assert some partial ordering business and see it is a lattice. (Lee Prop 1.17)
- every smooth atlas of a topological manifold $M$ is contained in a unique maximal smooth atlas. with 'maximal' referring to set inclusion. Recall an atlas is a collection of charts $(U_\alpha, x_\alpha)\in \mathcal{A}$.
- we can construct this maximal smooth atlas, called the **smooth structure determined by $\mathcal{A}$**, creating an equivalence class and sending each smooth atlas there.
- more precisely: two smooth atlases get sent to the same class if their union is again a smooth atlas that contains both of them. thus 'maximal'
- the second property: two smooth atlases over $M$ determine the same smooth structure iff their union is a smooth atlas (this is easy to see, use equivalence class muscle).



### smooth manifold chart lemma
Follows (Lee Lemma 1.35) closely. Gives a sufficient condition for a set $M$, together with sets $U_\alpha$, and functions $x_\alpha:U_\alpha\to\realn$ to be a 
- topological manifold
- which has a unique smooth manifold structure that makes each 'chart' a smooth chart.

The last definition we will need is the **smooth chart**: a chart that belongs to a maximal smooth atlas.

In english, if we have a smooth manifold (big smooth atlas on a top. space), we can choose smooth charts, which belong to this manifold. and any pair of (smooth) charts from this big atlas, is again smoothly compatible. 

and no chart outside this atlas (which is a subcollection of the family of charts on $M$), is smoothly compatible with ALL of the existing smooth charts.

--- 

## smooth functions
Let $M$ be a smooth $n$-manifold. A vector-valued function $f: M\to\real^k$ is a smooth function. If every point $p\in M$, induces a 
- smooth chart
- such that the euclidean space the chart is homeomorphic to, makes $f$ a smooth function 

$$f\circ x_\alpha^{-1}\in C^{\infty}(\realn,\real^k)$$

for each $f$ that is smooth. we define the **coordinate rep. of $f=\hat{f}$** 
- basically the same function but with domain an open subset of $\realn$.
- since $f:M\to\real^k$. Fix a chart $(U,\psi)$. For any point in the range of the chart (which is an open subset of $\realn$), 
- send it through the inverse chart $\psi^{-1}$ (to get the corresponding point in $M$) and send it into $f$.

$$
\hat{f}:\psi(U)\to\real^k,\quad \hat{f} = f\circ\psi^{-1}
$$

It is a fact that smooth functions are smooth with respect to every smooth chart. This is because for every point $p\in (U_\alpha,x_\alpha)$, either 

$$F\circ  x^{-1}_{\alpha} $$ is smooth, or $U_\alpha$ intersects some other chart $(U_\beta, x_\beta)$. So $Fx^{-1}_{\beta}$ is smooth, so is

$$
Fx^{-1}_{\beta}x_\beta x^{-1}_\alpha = Fx^{-1}_\alpha
$$

---

## smooth maps between manifolds
If $M$ and $N$ are smooth manifolds, a map $F:M\to N$ is called smooth, if at every point in its domain, $p\in M$, we can find smooth charts in $M$ and $N$, whose domain contains the $p$ and the range of $F(p)$ respectively. 

The two corresponding smooth charts are 'neighbourhoods' about the **point** $p$, and the set $F(U)$.

Concretely:
- $p\in M$ and there exists charts $(U, x)\in \mathcal{A}_M$, $(V, y)\in\mathcal{A}_N$ st

$$
F(p)\in U,\: F(U)\subseteq V
$$

and the '**coordinate rep. of $F\in C^{\infty}$**' (recall we have to fix a chart in the domain first, just like the **coordinate rep. of $f:M\to\real$**).

$$
\hat{F}= y \circ F\circ x^{-1}\quad \hat{F}\in C^{\infty}(\realn,\real^k)
$$

where $M$: dimension $n$, and $N$: dimension $k$.

### Continuity
in reality we have said nothing new, since $M$ and $N$ are locally homeomoprhic to some open subset of the $n,k$-plane. we simply passed the problem from a topological problem to a problem on $\real^n\to\real^k$ because of homeomorphisms.

Continuity of the map $F\in C(M,N)$, is nothing special. The inverse of a homeomorphism is again a homeomorphism. So we can drop the open sets through the pipeline. More precisely, if $p\in M$, then $F(p)$ induces a neighbourhood (or a smooth chart) about $F(p)\in (V,y)$, and because $F$ is smooth, $p\in (U,x)$ for some smooth chart wrt $M$ as well.

Fix an open set $W\subseteq N$ containing $F(p)$, 
- $F(p)\in W\implies F(p)\in W\cap V$ which is open Rel $V$. Send this open set (Rel $V$) into $\real^k$, since $y$ is a homeomorphism $y: V\to y(V)\subseteq\real^k$, or we can use the previous formula:

$$
F = y^{-1}\circ \hat{F}\circ x
$$

Similar to the 'change of basis' muscle in linear algebra (except $F$ may not be a homeomorphism, not even locally). The restriction of a continuous map is again continuous, and inverse images of `F|_U` are open (Rel $U$) iff they are open Rel $M$.

This is the 'translation' mechanism, between the coordinate charts $M$ and $N$, and the restriction of $F$ onto the domain of the chart in $M$.
