---
layout: post
title: smooth manifolds
date: 2023-05-09 20:16
category: manifolds
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

## smooth functions
Let $M$ be a smooth $n$-manifold. A vector-valued function $f: M\to\real^k$ is a smooth function. If every point $p\in M$, induces a 
- smooth chart
- such that the euclidean space the chart is homeomorphic to, makes $f$ a smooth function 

$$f\circ x_\alpha^{-1}\in C^{\infty}(\realn,\real^k)$$

for each $f$ that is smooth. we define the **coordinate rep. of $f$** 
- combine ch