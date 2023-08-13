---
layout: article
title: Functional Analytic setting for Closed Characteristics
date: 2023-08-01 02:51
category: 
author: 
tags: ['symplectic']
summary: 
---
# Functional Analysis
## Function spaces and their topologies

- Let $E\subseteq \realn$ be any subset.

    $$
    C_c^\infty(E) = \bigset{f\in C_c^\infty(\realn),\: \supp{f}\subseteq E}
    $$

- We denote $\mathcal{D} = C_c^\infty(\realn) = C_c^\infty$, and $\mathcal{D}(E) = C_c^\infty(E)$ for an arbitrary $E\subseteq\realn$.
- If $U\subseteq\realn$ is open, then $\mathcal{D}(U)$ can be written as the countable union of compact subsets of $U$. (Recall if $\xx$ is LCH and $\sigma$-compact, then so is any open $U\subseteq \xx$ in the subspace topology, Folland Exercise 4.55).
- If $K\subseteq\realn$ is compact, $\mathcal{D}(K)$ is a *Frechet space* with the norm

    $$
    \phi\mapsto \norm{\partial^\alpha \phi\vert_{K}}_u = \sup_{x\in K}\vert \partial^\alpha \phi(x)\vert  = \sup_{x\in \realn}\vert\partial^\alpha \phi(x)\vert = \norm{\partial^\alpha\phi}_u
    $$

<div class="definition-box" markdown=1 name="Schwartz Space">
We define a subspace of functions in $C^\infty$ called the **Schwartz Space**. It is the space of smooth functions whose partials are rapidly decreasing.

$$
\szz = \bigset{f\in C^\infty,\: \norm{f}_{(N,\alpha)}<+\infty \quad \text{for all }N,\alpha}
$$

where $$\norm{f}_{(N,\alpha)} = \sup_{x\in\real^{n}}(1 + \vert x\vert)^N\vert\partial^\alpha f(x)\vert$$.
</div>
<div class="definition-box" markdown=1 name="Space of slowly-increasing smooth functions $C_{s}^\infty$">
Slowly-increasing: all partials can be dominated by polynomials.

$$
C_{s}^\infty = \bigset{f\in C^\infty,\: \vert \partial^\alpha f(x)\vert \Lsim_{\alpha} (1+\vert x\vert)^{N(\alpha)},\text{ for all }\alpha}
$$

</div>
<div class="lemma-box" markdown=1 name="Density Lemma">
The following inclusions are dense. We say **$p$ is usual** if $p\in [1,+\infty)$, and **$p$ is reflexive** if $L^p$ is.

- If $(\xx,\mcal,\mu)$ is any measure space, the space of $L^1$ simple functions, $\Sigma_{1}\subseteq L^p$ for usual $p$ and $p=+\infty$,

- If $\xx$ is LCH and $\mu$ a Radon measure, $C_c(\xx)\subseteq L^p(\mu)$ for usual $p$,

- Lusin: If $\xx$ and $\mu$ are inherited from the previous bullet point, any measurable function $f$ can be uniformly approximated by $\phi\in C_c(\xx)$, with $\phi=f$ on $\xx\setminus A$, where $\mu(A)<\varepsilon$,

- Stone: The complex exponentials $(E_{k})_{k\in\mathbb{Z}^n}$,
    
    $$E_k(x) = \exp(2\pi i\langle k,x\rangle),\quad x\in\mathbb{T}^n$$
    
    are dense in $C(\mathbb{T}^n)$ in the uniform norm, and $(E_k)_{k\in \mathbb{Z}^n}\subseteq L^2(\mathbb{T}^n)$.

- $C_c^\infty\subseteq\szz\subseteq L^p$ for usual $p$ on $\realn$,
- $C_c^\infty\subseteq\szz\subseteq C_0$, where $C_0$ are the continuous functions that **vanish at infinity**  on $\realn$,
- $C_c^\infty\subseteq C^\infty$, where $C_c^\infty$ is LF and $C^\infty$ is equipped with the Frechet topology of compact convergence on $\realn$.

</div>

## Fourier Transform on $\real^n$
<div class="definition-box" markdown=1 name="">
Let $f\in L^1(\realn) = L^1$, we define the **Fourier Transform of $f$** to be the map $\mathcal{F}f: \real^n\to\mathbb{C}$,

$$
\mathcal{F}f(\zeta) = \int_{\realn}f(x)e^{-2\pi i\langle \zeta,x\rangle}dx = \int_{\realn} f(x)E_{-\zeta}(x)dx
$$

