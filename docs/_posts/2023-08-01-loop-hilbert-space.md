---
layout: article
title: Sobolev Spaces for Closed Characteristics
date: 2023-08-01 02:51
category: 
author: 
tags: ['symplectic']
summary: 
---
# Misc Notes


## $L^2(S^{1},\real^{2n})$ and its operations
We begin with the scalar-valued output case. 
<div class="definition-box" markdown=1>
If $f,g\in L^2(S^{1},\real)$, we define

$$
\langle f,\: g\rangle_{L^2(S^1,\real)} = \int \langle f(t),\: g(t)\rangle_{\real}dt
$$


</div>


The case $f,g\in L^2(S^1,\real^{k})$ is similar. But first, we state the definition of $L^2$ for vector-valued functions for completeness.
<div class="definition-box" markdown=1>
Let $n$ be a positive integer, we define

$$
L^2(S^1,\real^{k}) = \bigset{f = (f_1,\ldots,f_{k}),\: f_i\in L^2(S^1,\real)\quad \forall i\leq k}
$$

More generally, if $p\in\real$, we define

$$
L^p(A, \real^{k}) = \bigset{f=(f_1,\ldots,f_k),\: f_i\in L^p(A, \real)\quad\forall i\leq k}
$$

where $A$ is any measurable subset of $\real$. 

</div>


<div class="definition-box" markdown=1>
the *inner product* on $\real^{k}$ between two vectors $v$ and $w$ is defined as the sum of the component scalar products,

$$
\langle v,w\rangle_{\real^{k}} = \sum_{i\leq k}\langle v^i, w^i\rangle_{\real}
$$

Applying Cauchy-Schwartz for $i\leq k$ gives

$$
\vert\langle v,w\rangle_{\real^{k}}\vert\leq \sum \vert \langle v^i, w^i\rangle_{\real}\vert\leq \sum \vert v^i\vert\cdot\vert w^i\vert
$$


</div>

<div class="definition-box" markdown=1>
We define the inner product on $L^2(S^1,\real^{k})$ as the integral over the pointwise inner product. 

$$
\langle f,\: g\rangle_{L^2} = \sum_i \int \langle f^i(t), g^i(t)\rangle_\real dt
$$

The integrals in the sum above converges absolutely. For $i\leq k$, we have  

$$
\begin{align}
\int \vert\langle f^i(t),\: g^i(t)\rangle\vert dt &\leq \int \vert f^i\vert\cdot\vert g^i\vert dt\\
&\leq \norm{f^ig^i}_{L^1(S^1,\real)}\\
&\leq \norm{f^i}_{L^2(S^1,\real)}\cdot \norm{g^i}_{L^2(S^1, \real)}
\end{align}
$$

</div>



<div class="lemma-box" markdown=1>
Let $f,g\in L^2(S^{1},\real^{k})$, the integral over the *pointwise inner product* of $x$ and $y$,


$$
\begin{align}
\int \langle f(t),\: g(t)\rangle_{\real^{k}} \: dt &= \int \sum_i \langle f^i(t), g^i(t)\rangle_\real dt\\
&= \sum_i \int \langle f^i(t), g^i(t)\rangle_\real dt\\
&= \langle f,\: g\rangle_{L^2(S^1, \real^{k})}
\end{align}
$$

converges absolutely. Furthermore, 

$$
\langle f,\: g\rangle_{L^2(S^1,\real^{k})} = \int \langle f(t),\: g(t)\rangle_{\real^{k}}dt
$$


</div>
<div class="definition-box" markdown=1>
Let $f\in L^p(A,\real^k)$, where $A$ is a Borel subset of $\real$, we define the $p$-norm of $f$ by

$$
\norm{f}_{L^p(,\real^k)} = \biggl(\sum_i\norm{f^i}_{L^p(A,\real)}^p\biggr)^{1/p}
$$

If $p=+\infty$, define $$\norm{f}_{L^{\infty}(A,\real^k)} = \sup_{i\leq k}\norm{f^i}_{\infty}$$.
</div>
<div class="definition-box" markdown=1>
Let $p$ and $q$ be conjugate exponents. If $p$ is a reflexive exponent (hence so is $q$), we write

$$
\langle f^i, g^i\rangle_{L^{(p,q)}(A,\real)} = \int_A f^i(x)g^i(x) dx
$$

for $f^i\in L^p(A,\real)$ and $g^i\in L^q(A,\real)$. If $p=1$ or $p=+\infty$, by abuse of notation we shall use $\langle f^i, g^i\rangle$ to refer to the integral over the pointwise product. 
</div>


