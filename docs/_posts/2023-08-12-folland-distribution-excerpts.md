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