</div>

<div class="lemma-box" markdown=1 name="">
The Fourier Transform of an integrable function is always bounded and continuous (identified a.e), and $\mathcal{F}(L^1)\subseteq BC(\realn)$, and 

$$\norm{\hat{f}}_u\leq \norm{f}_1$$

</div>

<div class="theorem-box" markdown=1 name="">
Basic properties of the Fourier Transform
- The integral defining $\mathcal{F}$ converges for $L^1 + L^2$, and
- Hausdorff Young: if $1\leq p\leq 2$ and $q$ is conjugate to $p$, 
    
    $$
    \norm{\hat{f}}_q\leq\norm{f}_p
    $$

- Algebraic Properties ![Folland 8.22]({{ site.baseurl }}{% link /images/folland-8-22.png %})
- Riemann-Lebesgue: $\mathcal{F}$ maps $L^1$ to $C_0$, and
- If $f$ and $\hat{f}$ are in $L^1$, then $\breve{\hat{f}} = \hat{\breve{f}}=f_0$ a.e, and $f_0$ is continuous.
</div>
<div class="theorem-box" markdown=1 name="">
Fourier Transform and its isomorphisms
- $\mathcal{F}$ is a **linear isomorphism** from $\szz$ into itself, (linear and continuous),

- $\mathcal{F}$ is a **unitary isomorphism** form $L^2$ into itself.

    $$
    \norm{\hat{f}}_2=\norm{f}_2\quad\text{and}\quad\langle f,g\rangle_{L^2} = \langle \hat{f},\hat{g}\rangle_{L^2}
    $$
 
- We have yet to define the Fourier Transform on the space of tempered distributions, but it is true that $\mathcal{F}$ extends continuously to a **linear isomorphism** from $\szz'$ into itself.
</div>

<div class="remark-box" markdown=1 name="">
$T\in \mathcal{L}(\xx,\yy)$ where $\xx$ and $\yy$ are Banach spaces is an **isometry** if $\norm{Tx} = \norm{x}$ for every $x\in \xx$. A **linear isomorphism** between Banach spaces is any continuous, invertible map. Furthermore, if $\xx$ and $\yy$ are Hilbert spaces, $T$ is a **unitary isomorphism** if $T$ is invertible, and 

$$
\langle Tx, Ty\rangle = \langle x,y\rangle
$$

It can be shown (Folland 5.55) $T$ is a unitary isomorphism iff it  surjective linear isometry.

</div>

## Fourier Transform on $\mathbb{T}^n$
We define $S^1$ to be the unit circle in the complex plane. The map 

$$
(x_1,\ldots, x_n)\mapsto (e^{2\pi i x_1},\ldots, e^{2\pi i x_n})
$$

is a **homeomorphism** (actually a Lie group isomorphism) between $\realn/\mathbb{Z}^n\cong (\real/\mathbb{Z})^n$ and $S^1\times \cdots\times S^1 = \mathbb{T}^n$. For measure-theoretical purposes, we identify

$$
Q = [-2^{-1},\: 2^{-1})^n\quad\text{with}\quad \mathbb{T}^n
$$

or $$Q = [0,\: 1)^n$$. It is important to note that $\mathbb{T}^n$ is compact and Hausdorff, but $Q$ is not. The usual construction for the Fourier Transform on $L^2(\mathbb{T}^n)$ is by showing 

<div class="theorem-box" markdown=1 name="">
Let $E_{k}(x) = e^{2\pi i\langle k,x\rangle}$ for $k\in\mathbb{Z}^n$. Then $(E_k)_{k\in \mathbb{Z}^n}$ is an orthonormal (Hilbert) basis of $L^2(\mathbb{T}^n)$. We define the **Fourier Transform on $L^2(\mathbb{T}^n)$** of a $L^2$, $1$-periodic function $f\in L^2(\mathbb{T}^n)$ to be the **unitary map** that retrieves the orthonormal coefficients (see Folland 5.30)

$$
\mathcal{F}f = \hat{f}\in l^2(\mathbb{Z}^n)\quad\text{where}\quad \hat{f}(k) = \langle f,E_k\rangle_{L^2}
$$

Computing the right member reads

$$
\langle f, E_k\rangle_{L^2} = \int_{\xx}f(x)\cl{E_k(x)}dx\quad k\in\mathbb{Z}^n
$$

