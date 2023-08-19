---
layout: article
title: Appendix for Functional Analysis
date: 2023-08-12 23:51
tags: ['distributions','distributional derivative','schwartz space','fourier transform','tempered distributions']
summary: 
---
# Folland Excerpts
## Chapter 5 - Frechet Space Convergence
![]({{ site.baseurl }}{% link /images/folland-5-15-part1.png %})
![]({{ site.baseurl }}{% link /images/folland-5-15-part2.png %})

## Chapter 8 - Multivariate Calculus
![]({{ site.baseurl }}{% link /images/folland-page-236.png %})
![]({{ site.baseurl }}{% link /images/folland-page-237.png %})

## Chapter 9 - Distribution and its Operations
![]({{ site.baseurl }}{% link /images/folland-page-284.png %})
![]({{ site.baseurl }}{% link /images/folland-page-285.png %})

![]({{ site.baseurl }}{% link /images/folland-9-3.png %})

![]({{ site.baseurl }}{% link /images/folland-page-295.png %})

# Inequalities

## Chapter 8
<div class="lemma-box" markdown=1 name="">
For any $N\in\mathbb{N}^+$, if $\beta$ is a multi-index with $\vert \beta\vert\leq N$, then

$$
\vert x^{\beta}\vert \leq (1+\vert x\vert)^N
$$

</div>
<div class="proof-box" markdown=1 proof-name="">
Expanding the left and right hand sides, we see

- LHS

    $$
    \biggl\vert\prod_{i\leq n} x_i^{\beta_i}\biggr\vert = \prod_{i\leq n} \vert x_i\vert^{\beta_i}
    $$

- RHS

    $$
    \biggl( 1 + \biggl(\sum_{i\leq n}\vert x_i\vert ^2\biggr)^{1/2}\biggr)^{N}
    $$

The estimate clearly holds for $N=0$. Hypothesize it holds for $N-1$, if $\beta$ is a multi-index with order $\vert\beta\vert\leq N-1$, then

$$
\vert x^{\beta}\vert\leq (1+\vert x\vert)^{N-1}\leq (1+\vert x\vert)^N
$$

Assume $\vert\beta\vert = N-1$, and we multiply by any coordinate $\vert x_i\vert$, to the left and right hand sides of the equation, and see that 

$$
\vert x_i\vert\cdot\vert x^{\beta}\vert\leq \vert x_i\vert\cdot (1+\vert x\vert)^{N-1}\leq (1+\vert x\vert)^{N}
$$

</div>
<div class="lemma-box" markdown=1 name="">
If $\alpha$ is any multi-index, then

$$
\vert x^\alpha\vert \leq (1+\vert x\vert^2)^{\vert\alpha\vert/2}
$$

</div>
<div class="proof-box" markdown=1 proof-name="">
We will use induction on the order of $\alpha$. If $\vert\alpha\vert=0$, both sides are equal to $1$. Assume it holds for $\vert\alpha\vert = 0,1,\ldots, N-1$, and for any multi-index $\beta$ with order $\vert\beta\vert = N$, there exists a (not necessarily unique) multi-index $\alpha$ of order $\vert\alpha\vert = N-1$, such that $\beta-\alpha = e_j$.

By induction hypothesis, we see taht 

$$
\vert x^\alpha\vert = \prod_{j\leq n}\vert x^{\alpha_j}_{j}\vert\leq (1+\vert x\vert^2)^{\vert\alpha\vert/2}
$$

Multiplying by the coordinate function $\vert x_j\vert$, similar to the previous proof. 

$$
\vert x^{\beta} \vert = \vert x_j\vert\cdot \vert x^{\alpha}\vert\leq \vert x_j\vert \cdot (1+\vert x\vert^2)^{\vert\alpha\vert/2}
$$

Since the "$L^1$ cosine" is less than $1$, meaning

$$
\dfrac{\vert x_j\vert}{\sqrt{1+\vert x\vert ^2}}\leq 1
$$

This implies $$\vert x^{\beta}\vert\leq (1+\vert x\vert^2)^{\vert\beta\vert/2}$$.


</div>
<div class="remark-box" markdown=1 name="">
To show the $L^1$ cosine inequality, the projection map $x\mapsto x_j$ is norm-decreasing; as $\realn$ is a Hilbert space with the standard inner product. And $\vert x\vert^2\leq 1 + \vert x\vert ^2$.
</div>

# Hofer Chapter 3

## Equivalence of $H_s$ for $s\geq 0$
<div class="remark-box" markdown=1 name="">
The following is incomplete.
</div>
For convenience we will set $\dzz'=\dzz'(\Torusn)$, and $C^\infty = C^\infty(\Torusn)$.

Comparing the two characterizations of $H_s$,