<div class="definition-box" markdown=1>
Generalizing to the vector-valued case, let $f\in L^p(A,\real^k)$ and $g\in L^q(A,\real^k)$. We define the *$L^{(p,q)}(A,\real^k)$ product of $f$ and $g$ by*

$$
\langle f,\: g\rangle_{L^{(p,q)}(A,\real^k)} = \sum_i\langle f^i,\: g^i\rangle_{L^{(p,q)}(A,\real)}
$$

To simplify the notation, we sometimes omit the domain and the codomain in the subscripts,

$$
\norm{f}_{L^{p}(A,\real^k)} = \norm{f}_p,\quad\text{and}\quad \langle f,\: g\rangle_{L^{(p,q)(A,\real^k)}} = \langle f,\: g\rangle_{(p,q)}
$$

</div>
<div class="theorem-box" markdown=1>
The $p$-norm above indeed defines a norm on $L^p(A,\real^k)$.
</div>
<div class="proof-box" markdown=1 proof-name="">
It is clear that $L^p$ is a vector space (over $\real$). Absolute homogeneity and the triangle inequality follows immediately from the definition, and considering the properties of $\norm{\cdot}_{L^p(A,\real)}$. Definiteness comes from checking one each component function.
</div>
<div class="theorem-box" markdown=1>
Holder's Inequality for vector-valued $L^p$ functions. Let $A$ be a Borel subset of $\real$, and $p\in [1,+\infty]$. If $f,g\in L^p(A,\real^k)$, the $L^{(p,q)(A,\real^k)}$ product converges absolutely, and

$$
\vert \langle f,\: g\rangle_{(p,q)}\vert \leq \norm{f}_p\cdot\norm{g}_q
$$

</div>
<div class="proof-box" markdown=1 proof-name="">
If $p\neq 1$, consider this sequence of inequalities

$$
\begin{align}
\vert\langle f,\: g\rangle_{(L^p, L^q)}\vert &\leq \sum\biggl\vert\langle f^i, g^i\rangle_{L^{(p,q)}(A,\real)}\biggr\vert\\[1ex]
&\leq\sum \int_A\biggl\vert f^i(x)g^i(x) \biggr\vert dx\\[1ex]
&\leq\sum \norm{f^i}_{p}\cdot\norm{g^i}_{q}\\[1ex]
&\leq \norm{f}_p\cdot\norm{g}_q
\end{align}
$$

for the last inequality we used Holder's Inequality for finite sums (with respect to the counting measure). If $p=1$, we have

$$
\begin{align}
\vert \langle f,\: g\rangle_{(1,+\infty)} &\leq \sum \vert \langle f^i,\: g^i\rangle_{(1,+\infty)}\vert\\
&\leq \sum_i \norm{f^i}_{1}\cdot\norm{g^i}_{\infty}\\
&\leq \sum_i \norm{f^i}_{1}\cdot (\sup_{j}\norm{g^j}_{\infty})\\
&\leq (\sup_{j}\norm{g^j}_{\infty})\cdot \sum_i \norm{f^i}_{1}\\
&\leq \norm{f}_{1}\cdot\norm{g}_{\infty}
\end{align}
$$


</div>

## Proposition 5
We define the $L^2$ Sobolev spaces on $S^1$ in the notation of Hofer, 
- $$H^s = \bigset{f\in L^2(S^1,\real^{2n}),\: \sum_{k\in\mathbb{Z}} \vert k\vert^{2s}\vert\hat{f}(k)\vert^2<+\infty}$$
- $H^s$ is equipped with inner product
$$
\langle x,y\rangle_{(s)} = \langle x_0, y_0\rangle + 2\pi \sum_{k\in\mathbb{Z}}\vert k\vert^{2s}\langle x_k, y_k\rangle
$$

    and 

    $$\lVert x\rVert_{(s)}^2 = (\langle x,x\rangle)^{1/2} = \biggl(\lVert x_0 \rVert_{\real^{2n}}^2 + \biggl(2\pi\sum_{k\in\mathbb{Z}}\vert k\vert^{2s}\lVert x_k \rVert_{\real^{2n}}^2\biggr)\biggr)^{1/2}$$

Consider the inclusion map $j: H^{1/2}\to L^2$, where both are Hilbert Spaces (to be proven). Identifying their dual through the Riesz isomorphism, 

$$
j^*: L^2\to H^{1/2},\quad \langle j(x), y\rangle_{L^2} =\langle x, j^*(y)\rangle_{H^{1/2}}
$$

for every $x\in H^{1/2}$ and $y\in L^2$. The statement of Proposition 5 is as follows 