where $\cl{E_k(x)} = E_{-k}(x) = e^{-2\pi i\langle k,x\rangle}$, and the domain of integration $\xx$ is equal to $Q$ or $\mathbb{T}^n$. The **Fourier Series of $f$** is the countable sum

$$
\sum_{k\in\mathbb{Z}^n}\hat{f}(k) E_k(x)
$$

which converges to $f$ in $L^2$ independent of permutation.


</div>

The algebraic operations described in the previous section carry over as well. We can also extend the domain of $\mathcal{F}$ to $L^1 + L^2$ on the $n$-torus, and this will be the last $n$-dimensional result we will need before turning to the convergence of one-dimensional Fourier Series.

<div class="theorem-box" markdown=1 name="">
**Hausdorff-Young Inequality for the Torus**. Let $1\leq p\leq 2$, and $q$ be conjugate to $p$. If $f\in L^p(\mathbb{T}^n)$, then $\hat{f}\in l^q(\mathbb{Z}^n)$, and $\norm{\hat{f}}_q\leq\norm{f}_p$.
</div>

## Fourier Series on $\mathbb{T}$
The Fourier Transform on $\realn$ converts $L^1$ convergence to uniform convergence in frequency. By Hausdorff-Young,

$$
\norm{\hat{f_n}-\hat{f}}_u=\norm{\mathcal{F}(f_n - f)}_u \leq\norm{f_n-f}_1
$$

Can the same be said for periodic $f\in L^1(\mathbb{T}^n)$, $\hat{f}\in l^1(\mathbb{Z}^n)$? When does $$\lim_{m\to\infty}\sum_{-m}^{m} \hat{f}(k)E_{k}(x)$$ converge pointwise everywhere, uniformly, compactly to the original function $f$? To wit, let us define the following terminology.

<div class="definition-box" markdown=1 name="">
We define the **$m$-th symmetric partial sum of the Fourier Series of $f$** to be

$$
S_mf(x) = \sum_{\vert k\vert\leq m} \hat{f}(k)E_{k}(x)
$$

and the **$m$-th Dirichlet kernel** 

$$
D_m(x) = \sum_{\vert k\vert\leq m}E_k(x)
$$

Since $\hat{f}(k) = \langle f, E_{k}\rangle_{L^{(p,q)}}$ for suitable $1\leq p\leq 2$, and $q\geq 1$, we compute

$$
\begin{align}
S_m f(x) &= \sum_k E_{k}(x)\int_0^1 f(y)E_{-k}(y)dy \\
&= \sum_k \int_0^1 f(y)E_{k}(x-y)dy\\
&= \sum_k (f\ast E_{k})(x)\\
&= f\ast \biggl(\sum_k E_k\biggr)(x)\\
&= (f\ast D_m)(x)
\end{align}
$$


</div>

Although we will not use this next result, it gives sufficient conditions for pointwise convergence of the symmetric partial sums.

<div class="theorem-box" markdown=1 name="">
**Folland 8.43:** If $f\in BV(\mathbb{T})$ where $$\mathbb{T}\cong [-2^{-1},\: +2^{-1}]$$, then $S_m f$ converges **pointwise everywhere** to the arithmetic mean of the left and right limits of $f$.

$$
\lim_{m\to\infty} S_m f(x) = 2^{-1}[f(x+) + f(x-)]\quad\forall x\in \real
$$

</div>

The next two results  provides an answer (but not a complete one) to the question of uniform convergence. We will prove the first result.

<div class="theorem-box" markdown=1 name="">
**Folland 8.33**: Let $f:\real\to\mathbb{C}$ be a $1$-periodic, absolutely continuous function. Suppose also $f'\in L^p(\mathbb{T})$ for reflexive $p$. Then $\hat{f}\in l^1(\mathbb{Z})$.
</div>
<div class="proof-box" markdown=1 proof-name="">
Sketch: use Folland 8.20 to 8.21, 8.22. AC, BV, and Integration by parts formula (sufficient conditions), theorem 3.36. Goal is to prove 8.33
state theorem 8.45, without proving.

- Measure Theoretic equivalences of the torus, and the product interval.
- Some abstract harmonic analysis maybe?
</div>

The proof of the following claim is absolutely non-trivial. The first of the three claims is proven using Weierstrass' $M$-test. The second is proven using a clever argument concerning the Poisson kernel. The third and last statement follows from Corollary 8.45.