$$
H_s^1 = \bigset{f\in L^2(\Torusn,dx),\: \sum_{k\in\mathbb{Z}^n}\vert k\vert^{2s}\vert\hat{f}(k)\vert^2<+\infty}
$$

and

$$
H_s^2 = \bigset{f\in \dzz',\: \sum_{k\in\mathbb{Z}^n}(1+\vert k\vert^2)^s\vert\hat{f}(k)\vert^2 <+\infty}
$$

Since $(1+\vert k\vert^2)^{s}\geq \vert k\vert^{2s}$ for $k\in\mathbb{Z}^n$, we see that $H_{s}^1\subseteq H_{s}^2$. If $f\in H_s^2$, then 

$$
\sum_k ()
$$

$$
\sum_{j\in\mathbb{Z}^n} (1+\vert j\vert^2)^{s}\cdot\vert \hat{f}(k)\vert^2\quad\text{and}\quad\sum_{j\in\mathbb{Z}^n} \vert j\vert^{2s}\cdot \vert \hat{f}(k)\vert^2
$$

It is clear the left member is greater than the right, and 

## Vector-valued $L^p$ spaces
We begin with the scalar-valued output case. 
<div class="definition-box" markdown=1 name="$L^2$ inner product">
If $f,g\in L^2(A,\real)$, we define

$$
\langle f,\: g\rangle_{L^2(A,\real)} = \int \langle f(t),\: g(t)\rangle_{\real}dt
$$

</div>

The case $f,g\in L^2(A,\real^{k})$ is similar. But first, we state the definition of $L^2$ for vector-valued functions for completeness.

<div class="definition-box" markdown=1>
Let $n$ be a positive integer, we define

$$
L^2(A,\real^{k}) = \bigset{f = (f_1,\ldots,f_{k}),\: f_i\in L^2(A,\real)\quad \forall i\leq k}
$$

More generally, if $p\in\real$, we define

$$
L^p(A, \real^{k}) = \bigset{f=(f_1,\ldots,f_k),\: f_i\in L^p(A, \real)\quad\forall i\leq k}
$$

where $A$ is any measurable subset of $\real$. 

</div>


<div class="definition-box" markdown=1 name="$\real^{k}$ inner product">
the *inner product* on $\real^{k}$ between two vectors $v$ and $w$ is defined as the sum of the component scalar products,

$$
\langle v,w\rangle_{\real^{k}} = \sum_{i\leq k}\langle v^i, w^i\rangle_{\real}
$$

Applying Cauchy-Schwartz for $i\leq k$ gives

$$
\vert\langle v,w\rangle_{\real^{k}}\vert\leq \sum \vert \langle v^i, w^i\rangle_{\real}\vert\leq \sum \vert v^i\vert\cdot\vert w^i\vert
$$

</div>

<div class="definition-box" markdown=1 name="$L^2(A,\real^{k})$ inner product">
We define the inner product on $L^2(A,\real^{k})$ as the integral over the pointwise inner product. 

$$
\langle f,\: g\rangle_{L^2} = \sum_i \int \langle f^i(t), g^i(t)\rangle_\real dt
$$

The integrals in the sum above converges absolutely. For $i\leq k$, we have  

$$
\begin{align}
\int \vert\langle f^i(t),\: g^i(t)\rangle\vert dt &\leq \int \vert f^i\vert\cdot\vert g^i\vert dt\\
&\leq \norm{f^ig^i}_{L^1(A,\real)}\\
&\leq \norm{f^i}_{L^2(A,\real)}\cdot \norm{g^i}_{L^2(A, \real)}
\end{align}
$$

</div>



<div class="lemma-box" markdown=1>
Let $f,g\in L^2(A,\real^{k})$, the integral over the *pointwise inner product* of $x$ and $y$,


$$
\begin{align}
\int \langle f(t),\: g(t)\rangle_{\real^{k}} \: dt &= \int \sum_i \langle f^i(t), g^i(t)\rangle_\real dt\\
&= \sum_i \int \langle f^i(t), g^i(t)\rangle_\real dt\\
&= \langle f,\: g\rangle_{L^2(A, \real^{k})}
\end{align}
$$

converges absolutely. Furthermore, 

$$
\langle f,\: g\rangle_{L^2(A,\real^{k})} = \int \langle f(t),\: g(t)\rangle_{\real^{k}}dt
$$

</div>
<div class="definition-box" markdown=1 name="$L^p$ norm for vector-valued functions">
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
Holder's Inequality for vector-valued $L^p$ functions. Let $A$ be a Borel subset of $\real$, and $p\in [1,+\infty]$. If $f,g\in L^p, L^q$ respectively, then the $L^{(p,q)}(A,\real^k)$ product converges absolutely. And

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
