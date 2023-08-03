---
layout: article
title: notes on compactness
date: 2023-05-15 15:46
category: math
---
Compactness by itself kinda means nothing, it has to be tied to some additional structure.

In most cases you'll see compactness in Hausdorff spaces, which means a couple things:

Ordinarily, if you have a continuous function $f:\xx\to\yy$, where $\xx$ and $\yy$ are any topological spaces, one cannot deduce any topological information from $\xx$ into $\yy$.

But if $\yy$ is Hausdorff, and $\xx$ is compact, then 

$f(\xx)$ is compact, and it maps closed sets into closed sets. If $f$ is a bijection, then you a very nice homeomorphism for free essentially.

Compactness is quite abundant, closed balls in $\realn$ are compact, and in any finite dimensional vector space (see chapter on Local compactness).

That aside, 'compactness' allows you to extend 'local' properties, to 'global' properties.

Example: if $\xx$ is a compact metric space, then every continuous function from $\xx$ to $\mathbb{C}$ is uniformly continuous. Continuity here is a local phenomenon, and compactness allows us to extends to a global property through compactness. To see this, recall the definition for continuity. At every point $x\in \xx$, and if $\varepsilon>0$, there exists a neighbourhood about $x$, denoted by $U$, such that

$$
    x\in U\subseteq f^{-1}(B(\varepsilon, f(x)))
$$

**Points within this neighbourhood $U$ are $2\varepsilon$-uniformly continuous** (!!!), this is clear after a triangle-inequality argument. Suppose $y$ and $z$ are in $U$, then

$$
    \norm{f(y)-f(z)}\leq \norm{f(x)-f(y)} + \norm{f(x) - f(z)}< 2\varepsilon
$$

Now, if $\xx$ is a compact metric space, let $x$ range through all the points of $\xx$, and at each $x$, find an open ball of radius $\delta>0$ such that points within this ball are $\varepsilon/3$ uniformly continuous. For every $y,z$ with $d(y,x)<\delta$, $d(z,x)<\delta$ implies

$$
|f(y)-f(z)|<\varepsilon/3
$$

For the same $\delta>0$, let $\xx$ be covered by balls of the form

$$
B(\delta(x)3^{-1}, x),\: x\in \xx
$$


this induces a finite subcollection, $$\{B(\delta(x_{j})3^{-1},x_{j})\}$$. Now let $\delta = \min \delta(x_j)$. And let $y,z\in \xx$ with $d(y,z)<\delta/3$, each of the two points lie in balls with centers indexed by $j$ and $k$ (where $j$ is not necessarily equal to $k$). 

*We will show this doesn't matter since $x_j$ and $x_k$ each lie within $\delta$ distance of the other, and everythig works out nicely using the Triangle Inequality in $\mathbb{C}$.*

$$
\begin{cases}y\in B(\delta(x_j)3^{-1}, x_{j})\\ z\in B(\delta(x_k)3^{-1}, x_{k})\end{cases}\implies d(x_j,x_k)\leq d(x_k,z) + d(x_j,y) + d(y,z)<\delta
$$

Hence, $\norm{f(x_j) - f(x_k)}<\varepsilon/3$. Furthermore, both $f(y)$ and $f(z)$ lie within $\varepsilon/3$ distance from $f(x_j)$ and $f(x_k)$. Combining everything reads

$$
\norm{f(y)-f(z)}\leq \norm{f(x_j)-f(x_k)} + \norm{f(y)-f(x_j)} +\norm{f(z) - f(x_k)}<\varepsilon
$$

Example: Another exmaple of how compactness allows us to extend local properties to global ones is that of regularity. See [here]({{ site.baseurl }}{% link /download/Lee-Appendix_A_Compiled.pdf %}).