<div class="theorem-box" markdown=1 name="">
If $f\in L^1(\mathbb{T})$ and $\hat{f}\in l^1(\mathbb{Z})$. Then there exists a **continuous function** $g$ such that $S_m f\to g$ absolutely and uniformly. If $f$ is assumed to be continuous, then $S_m f\to f$ uniformly on compact subsets of $\real$.
</div>



## Types of Distributions

<div class="definition-box" markdown=1 name="Distributions on $C_c^\infty$">
A **distribution** is a *continuous linear functional* on $C_c^\infty$. The space of distributions is denoted by $\mathcal{D}'(\realn) = \mathcal{D}'$. 

- Depending on the context, it can be considered as a vector space over the field $\mathbb{C}$, or as a module over $C^\infty$.
- We equip $\mathcal{D}'$ with the weak-$\ast$ topology. That is, the topology of pointwise convergence on $C_c^\infty$. 
- We sometimes refer to $C_c^\infty$ as the *space of test functions* or $\mathcal{D}$. It is equipped with the [canonical LF-topology](https://en.wikipedia.org/wiki/LF-space).
</div>
<div class="definition-box" markdown=1 name="Tempered Distributions">
A **tempered distribution** is the space of continuous linear functionals on $\szz$. The space of tempered distributions is denoted by $\szz'$
- Depending on the context, it can be considered as a vector space over $\mathbb{C}$ or as a module over $C_{s}^\infty$; the space of **slowly-increasing smooth functions**.
- It is equipped with the weak-$\ast$ topology.
</div>
<div class="definition-box" markdown=1 name="Support of Distribution">
The **support** of a distribution $F\in \mathcal{D}'$ is defined as the complement of the **largest open set $W\subseteq\real^n$** such that $F(C_c^\infty(W))=0$. Constructively, if $F_0 = \bigset{U\subseteq\realn,\: U\text{ is open, } F(C_c^\infty(U))=0}$, then $W = \bigcup_{U\in F_0}U$, and $\supp{F} = \real^{n}\setminus W$.

- We say a distribution $F$ has **compact support** if $\supp{f}$ is compact, and it has **full support** if $\supp{F} = \realn$.
- The space of compactly supported distributions on $\realn$ is denoted by $\Epsilon'$.
</div>

The following is a result that we will not use.

<div class="theorem-box" markdown=1 name="">
The continuous dual space of $C^\infty(\realn)$ is *precisely* the space of compactly supported distributions; if we identify $\Epsilon'\subseteq\mathcal{D}'$ with its continuous extension.
</div>

## Operations on Distributions
See [this post]({{ site.baseurl }}/{% post_url 2023-08-12-folland-distribution-excerpts %}) for a summary. Let us recall the following properties of $\mathcal{F}$ on $L^1(\realn)$. 

Throughout this section, $G$ will denote a **topological group**.

<div class="definition-box" markdown=1 name="">
Let $y\in \realn$ and $f: \realn\to\mathbb{C}$ be measurable. We denote the **right translate** and the **left translate** of $f$ by $y$ by

$$
L_y f(x) = \tau_y f(x) = f(\tau_{y}^{-1}(x))\quad\text{and}\quad R_y f(x) = f(\tau_y(x))
$$

</div>

A **left-invariant measure** on $G$, is a Borel measure $\mu_L:\borel_{G}\to [0,+\infty]$$ such that for any Borel set $E\in\Borel_{G}$, $\mu_L(E) = \mu_L(xE)$ for any $x\in G$.


We will be working with locally compact metric abelian groups. 



## Sobolev Spaces over $\mathbb{C}$
In this section, we will introduce a special subset of tempered distributions on $\realn$ called the **Sobolev spaces**, denoted by $H_s$ or $H^s$ depending on the text for $s\in\real$. What is nice about $H^s$ is that the are Hilbert spaces, and the **periodic Sobolev spaces** over $\real$ are used in the proof of the **non-triviality of the special symplectic capacity $c_0$**. We first discuss $H^s$ over $\mathbb{C}$, and we will modify the argument in Hofer's text in order to *fold $\real^{2n}$ into $\realn$* and using an **almost complex structure** on the real symplectic manifold $(\real^{2n},\omega_0)$

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




## Proposition 5
We define the $L^2$ Sobolev spaces on $A$ in the notation of Hofer, 
- $$H^s = \bigset{f\in L^2(A,\real^{2n}),\: \sum_{k\in\mathbb{Z}} \vert k\vert^{2s}\vert\hat{f}(k)\vert^2<+\infty}$$
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