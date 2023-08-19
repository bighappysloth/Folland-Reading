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
See [this post]({{ site.baseurl }}/{% post_url 2023-08-12-folland-distribution-excerpts %}#chapter-9---distribution-and-its-operations) for a summary. 


## Elements of Abstract Harmonic Analysis

<div class="definition-box" markdown=1 name="">
A **topological group** is a group $G$ endowed with the topology, in which the **group action** $A: G\times G\to G$ that takes $(g,h)\mapsto gh^{-1}$ is **continuous**. An *equivalent characterization* of $G$ is to require the multiplication map $m(x,y)= xy$, and the inversion map $x\mapsto x^{-1}$ be continuous. 

</div>

Like in Group Theory, we use the following notation for cosets. Let $H$ be any subset (not necessarily a subgroup) of a topological group $G$.

- $aH = \\{ab,\: b\in H \\}$,
- $Ha = \\{ba,\: b\in H \\}$,
- $H^{-1} = \\{b^{-1},\: b\in H \\}$,
- $HK = \\{ab,\: a\in H, b\in K\\}$
- We say $H\subseteq G$ is **symmetric** if $H = H^{-1}$. 

Throughout this section, $G$ will denote a **topological group**.

A **left-invariant measure** on $G$, is a Borel measure $\mu_L:\borel_{G}\to [0,+\infty]$ such that for any Borel set $E\in\borel_{G}$, $\mu_L(E) = \mu_L(xE)$ for any $x\in G$. Similarly for **right-invariant measures**.

A **left (resp. right) Haar measure** on $G$ is a left (resp. right) invariant Radon measure.

<div class="remark-box" markdown=1 name="">
Recall a **Radon measure** on a LCH space $\xx$ is a Borel measure that is finite on all compact sets, and outer regular on Borel sets, and inner regular on open sets. 

This means we can approximate Borel sets using open supersets, and we can approximate open sets using compact subsets (which have finite measure).
</div>

![Folland 11.1]({{ site.baseurl }}{% link /images/folland-11-1.png %})

Let $\xx$ be a topological space, a **continuous group action** of $G$ on $\xx$ is a map $G\times \xx\to \xx$. For any $g,h,e\in G$, $x\in \xx$, where $e\in G$ denotes the identity element of $G$ we have

$$h(gx) = (hg)x\quad\text{and}\quad ex = x$$


<div class="definition-box" markdown=1 name="">
Let $y\in \realn$ and $f: \realn\to\mathbb{C}$ be measurable. We denote the **right translate** and the **left translate** of $f$ by $y$ by

$$
L_y f(x) = \tau_y f(x) = f(\tau_{y}^{-1}(x))\quad\text{and}\quad R_y f(x) = f(\tau_y(x))
$$

</div>

For Lemma 3.74, we can replace $\mu$ with a G-invariant Radon measure, and $\xx$ by a $\sigma$-compact LCH space. The assumption that $G$ is metrizable can be dropped as well, see Folland Chapter 11.

![Einsiedler]({{ site.baseurl }}{% link /images/unitary-representation-group-action.png %})

### Group Actions and Fourier transforms
From Folland 8.22a) the translation of $f\in L^1(\realn)$,

$$
(\tau_y f)(x) = f(x-y)\quad\text{and}\quad \mathcal{F}(\tau_y f)(\zeta) = E_{-y}(\zeta)\hat{f}(\zeta)
$$

The translation of distributions

$$
\langle \tau_y F,\phi\rangle = \langle F, \tau_{-y}\phi\rangle
$$

The Fourier Transform of a Tempered Distribution is defined by the Tempered Distribution that precomposes $\phi\in \szz$ by its Fourier Transform.

$$
\langle \hat{F},\phi\rangle = \langle F,\hat{\phi}\rangle
$$

Combining the shift and the transform, we get

$$
\begin{align}
\langle (\tau_y F)\hat{\:}, \phi\rangle &= \langle \tau_y F, \hat{\phi}\rangle \\
&= \langle F, \hat{\phi}(\zeta + y)\rangle \\
&= \langle F, \tau_{-y}\hat{\phi}\rangle 
\end{align}
$$

Alternatively, we can write $$\langle F, \hat{(E_{-y}\phi)}\rangle =\langle\hat{F}, E_{-y}\phi\rangle = \langle E_{-y}\hat{F},\phi\rangle$$

Whether or not the arguments within the duality pairing is in $x$ or $\zeta$ does not matter, because $F$ is not a function and it does not make sense to compare arguments that way. $x$ and $\zeta$ represents general points in $\realn$.

We now turn our attention to the symmetries

$$
(\tau_y f)^\hat{\:} = (E_{-y})\hat{f}\quad\text{and}\quad\biggl[ \tau_y\hat{f} = (E_yf)^\hat{\:}\quad\text{or}\quad (\tau_y f)^\breve{\:} = E_y\breve{f}\biggr]
$$

Moreover, the differentiation of Tempered Distributions, note $E_{\zeta}(x)$ is $C_s^\infty$ for $\zeta\in\realn$.

$$
(\partial^\alpha f)^\hat{\:} = (2\pi i \zeta)^{\alpha}\hat{F}\quad\text{and}\quad \biggl[(\partial^\alpha \hat{F})^{\breve{\:}} = ((-2\pi ix)^{\alpha}F)^{\hat{\:}}\quad\text{or}\quad (\partial^\alpha F)^{\breve{\:}} = (-2\pi i x)^\alpha\breve{F} \biggr]
$$


# Sobolev spaces
In this section, we will introduce a special subset of tempered distributions on $\realn$ called the **Sobolev spaces**, denoted by $H_s$ or $H^s$ depending on the text for $s\in\real$. What is nice about $H^s$ is that the are Hilbert spaces, and the **periodic Sobolev spaces** over $\real$ are used in the proof of the **non-triviality of the special symplectic capacity $c_0$**. We first discuss $H^s$ over $\mathbb{C}$, and we will modify the argument in Hofer's text in order to *fold $\real^{2n}$ into $\realn$* and using an **almost complex structure** on the real symplectic manifold $(\real^{2n},\omega_0)$.

## Sobolev spaces over $\mathbb{C}$

Some terminology: the *morphisms* of $\szz'$ are continuous linear maps, so an *endomorphism* on $\szz'$ would be a continuous map $T: \szz'\to\szz'$ that is continuous with respect to the weak-$\ast$ topology.

We will define the Sobolev spaces in terms of the Fourier Transform on $\szz'$. 


<div class="lemma-box" markdown=1 name="">
Let $g\in C_s^\infty$. The pointwise multiplication map $m_g: \szz\to\szz$, $m_g(\phi) = g\phi$ is an endomorphism on $\szz$.
</div>
<div class="proof-box" markdown=1 proof-name="">
First, we show $m_g$ maps into $\szz$. Indeed, fix $\phi\in\szz$ and a multi-index $\alpha$, and $N\in\nat^+$. we can obtain $M_\alpha\in\nat^+$, such that

$$
\vert \partial^\beta g(x)\vert\Lsim_{g,\alpha} (1+\vert x\vert)^{M_\alpha}\quad\forall\vert\beta\vert\leq\vert\alpha\vert
$$

By the [product rule]({{ site.baseurl }}/{% post_url 2023-08-12-folland-distribution-excerpts %}#chapter-8---multivariate-calculus), and denoting finite sums by $\sum^\wedge$, 

$$
\partial^\alpha (g\phi) = \sum_{\beta+\gamma = \alpha}\dfrac{\alpha!}{\beta!\gamma!}(\partial^\beta g)(\partial^\gamma \phi)\implies\vert\partial^\alpha(g\phi)\vert\Lsim_{\alpha,g}\sum^{\wedge}\vert\partial^\gamma\phi\vert(1+\vert x\vert)^{M_{\alpha}}
$$

Multiplying by $(1+\vert x\vert)^{N}$ on both sides of the estimate yields

$$
(1+\vert x\vert)^N\vert\partial^\alpha(g\phi)\vert\Lsim_{\alpha,g}\sum^{\wedge}\vert\partial^\gamma\phi\vert(1+\vert x\vert)^{M_\alpha + N}\Lsim_{\alpha,g}\sum^{\wedge}\norm{\phi}_{(N+M_\alpha,\gamma)}<+\infty
$$

Continuity follows immediately from the equation above, see [definition of continuity between TVS]({{ site.baseurl }}/{% post_url 2023-08-12-folland-distribution-excerpts %}#chapter-5---frechet-space-convergence).


</div>
<div class="lemma-box" markdown=1 name="">
For $s\in\real$, let $$\Lambda_s: f\mapsto [(1+\vert\zeta\vert^2)^{s/2}\hat{f}]^{\breve{\:}}$$ is an automorphism on $\szz'$, with inverse $\Lambda_s^{-1} = \Lambda_{-s}$.
</div>
<div class="proof-box" markdown=1 proof-name="">
The Fourier Transform on $\szz'$ and its inversion are isomorphisms on $\szz'$, hence the first and last step are continuous. 

$$
f\mapsto \hat{f}\mapsto (1+\vert\zeta\vert^2)^{s/2}\cdot \hat{f} \mapsto \Lambda_s f
$$


For $s\in\real$, $g(\zeta) = (1+\vert\zeta\vert^2)^{s/2}$ is clearly slowly increasing. It suffices to show multiplication by a slowly increasing function with a tempered distribution $F\in \szz'$ is continuous. Since $\szz'$ is equipped with the topology of pointwise convergence, the previous Lemma implies 

$$
\langle g F_n,\phi\rangle = \langle F_n, g\phi\rangle\longrightarrow \langle F,g\phi\rangle = \langle g F,\phi\rangle
$$

$\Lambda_s$ is continuous. Moreover, the mutliplication by slowly increasing functions on $\szz'$, the Fourier Transform and its inverse is defined by precomposing the duality pairing with the respective map, so 

$$
\langle \Lambda_s F,\phi\rangle = \langle F,\Lambda_s\phi\rangle\quad\forall F\in\szz',\: \phi\in\szz
$$


To show $\Lambda_s^{-1} = \Lambda_{-s}$, it suffices to show $\Lambda_{-s}\Lambda_{s}\phi = \phi$ for $\phi\in \szz$, if we identify $\szz\subseteq\szz'$ this is because

$$
\langle\Lambda_{-s}\Lambda_{s}F,\phi\rangle = \langle F,\Lambda_{-s}\Lambda_{s}\phi\rangle
$$

And

$$
\begin{align}
\Lambda_{-s}\Lambda_s\phi &= \Lambda_{-s}\biggl(((1+\vert\zeta\vert^2)^{s/2}\hat{\phi})^{\breve{\:}}\biggr)\\
&= \biggl[(1+\vert\zeta\vert^2)^{-s/2}\biggl((1+\vert\zeta\vert^2)^{s/2}\hat{\phi}\biggr)\biggr]^{\breve{\:}}\\
&= \hat{\phi}^{\breve{\:}}\\
&= \phi
\end{align}
$$

The last equality is due to $\mathcal{F}$ being an isomorphism on $\szz$, and the proof is complete upon replacing the roles of $s$ and $-s$.
</div>

<div class="definition-box" markdown=1 name="">
If $s\in\real$, the **Sobolev space $H_s$** is the space

$$
H_s = \bigset{f\in \szz',\: \Lambda_sf\in L^2}
$$

The claim $\Lambda_sf\in L^2$ should be interpreted with respect to the ambient topology of $\szz'$. **There exists $g\in L^2$ that realizes the duality pairing $\langle \Lambda_s f, \cdot\rangle$**, if $\phi\in\szz$ is arbitrary, 

$$
\langle \Lambda_s f,\phi\rangle_{(\szz',\szz)} = \langle f, \Lambda_s \phi\rangle_{(\szz',\szz)} = \langle g, \Lambda_s (\iota\phi)\rangle_{(L^2,L^2)} 
$$

where $\iota: \szz\to L^2$ is the inclusion map.

</div>

We call $\Lambda_s f$ the **$L^2$ representative of $f$**. Clearly, the $L^2$ representative of $f$ is unique a.e. Suppose the $L^2$ representative is linear in $H_s$ for the moment, we can borrow the algebraic and topological structure from $L^2$ by pulling back the inner product. As in

$$
\langle f,g\rangle_{(s)} =  \langle \Lambda_s f,\Lambda_s g\rangle_{(L^2, L^2)} = \langle (\Lambda_s f)^\hat{\:} ,(\Lambda_s g)^\hat{\:} \rangle_{(L^2, L^2)} = \int_{\realn}\hat{f}(\zeta)\cl{\hat{g}(\zeta)}(1+\vert\zeta\vert^2)^s d\zeta
$$

The second equality is due to the Fourier Transform being unitary on $L^2$. The next lemma will allow us to justify the claim that $\langle\cdot,\cdot\rangle_{(s)}$ as is defined above is indeed an inner product; because the linear pullback of an inner product is again an inner product.


<div class="lemma-box" markdown=1 name="">
The $L^2$ representative of $H_s$ is linear, that is: 

$$\Lambda_s \sum^{\wedge} = \sum^{\wedge}\Lambda_s$$

Moreover, $\Lambda_s f = 0$ in $L^2$ means $f = 0$ in $\szz'$.
</div>
<div class="proof-box" markdown=1 proof-name="">
First, it is clear the zero distribution is represented by the zero function in $L^2$. so $\Lambda_s 0 = 0$. Next, let $f,g\in H_s$, and $\Lambda_s f$ and $\Lambda_s g$ be their $L^2$ representatives. Fix $\phi\in \szz$, 

$$
\begin{align}
\langle\Lambda_s (f+g), \phi\rangle_{(L^2,L^2)} &= \langle f+g,\Lambda_s \phi\rangle_{(\szz',\szz)}\\
&= \langle f,\Lambda_s \phi\rangle_{(\szz',\szz)} + \langle g,\Lambda_s \phi\rangle_{(\szz',\szz)}\\
&= \langle \Lambda_s f,\phi\rangle_{(L^2,L^2)} + \langle \Lambda_s g,\phi\rangle_{(L^2,L^2)}\\
&= \langle \Lambda_s f + \Lambda_s g,\phi\rangle_{(L^2,L^2)}
\end{align}
$$

Homogeneity is proven in a similar manner. Suppose $f\in H_s$ and $\Lambda_s f=0$ in $L^2\cong (L^2)^*$. Let $\phi$ be any Schwartz function, precomposing the $L^2$ pairing with the inclusion map $\iota: \szz\to L^2$ yields

$$
\langle \Lambda_s f, \phi\rangle_{(\szz',\szz)} = \langle \Lambda_s f, \iota\phi\rangle_{(L^2, L^2)} = 0
$$

Therefore $\Lambda_s f = 0$ in $\szz'$ as well. But $\Lambda_s$ is an automorphism on the space of Tempered Distributions, so that

$$
\Lambda_s f = 0 \iff f\in \operatorname{Ker}(\Lambda_s) \iff f = 0
$$

and the proof is complete.
</div>

<div class="remark-box" markdown=1 name="">
Question: Is the map $f\mapsto \Lambda_s f$ injective? Attempt: not necessarily injective, because $L^2$ may mod out a.e differences, but do these differences matter if we precompose Schwartz functions by the inclusion map? Because the weak-$\ast$ topology is Hasudorff, this would prove injectivity?
</div>

## Key results of $H_s$ over $\mathbb{C}$
<div class="theorem-box" markdown=1 name="">
Let $s\in \real$, the preceding discussion shows that $H_s$ is a pre-Hilbert space (an inner product space vector space that is not necessarily complete)

- The Fourier transform is a unitary isomorphism from $H_s$ into $L^2(\realn,\mu_s)$, where $d\mu_s(\zeta) = (1+\vert\zeta\vert^2)^sd\zeta$ is an absolutely continuous measure wirth respect to the standard Lebesgue measure. And $H_s$ is a Hilbert space,
- The space of Schwartz functions $\szz$ is dense in $H_s$
- If $t < s$, $H_s$ can be embedded as a dense linear subspace of $H_t$ in the topology of $H_t$. In particular, **the spaces decrease, and the norms increase**. That is,

$$
t<s\implies H_s\subseteq H_t\quad\text{and}\quad \norm{\cdot}_{(t)}\leq\norm{\cdot}_{(s)}
$$

- $\Lambda_t$ is a unitary isomorphism from $H_s$ to $H_{s-t}$, here we view $\Lambda_t$ as a map between Sobolev spaces; whose topology differs that from the weak-$\ast$ topology of $\szz'$,
- $H_0 = L^2$, and $$\norm{\cdot}_{(0)} = \norm{\cdot}_{L^2}$$
- The distributional derivative operator, which is defined on the whole of $\szz'$, hence defined on each $H_s$ is a bounded linear map from $H_s$ to $H_{s-\vert\alpha\vert}$, for all $s\in\real$, and multi-index $\alpha$.
</div>
<div class="proof-box" markdown=1 proof-name="Proof of first claim">
Suppose $\xx$ is a vector space and $\yy$ is an inner product space over $\mathbb{C}$. If $\tau:\xx\to\yy$ is an **linear injection**, the pullback of the inner product on $\yy$ through $\tau$ is again an inner product on $\xx$; in other words, $\tau$ equips $\xx$ with an inner product that is $\tau$-related to $\yy$.

If $\tau$ is a **linear bijection**, $\tau$ is an IPS isomorphism. So it suffices to prove surjectivity. 

First, we prove the inclusion map $\szz\to L^P$ for usual $p$ and $p = +\infty$ is continuous. If $p = +\infty$, then 

$$
\norm{f}_{\infty}=\norm{f}_{(0,0)}
$$

If $p$ is usual, we use the following trick. Let $N = n+1$ where $n$ is the dimension of the domain. 

$$
\begin{align}
\norm{f}_{p}^{p} &= \int_{\realn}\vert f\vert^{p} \cdot(1+\vert x\vert)^{Np}\cdot(1+\vert x\vert)^{-Np}\\
&\leq \int_{\realn} \biggl(\vert f\vert (1+\vert x\vert )^N\biggr)^p\cdot (1+\vert x\vert )^{-Np}dx\\
&\leq \int_{\realn} \biggl(\vert f\vert (1+\vert x\vert )^N\biggr)^p\cdot (1+\vert x\vert )^{-N}dx\\
&\leq \norm{f}_{(N,0)}^{p}\int_{\realn}(1+\vert x\vert)^{-N}dx\\
&\leq \norm{f}_{(N,0)}^{p}\norm{(1+\vert x\vert)^{-N}}_{1}
\end{align}
$$

For the third inequality we used the fact 

$$
p\geq 1\implies Np\geq N\implies (1+\vert x\vert)^{-Np}\leq (1+\vert x \vert)^{-N}
$$

Taking the $p$-th root, $$\norm{f}_{p}\leq\norm{f}_{(N,0)}\norm{(1+\vert x\vert)^{-N}}_{1}^{1/p} $$. Hence the inclusion map is a toplinear embedding (a linear topological embedding). We now show the dual of $\szz$ is toplinearly embedded in the dual of $L^{p}$ for usual $p$ and $p = +\infty$ with respect to the weak-$\ast$ topologies $\sigma(\szz', \szz)$, and $\sigma((L^p)^*, L^p)$. 

Let $\iota: \szz\to L^p$ be the toplinear embedding, and $$\iota^*$$ be the pullback of $$(L^p)^*$$ by precomposing any $$f\in (L^p)^*$$ by $\iota$. Such that for every $\phi\in\szz$,

$$
(\iota^*f)(\phi) = f(\iota\phi)\quad\forall f\in (L^p)^*
$$

The composition of continuous maps is again continuous, so $$\iota^*$$ maps into the tempered distributions. To show continuity, fix a convergent sequence $f_n\to f$ in $$\sigma((L^p)^*, L^p)$$. Now fix $\phi\in \szz$, almost by definition,

$$
\vert \iota^*f_n(\phi) - \iota^*f(\phi)\vert = \vert f_n(\iota\phi) - f(\iota\phi)\vert\to 0
$$

therefore $$\iota^*f_n\to \iota^*f$$ in $\sigma(\szz', \szz)$. So $\iota^*$ is a toplinear embedding. 

Next, we show the Fourier Transform is a surjection from $H_s$ onto $L^2(\realn,\mu_s)$. Indeed, fix $$\varphi\in L^2(\realn,\mu_s)$$,

$$
\begin{align}
\varphi\in L^2(\realn,\mu_s)&\iff \varphi(1+\vert\zeta\vert^2)^{s/2}\in L^2(\realn, d\zeta)\\
&\iff \mathcal{F}^{-1}(\varphi(1+\vert\zeta\vert^2)^{s/2} )\in (L^2)^*(\realn,d\zeta)\\
&\implies \iota^*\mathcal{F}^{-1}(\varphi(1+\vert\zeta\vert^2)^{s/2} )\in \szz' 
\end{align}
$$

The second equivalence comes from $\mathcal{F}$ being unitary, and $L^2$ being reflexive, the third is because $(L^2)^*$ is toplinearly embedded into $\szz'$. Now, let $\theta\in\szz'$ realize the duality pairing implied in the last equation. For every $a\in \szz$, 

$$
\begin{align}
\langle \iota^*\mathcal{F}^{-1}(\varphi(1+\vert\zeta\vert^2)^{s/2}), a\rangle_{(\szz','szz)} &=\langle \mathcal{F}^{-1}(\varphi(1+\vert\zeta\vert^2)^{s/2}),\iota a\rangle_{((L^2)^*, L^2)}\\
&=\langle \varphi(1+\vert\zeta\vert^2)^{s/2},\mathcal{F}(\iota a)\rangle_{((L^2)^*, L^2)}
\end{align}
$$

The inclusion map commutes with the Fourier Transform, because $\mathcal{F}(\szz) = \szz$, so does the pullback, since $$\mathcal{F}(L^2) = L^2 = (L^2)^*$$.

</div>

<div class="proof-box" markdown=1 proof-name="Proof of the rest">
$H_s$ is Hilbert isomorphic to $L^2(\realn,\mu_s)$, $\szz$ is dense in $L^2(\realn,d\zeta)$. It therefore suffices to show $\szz$ is dense in $L^2(\realn, \mu_s)$. Let $f\in L^2(\realn,\mu_s)$, then

$$
\int_{\realn}\vert f\vert^2 (1+\vert\zeta\vert^2)^{s}d\zeta = \norm{f}^2_{L^2(\mu_s)} = \norm{(1+\vert\zeta\vert^2)^{s/2} f}_{L^2(d\zeta)}<+\infty
$$

Furthermore, if $g\in \szz$, so is $h = (1+\vert\zeta\vert^2)^{-s/2}g$, since $(1+\vert\zeta\vert^2)^{t}$ is slowly increasing for every $t\in\real$. Using the density of $\szz$ in $L^2(\realn, d\zeta)$, if $\varepsilon>0$ we obtain a $g\in\szz$ with $\int \vert (1+\vert\zeta\vert^2)^{s/2}f - g\vert^2d\zeta < \varepsilon^2$

$$
\begin{align}
\int \vert (1+\vert\zeta\vert^2)^{s/2}f - g\vert^2d\zeta &= \int (1+\vert\zeta\vert^2)^{s}\cdot \vert f-h\vert^2d\zeta\\
&=\norm{f-h}_{L^2(\mu_s)}^2\\
&< \varepsilon^2
\end{align}
$$

This proves the second claim. The third claim follows the fact that given $t<s$ then $A_t\leq A_s$ pointwise, where $A_t = (1+\vert\zeta\vert^2)^{t/2}$, and 

$$
\norm{f}_{(t)} = \norm{A_t f}_{2}\leq \norm{A_s f}_{2} = \norm{f}_{(s)}
$$

Therefore $H_s\subseteq H_t$ as a subspace, and the inclusion map $j: H_s\to H_t$ is linear and continuous; as

$$
\norm{jf}_{(t)}= \norm{f}_{(t)}\leq \norm{f}_{(s)}
$$

so that $j$ is a **toplinear embedding**, meaning it is linear, continuous and is a topological embedding. Next, we show the multiplication map on the space of tempered distributions, $\Lambda_t: \szz'\to \szz'$, with $f\mapsto A_t\cdot f\in \szz'$ is a unitary isomorphism from $H_s\to H_{s-t}$, and $\Lambda_t^{-1} = \Lambda_{-t}$.

Fix $f,g$ in $H_s$, noting that $\Lambda_{s-t}\Lambda_{t} f = \Lambda_s f$ (verify), using the Hilbert space structure on $H_s$ and $H_t$ instead of the weak-$\ast$ topology inherited from $\szz'$, we compute the following

$$
\begin{align}
\langle f,g\rangle_{(s)}&= \langle \Lambda_s f,\Lambda_s g \rangle_{(L^2, L^2)}\\
&= \langle \Lambda_t f,\Lambda_t g \rangle_{(s-t)} \\
&= \langle\Lambda_{s-t}\Lambda_{t} f, \Lambda_{s-t}\Lambda_{t} g  \rangle_{(L^2, L^2)}\\
&= \langle \Lambda_{s}f, \Lambda_{s} g \rangle_{(L^2,L^2)}\\
&= \langle f,g\rangle_{(s)}
\end{align}
$$

This establishes the fourth and fifth claims. 

Finally, to show $\partial^\alpha: H_s\to H_{s-\vert\alpha\vert}$ is a continuous linear map, we use the properties of the Fourier Transform for tempered distributions.

- $$(\partial^\alpha F)^{\hat{\:}} = (2\pi i \zeta)^{\alpha}\hat{F}$$, where $\hat{F}$ denotes the distributional Fourier Transform, and the factor of $(2\pi  i \zeta)^{\alpha}$ is a slowly increasing (smooth) function.
- Computing $$(\Lambda_{s-\vert\alpha\vert}\partial^\alpha f)^{\hat{\:}}$$,

$$
\begin{align}
(\Lambda_{s-\vert\alpha\vert}\partial^\alpha f)^{\hat{\:}} &= (1+\vert\zeta\vert^2)^{s/2 - \vert\alpha\vert/2}\cdot(\partial^\alpha f)^{\hat{\:}}\\
&= (1+\vert\zeta\vert^2)^{s/2 - \vert\alpha\vert/2}\cdot(2\pi i \zeta)^{\alpha}
\cdot \hat{f}\\
&= (2\pi i)^{\vert\alpha\vert}(1+\vert\zeta\vert^2)^{(s-\vert\alpha\vert)/2}\cdot \zeta^\alpha\cdot\hat{f}\\
\end{align}
$$

So $$({\Lambda_{s-\vert\alpha\vert}\partial^\alpha f}^{\hat{\:}}) = C_{\alpha} (1+\vert\zeta\vert^2)^{(s-\vert\alpha\vert)/2}\cdot \zeta^\alpha \cdot\hat{f}$$, where $C_\alpha = (2\pi i)^{\vert\alpha\vert}$. We know that 

$$
\Lambda_s f\in L^2\iff (\Lambda_s f)^{\hat{\:}} = (1+\vert\zeta\vert^2)^{s/2}\hat{f}\in L^2
$$

So the expression that *defines* $$(\Lambda_{s-\vert\alpha\vert}\partial^\alpha f)^{\hat{\:}}$$ pointwise function. We can compute its $L^2$ norm, 

$$
\begin{align}
\norm{\partial^{\alpha}f}_{(s-\vert\alpha\vert)} &=\norm{(\Lambda_{s-\vert\alpha\vert}\partial^\alpha f)^{\hat{\:}}}_{L^2}\\
&= \norm{(1+\vert\zeta\vert^2)^{s/2 - \vert\alpha\vert/2}\cdot\mathcal{F}(\partial^\alpha f)}_{L^2}\\
&= \norm{(1+\vert\zeta\vert^2)^{(s-\vert\alpha\vert)/2}C_{\alpha}\zeta^{\alpha}\hat{f}}_{L^2}\\
&\Lsim_{\alpha}\norm{(1+\vert\zeta\vert^2)^{s/2}\hat{f}}_{L^2}\\
&\Lsim_{\alpha}\norm{f}_{(s)}
\end{align}
$$

the first equality is because of plancherel, and the second last estimate is justified by Lemma 2 [here]({{ site.baseurl }}/{% post_url 2023-08-12-folland-distribution-excerpts %}#chapter-8). The inverse trasnfrom of an $L^2$ function is again $L^2$, therefore $\Lambda_{s-\vert\alpha\vert}\partial^\alpha f$ is in $L^2$, and $\partial^\alpha$ is continuous.

</div>


<div class="definition-box" markdown=1 name="">
If $C_0$ denotes the space of continuous functions that **vanish at infinity**, we define

$$
C_{0}^{k} = \bigset{f\in C_0(\realn),\: \partial^{\alpha}f \in C_0\:\text{for }\vert\alpha\vert\leq k}
$$

If $k$ is finite, $C_0^k$ is a Banach space with the norm $f\mapsto \sum^{\wedge}\norm{\partial^\alpha f}_u$.

</div>


Before stating the Sobolev Embedding Theorem, we note that if $s>0$, then $H_s$ embeds continuously into $H_0 = L^2$. Identifying $f\in H_s$ with its $L^2$ representative, it makes sense to evaluate $f(x)\in\mathbb{C}$ up to a null set.

If the $L^2$ representative of $f$ coincides a.e with a continuous function $g$ we can *identify* $f$ again with this continuous function. If $g$ is a member of any of the **continuous function spaces** we have discussed (e.g: $C_0^k$, $\szz$) then we *say* $f\in C^{k}_0$ or $f\in \szz$.

If every member of $H_s$ belongs some continuous function space, for example $C_0^k$, then we write $H_s\subseteq C_0^k$. The obvious question becomes, given $H_s$ for $s>0$, 

- When can we identify each $H_s$ as a subset of $C_0^k$?
- When is the inclusion map $j: H_s\to C_0^k$ continuous? 
- When is the inclusion map compact?

Clearly the first question can be answered using regularity properties of the Fourier Transform, and the second depends on finding an estimate for the norm $f\in H_s$

$$
\sum_{\vert\alpha\vert\leq k} \norm{\partial^{\alpha} f}_u= \norm{f}_{C_0^k}\: \Lsim_{k}\: \norm{f}_{(s)}
$$

<div class="theorem-box" markdown=1 name="Sobolev Embedding Theorem">
Let $s > k + n2^{-1}$, where $k = 0, 1,\ldots$.

- For every $f\in H_s$ and multi-index $\alpha$ with $\vert\alpha\vert\leq k$: the Fourier Transform of the $\alpha$-distributional derivative of $f$ is in $L^1$ 

    $$
    (\partial^\alpha f)^{\hat{ }}\in L^1\quad\text{and}\quad \norm{\mathcal{F}(\partial^\alpha f)}_{L^1}\leq C\norm{f}_{(s)}
    $$

    where $C=(2\pi)^k\sqrt{\int (1+\vert\zeta\vert^2)^{k-s}d\zeta}$ is independent of $f$ and depends only on $k-s$. (We can obtain a sharper estimate by replacing the factor $(2\pi)^k$ with $(2\pi)^{k-s}$).

- $H_s$ can be identified as a subspace of $C_0^k$, and the inclusion map $j: H_s\to C_0^k$ is continuous.
</div>
<div class="proof-box" markdown=1 proof-name="">
We start with some semantics. Since $s>k+n2^{-1}>0$, $H_s\subseteq L^2$. The Fourier Transform of $f\in H_s$ is a pointwise function in $L^2$. The first bullet point is a *statement* about the integrability of the pointwise function $\mathcal{F}(\partial^\alpha f)$, where $\mathcal{F}$ and $\partial^\alpha$ should be interperted in the distributional sense, but it so happens that it produces a pointwise function, which we will *identify* with its tempered distribution.

$$
\mathcal{F}(\partial^\alpha f)\in L^1\subseteq\szz'
$$


Computing the Fourier Transform of $\partial^\alpha f$, where $\partial^\alpha: \szz'\to\szz'$ is the distributional derivative on the space of tempered distributions, the previous Theorem tells us 

$$
\partial^\alpha: H_s\to H_{s-\vert\alpha\vert}\quad\text{is continuous}
$$

But $\vert\alpha\vert\leq k\implies s-\vert\alpha\vert \geq s-k > n2^{-1}>0$. So the $\partial^\alpha f$ is also $L^2$, and 

$$
\mathcal{F}(\partial^\alpha f) = (2\pi i)^{\vert\alpha\vert}\zeta^{\alpha}\hat{f}(\zeta)
$$

Computing a pointwise estimate, using Lemma 2 [here]({{ site.baseurl }}/{% post_url 2023-08-12-folland-distribution-excerpts %}#chapter-8)

$$
\begin{align}
\vert\mathcal{F}(\partial^\alpha f)(\zeta)\vert&\leq(2\pi)^{k}\cdot\vert \zeta^\alpha\vert\cdot \vert\hat{f}\vert\\
&\Lsim_k (1+\vert\zeta\vert^2)^{\vert\alpha\vert/2}\vert\hat{f}\vert\\
&\Lsim_k (1+\vert\zeta\vert^2)^{k/2}\vert\hat{f}\vert\\
\end{align}
$$

We integrate over $\realn$, still denoting $(1+\vert\zeta\vert^2)^{t/2}$ by $A_t$, and using Cauchy Schwartz on the second line:

$$
\begin{align}
\norm{\mathcal{F}(\partial^\alpha f)(\zeta)}_{L^1}&\Lsim_k \norm{A_k \hat{f}}_{L^1}\\
&\Lsim_k \norm{A_{k-s}}_{L^2}\norm{A_{s}\hat{f}}_{L^2}\\
&\Lsim_k \norm{A^2_{k_s}}_{L^1}^{1/2}\norm{f}_{(s)}\\
&= C\norm{f}_{(s)}
\end{align}
$$

It suffices to show the integral defining $$C= (2\pi)^k\norm{A^2_{k-s}}_{L^1}^{1/2}$$ converges. Notice $1+\vert\zeta\vert^2\geq \vert\zeta\vert^2$ implies $(1+\vert\zeta\vert^2)^{k-s}\leq\vert\zeta\vert^{2(k-s)}$, and the exponent on $\zeta$ is $2(k-s) = -(2)(k-s)$. Since $2(s-k)>n$, the integral converges absolutely in $B^c$, where $B\subseteq\realn$ is some open ball containing the origin by Folland Corollary 2.52. Further, $A_{k-s}^{2} = (1+\vert\zeta\vert^2)^{2(k-s)}\leq 1$ pointwise for all $\zeta\in B$. So $A_{k-s}^2\in L^1(B)\cup L^1(B^c) = L^1(\realn)$. This proves the first bullet point.

The Fourier inversion integral converges for $\mathcal{F}(\partial^\alpha f)\in L^1$, and by Riemann-Lebesgue we see that 

$$
\partial^\alpha f=\mathcal{F}^{-1}\mathcal{F}(\partial^\alpha f)\in C_0
$$

where $\mathcal{F}^{-1}\mathcal{F} = \mathcal{F}\mathcal{F}^{-1} = \id{\szz'}$, and the inversion formula $\mathcal{F}^{-1}(g(\zeta)) = \mathcal{F}(g(-\zeta))$ for $g\in L^1$ implies

$$
\norm{\mathcal{F}^{-1}(g)}_u = \norm{\mathcal{F}(g(-\zeta))}_u\leq \norm{g(-\zeta)}_{L^1}=\norm{g}_{L^1}
$$

let $g = \mathcal{F}(\partial^\alpha f)$ and we see that

$$
\norm{\partial^\alpha f}_u\leq \norm{\mathcal{F}(\partial^\alpha f)}_{L^1}\Lsim_k \norm{f}_{(s)}\quad\forall \vert\alpha\vert\leq k
$$

Summing over all such $\alpha$, we obtain an estiamte for the $C_0^k$ norm of $f$.

$$
\norm{f}_{C_0^k} =\sum_{\vert\alpha\vert\leq k}\norm{\partial^\alpha f}_u \:\Lsim_{k,n}\: \norm{f}_{(s)}
$$

and this proves the second bullet point.
</div>
<div class="corollary-box" markdown=1 name="">
If $f\in H_s$ for all $s>0$ as a tempered distribution, then it can be identified pointwisely as a function in $C^\infty\cap C_0$.
</div>



## Distributions on $\Torusn$
Let $\mathbb{T}^n = (S^1)^n = (\real/\mathbb{Z})^n$ is a compact Hausdorff space. A function $f: \realn\to\mathbb{C}$ is **periodic** (or $1$-periodic) if $f(x+k) = f(x)$ for every $k\in\mathbb{Z}^n$. 


<div class="definition-box" markdown=1 name="">
A function $f: \realn\to\mathbb{C}$ is **periodic** (or $1$-periodic) if $f(x+k) = f(x)$ for every $k\in\mathbb{Z}^n$. $f$ can be uniquely identified within the space of $1$-periodic functions by its values in $Q=[0,1)^n$. The space of smooth periodic functions on $\realn$ is denoted by $C^\infty(\mathbb{T}^n)$.

$$
C^\infty(\Torusn) = \bigset{f\in C^\infty(\realn),\: f\text{ is periodic.}}
$$


</div>

Because the $n$-torus is compact, we can endow $C^\infty(\Torusn)$ with the Frechet topology of uniform convergence, and if $f\in C^\infty(\Torusn)$, its **restriction** onto the $Q$ is smooth. Since $Q$ represents $\Torusn$ as a quotient space, there exists an injection from smooth functions $C^\infty(Q)\to C^\infty(\Torusn)$. If $g\in C^\infty(Q)$, meaning its support is contained within $Q$ as a subset, we define the **extension map** $W$ to be

$$
Wg(t) = W_g(t) = g(x)\quad t-x\in\mathbb{Z}^n
$$

This coincides with the definition of $C^\infty(\Torusn)$, where each $f\in C^\infty(\Torusn)$ is uniquely determined by its values in $Q$, meaning

$$
W_{f\vert_{Q}} = f
$$

Few more things, if $\phi\in C_c^\infty(\realn)$, the **periodization map $P$** defined by

$$
P_\phi = \sum_{k\in\mathbb{Z}^n}\tau_k\phi
$$

converges to a smooth function in $C^\infty(\realn)$ and can be shown to be continuous (hence toplinear) from $C_c^\infty(\realn)$ into $C^\infty(\Torusn)$. We define the **distributional periodization map $P'$** to be a map

$$
P: \mathbf{D}'(\Torusn)\to \mathbf{D}'(\realn)
$$

that precomposes $F\in \mathbb{D}'(\Torusn)$ with $P$. That means

$$
\langle P'F,\phi \rangle_{(\mathbf{D}'(\realn), \mathbf{D}(\realn))} = \langle F, P\phi\rangle_{(\mathbf{D}'(\Torusn), \mathbf{D}(\Torusn))}
$$

It can be shown that the periodization map is continuous, and it maps $\dzz'(\Torusn)$ into $\dzz'_{per}(\realn)$, the space of *shift-invariant distributions*

$$
\dzz'_{per}(\realn) = \bigset{F\in\dzz'(\realn),\: \tau_kF = F\: \forall k\in\mathbb{Z}^n}
$$

- It can also be shown that $\dzz'_{per}(\realn)\subseteq\szz'$, which states: *every* shift-invariant distribution is tempered.
- $P$ maps $\dzz'(\Torusn)$ into $\dzz'_{per}(\realn)$. This is a bijection.

We are now in the position to dicuss the Fourier Transform of distributions on $\Torusn$. Since $C^\infty(\Torusn) = C_c^\infty(\Torusn)$, $\Epsilon'(\Torusn) = \dzz'(\Torusn) = \szz'(\Torusn)$. Moreover, the Fourier Transform of a $F\in\szz'(\realn)$ is *defined* by precomposing $F$ with the Fourier Transform on $\szz$, which is an isomorphism.

<div class="definition-box" markdown=1 name="">
Since $C^\infty(\Torusn)\subseteq L^2(\Torusn)$, we have a natural $L^2$ isomorphism. Motivated by the $\Epsilon'(\realn)$ case, we define the **Fourier Transform on $\dzz'(\Torusn)$** to be a map

$$
\mathcal{F}: \dzz'(\Torusn)\to C_s(\mathbb{Z}^n)
$$

where $C_s(\mathbb{Z}^n)$ is the space of 'slowly increasing' functions with domain $\mathbb{Z}^n$,

$$
C_s(\mathbb{Z}^n) = \bigset{g: \mathbb{Z}^n\to\mathbb{C},\: \vert g(k)\vert\Lsim_{g}(1+\vert k\vert)^{N},\:N\in\mathbb{N}^+}
$$

so that $\hat{F}(k) = \langle F, E_{-k}\rangle$, with $E_{-k}\in C^\infty(\Torusn)$
</div>
<div class="remark-box" markdown=1 name="">
The codomain $C_s(\mathbb{Z}^n)$ is not part of the definition, the definition of $\mathcal{F}$ on $\dzz'(\Torusn)$ is just a map that takes $\mathbb{Z}^n$ into the complex plane. The 'slowly increasing' part follows from the TVS continuity of $F: C^\infty(\Torusn)\to\mathbb{C}$. Because there exists a constant $C$ and $N$, such that 

$$
\vert \langle F,\phi\rangle \leq C\sum_{\vert\alpha\vert\leq N}\norm{\partial^\alpha \phi}_u\quad\forall \phi\in C^\infty(\Torusn)
$$

Applying this to $\hat{F}(k) = \langle F,E_{-k}\rangle$, 

$$
\begin{align}
\vert\hat{F}(k)\vert&\Lsim_F \sum_{\vert\alpha\vert\leq N}\norm{\partial^\alpha E_{-k}}_u\\
&\Lsim_F \sum_{\vert\alpha\vert\leq N}(2\pi k)^{\alpha}\cdot\norm{E_{-k}}_u\\
&\Lsim_F (1+\vert k\vert)^N
\end{align}
$$

for some $N$ that is dependent on $F$.

</div>


### Facts about $\mathcal{F}$ on $\dzz'(\Torusn)$
- The Fourier Transform is actually a linear isomorphism from $\dzz'(\Torusn)$ to $C_s(\mathbb{Z}^n)$. 

- Furthermore, the *Fourier Series* defined by taking linear combinations of $\hat{F}(k)E_k(x)\in C^\infty(\Torusn)$ **converges in $\dzz'(\Torusn)$** (in weak-$\ast$) to $F$ itself. 

- A surprising but non-trivial result is that if we view linear combinations of $\hat{F}(k)E_k(x)$ as elements in $\szz'(\realn)$, then $\sum \hat{F}(k)E_k$ **converges in $\szz'(\realn)$** (in weak-$\ast$) to $P'F$.

- Finally, the continuity of $\mathcal{F}$ on $\szz'$ gives us the following result: the Fourier Transform of $\sum \hat{F}(k)E_k$ for $F\in \dzz'(\Torusn)$ must **converge to the Fourier Transform of $P'F$**. 

$$
(P'F)^{\hat{\:}} = \mathcal{F}(\sum_{k\in\mathbb{Z}^n} \hat{F}(k)E_k) = \sum \hat{F}(k)\tau_k\delta
$$


## Periodic Sobolev Spaces $H_s$ over $\mathbb{C}$
We give the first *definition* of the **periodic Sobolev spaces** $H_s$ over the complex plane. We wish to define $H_s$ as a subspace of $\dzz'(\Torusn)$ by imposing some integrability condition on its Fourier Transform. First we define $\Lambda_s$ to be the map:

$$
\Lambda_s: \dzz'(\Torusn)\to \dzz'(\Torusn)\quad \Lambda_s F = \mathcal{F}^{-1}((1+\vert k\vert^2)^{s/2}\hat{F}(k))
$$

where $\mathcal{F}$ and its inverse should be viewed from $\dzz'(\Torusn)$ to $C_s(\mathbb{Z}^n)$.

<div class="remark-box" markdown=1 name="">
We should note $C_s(\mathbb{Z}^n)$ is closed under pointwise multiplication, and $(1+\vert k\vert^2)^{t}$ is in $C_s(\mathbb{Z}^n)$ for every $t\in\real$.
</div>

<div class="definition-box" markdown=1 name="">
If $s\in\real$, the **periodic Sobolev space** $H_s$ is a subspace of $\dzz'(\Torusn)$ where each element $F\in H_s$ satisfies

$$
\mathcal{F}(\Lambda_s F)\in l^2(\mathbb{Z}^n)\quad\text{or}\quad \sum_{k\in\mathbb{Z}^n}(1+\vert k\vert^2)^s\vert\hat{F}(k)\vert^2< +\infty
$$

</div>

As in the case for $H_s(\realn)$, we define the inner product by pulling back the inner product on $l^2$. This makes $H_s$ a Hilbert space, and the Fourier Transform is a unitary isomorphism from $H_s$ into $l^2(\mathbb{Z}^n, (1+\vert k\vert^2)^{s}dk)$, where $dk$ is the counting measure on $\mathbb{Z}^n$, and the $\sigma$-algebra on $\mathbb{Z}^n$ is assumed to be maximal. For all $f,g\in H_s$,

$$
\langle f,g\rangle_{(s)} = \langle \Lambda_s f,\Lambda_s g\rangle_{(L^2,L^2)} = \sum_{k\in\mathbb{Z}^n}\hat{f}(k)\cl{\hat{g}(k)}(1+\vert k \vert^2)^{s} = \langle \fourier(\Lambda_s f),\fourier(\Lambda_s g)\rangle_{(l^2,l^2)}
$$

and the norm on $H_s$ is $$\norm{f}_{(s)} = \norm{\Lambda_s f}_{l^2} =\sqrt{\sum_{k\in\mathbb{Z}^n}\vert\hat{f}(k)\vert^2(1+\vert k \vert^2)^s}$$

If $s\geq 0$ we can identify $H_s$ as a subset of $L^2(\Torusn)$. Furthermore, it is fruitful to consider another choice of $\Lambda_s$ that induces the same norm (hence topology), but with a different inner product.

<div class="definition-box" markdown=1 name="">
From now on $\Lambda_s$ will refer to the map

$$
\Lambda_s: \dzz'(\Torusn)\to\dzz'(\Torusn)\quad\Lambda_s F = \mathcal{F}^{-1}( (\delta_0 + 2\pi \vert k\vert^{s})\hat{F}(k))
$$

In terms of Fourier coefficients, this corresponds to 
- $\mathcal{F}(\Lambda_s F)(0) = \hat{F}(0)$, while 
- $\mathcal{F}(\Lambda_s F)(k) = 2\pi\vert k\vert^{s}\hat{F}(k)$ for $k\neq 0$

</div>

$\Lambda_s$ is clearly $C_s(\mathbb{Z}^n)$, so we define
<div class="definition-box" markdown=1 name="">
If $s\geq 0$, we define the **periodic Sobolev space $H_s$** to be the subspace of distributions on $\Torusn$ that satisfies 

$$
H_s = \bigset{f\in \dzz'(\Torusn),\: \mathcal{F}(\Lambda_s f)\in l^2(\mathbb{Z}^n,dk)}
$$

Alternatively, we can absorb the factor of $\Lambda_s$ into the measure, by writing 

$$
H_s = \bigset{f\in\dzz'(\Torusn),\: \mathcal{F}(f)\in l^2(\mathbb{Z}^n,\mu_s)}
$$

where $\mu_s(A) = \sum_{i\in A}(\delta_0(i) + \vert i\vert^{2s})$ which is simply the integral of the additional 'factor' with respect to the counting measure $dk$. We can simplify things further if we identify $H_s\subseteq L^2$ (because $s\geq 0$), and

$$
H_s = \bigset{f\in L^2(\Torusn),\: \mathcal{F}(f)\in l^2(\mathbb{Z}^n, \mu_s)}
$$

But the Fourier Transform is a unitary isomorphism between $L^2(\Torusn,dx)$ and $l^2(\mathbb{Z}^n,dk)$, combining the first and last characterization, we write

$$
H_s = \bigset{f\in L^2(\Torusn,dx),\: \Lambda_sf\in L^2(\Torusn,dx)}
$$

similar to Definition 8.1, the claim $\Lambda_s f\in L^2(\Torusn)$ should be interperted with respect to $\dzz'$. This means **there exists $g\in L^2(\Torusn)$ that realizes the duality pairing**

$$
\langle \Lambda_s f,\phi\rangle_{(\dzz',\dzz)}=\langle g,\iota\phi\rangle_{(L^2,L^2)}
$$

where $\iota:C^\infty(\Torusn)\to L^2(\Torusn)$ is the toplinear embedding.

</div>

The inner product and the norm on $H_s$ is now given by

$$
\begin{align}
\langle f,g\rangle_{(s)} &= \langle \Lambda_s f,\Lambda_s g\rangle_{(L^2,L^2)} \\
&=\langle \fourier(\Lambda_s f),\fourier(\Lambda_s g)\rangle_{(l^2,l^2)}\\
&= \sum_{k\in\mathbb{Z}^n}(\delta_0 + 2\pi \vert k\vert^s)\hat{f}(k)\cl{\hat{g}(k)}\\
\end{align}
$$

We define $A_s(j) = \delta_0(j) + \sqrt{2\pi}\vert j\vert^s$ for $j\in\mathbb{Z}^n$, so that 

$$
\begin{align}
\langle f,g\rangle_{(s)} &= \sum{k\in\mathbb{Z}^n} \vert A_s(k)\vert^2 \langle \hat{f}(k),\hat{g}(k)\rangle_{\mathbb{C}}\\
&= \langle \hat{f}(0),\hat{g}(0)\rangle_{\mathbb{C}} + 2\pi\sum_{k\in\mathbb{Z^n},\: k\neq 0}\vert k\vert^{2s}\langle \hat{f}(k),\hat{g}(k)\rangle_{\mathbb{C}}
\end{align}
$$

### Vector-valued $H_s$ loops over $\mathbb{C}$
We will now consider the case where the domain is $\real^1 = \real$, and measurable which are vector valued, i.e $f: \real\to \mathbb{C}^n$, where $n\geq 1$.

If $f = (f_1,\: \ldots, \: f_n)$ where each $f_i$ is $(\real,\mathbb{C})$ measurable. We say $f$ is $L^p$ if each $f_i\in L^p$. Continuity and smoothness properties of $f$ should be interpreted in a geometric setting. If $f\in C^p$, then it is a **morphsim of class $C^p$**.

See [this section]({{ site.baseurl }}/
{% post_url 2023-08-12-folland-distribution-excerpts %}#vector-valued-lp-spaces) for a summary.

The Fourier Transform of vector-valued functions is vector valued. Suppose $f\in L^2(\Torus, \mathbb{C}^n)$, we define

$$
\hat{f}:\mathbb{Z}\to\mathbb{C}^n\quad \hat{f}(k) = (\hat{f_1}(k),\:\ldots,\:\hat{f_n}(k))
$$

The $L^2(\Torus,\mathbb{C}^n)=L^2$ inner product of $f,g$ is defined similarly,

$$
\langle f,g\rangle_{L^2} = \sum_k \langle \hat{f}(k),\hat{g}(k)\rangle_{\mathbb{C}^n} =\sum_k\sum_i\langle\hat{f_i}(k),\hat{g_i} (k)\rangle_{\mathbb{C}} =\sum_{i\leq n}\langle f_i,g_i\rangle_{L^2}
$$

<div class="theorem-box" markdown=1 name="">
Prop 3: If $t>s\geq 0$, the Sobolev spaces decrease, while the norms increase.

$$
H_t\subseteq H_s\quad\text{and}\quad \norm{\cdot}_{(s)}\leq\norm{\cdot}_{(t)}
$$

Moreoever, the inclusion $I: H_t\to H_s$ is a continuous compact map.
</div>
<div class="proof-box" markdown=1 proof-name="">
The first two claims follow immediately from the definition of vector-valued $H_s$, and from Theorem 9.1, 9.2.

To show compactness, we will approximate $\iota$ using a sequence of finite-rank operators in the strong topology. The finite-rank operators we will choose are the symmetric partial sums.

$$
S_m f = \sum_{\vert k\vert \leq N} E_k\hat{f}(k)
$$

The idea is to use the fact that the norms on $H_s$ are defined through the pullback

$$
\Lambda_s: f\mapsto \fourier^{-1}(A_s(k)\hat{f}(k))
$$

with $A_s = \delta_0 + \sqrt{2\pi}\vert k\vert^{s}$. We approximate the inclusion map $I: H_t\to H_s$

$$
\begin{align}
\norm{S_n f - If}_{H_s}^{2} &= \norm{\sum_{\vert k\vert > N}\hat{f}(k)E_k }_{H_s}^{2}\\
&=2\pi\sum_{\vert k\vert> N}\vert\hat{f}\vert^2\vert A_s\vert^2\\
&=2\pi\sum_{\vert k\vert> N}\vert\hat{f}\vert^2\vert k\vert^{2s}\\
&=2\pi\sum_{k}\vert k\vert^{2(s-t)}\vert\cdot \vert k\vert^{2t}\cdot\vert\hat{f}\vert^2\\
&\leq 2\pi\cdot\vert N\vert^{2(s-t)}\sum_{k}\vert k\vert^{2t}\vert\hat{f}\vert^2\\
&\Lsim N^{-2a}\norm{f}^2_{H_t}
\end{align}
$$

for some $a = t-s > 0$. Taking square roots gives $$\norm{S_N f - If}_{H_s}\Lsim N^{-a}\norm{f}_{H_t}$$. This holds for an arbitrary $f\in H_t$, therefore

$$
\norm{S_N -I}_{\mathcal{L}(H_t, H_s)}\Lsim N^{-a}\quad\text{and}\quad\forall M>N,\: \norm{S_M - I}\Lsim N^{-a}\to 0
$$

therefore the inclusion map can be approximated by finite-rank operators in the strong topology, and $I$ is compact.

</div>
<div class="theorem-box" markdown=1 name="">
Prop 4: If $s>k+2^{-1}$, then $H_s(S^1)\subseteq C^k(S^1,\mathbb{C}^n)$. Essentially the periodic analogue of the Sobolev Embedding Theorem, moreover

$$
\norm{\mathcal{F}(\partial f)}_{l^1}\Lsim_{k,k-s}\norm{f}_{H_s}\quad\text{and}\quad \norm{\partial f}_{u}\Lsim_{k,k-s}\norm{f}_{H_s}
$$

for all multi-indices $\vert\alpha\vert\leq k$. 

</div>
<div class="proof-box" markdown=1 proof-name="">
We first compute the first estimate for the $l^1$ norm of the weak-$\alpha$ derivative of $f$. The following holds pointwise for $j\in\mathbb{Z}$.

$$
\vert\mathcal{F}(\partial^\alpha f)\vert = \vert 2\pi\vert^{\vert\alpha\vert}\cdot\vert j^\alpha\vert\cdot\vert \hat{f}\vert
$$

Because the domain is $1$-dimensional, the $\alpha$ is a scalar, so $\vert j^\alpha\vert = \vert j\vert^\alpha$. 

$$
\norm{\fourier(\partial^\alpha f)}_{l^1}\Lsim_k \norm{\vert j\vert^k\cdot\vert \hat{f}\vert}_{l^1}\Lsim \bignorm{\vert j\vert^s\cdot\vert\hat{f}\vert}_{l^2}\cdot\bignorm{\vert j\vert^{k-s}}_{l^2}\Lsim_{k,k-s}\norm{f}_{H_s}
$$

For the last estimate: 
- $\vert j\vert^s\leq A_s(j)$ pointwise for $j\in\mathbb{Z}$, and
- $\sum_{j}\vert j\vert^{2(k-s)}$ has exponent $2(k-s)<-1$, so it converges to *something* finite.

Now, use the Weierstrass $M$-test to show the series:

$$
\sum_{k\in\mathbb{Z}}\hat{f}(k)E_k\quad\text{converges absolutely, uniformly to some }g\in C(S^1)
$$

so $f$ (viewed as an a.e class of functions) admits a continuous representative. Furthermore, all the weak-derivatives of $f$ exist (up to order $k$) and are continuous, by a "well known result" - there exists a unique $C^k$ representative of $f$, whose ordinary derivatives represent the corresponding weak derivatives of $f$.

The $M$-test also gives us the estimate:

$$
\norm{\partial^\alpha f}_u\leq\norm{\fourier(\partial^\alpha f)}_{l^1}\Lsim_{k,k-s} \norm{f}_{H_s}
$$

if we equip $C^k$ with the standard norm $$\norm{f}_{C^k} = \sum_{\vert\alpha\vert\leq k}\norm{\partial^\alpha f}_u$$, then $$\norm{f}_{C^k}\Lsim_s \norm{f}_{H_s}$$ as well.

</div>
<div class="corollary-box" markdown=1 name="">
If $f_n\to f$ in $H_s$, and $k$ be a non-negative integer, such that $s > k + 2^{-1}$, then each $f_n$ (resp. $f$) admits unique $C^k$ representatives, whose ordinary derivatives represent the weak derivatives of $f_n$ (resp. $f$) up to order $k$. And $f_n\to f$ in $C^k$.
</div>

#### Adjoint map $j: H_{1/2}\to L^2$

<div class="theorem-box" markdown=1 name="">
Prop 5: Let $j: H_{1/2}\to L^2$ be the inclusion map. It is a compact continuous linear map, and so is the adjoint map $j^*: L^2\to H_{1/2}$ defined by

$$
\forall x\in H_{1/2},\: y\in L^2\quad \langle j(x),y\rangle_{L^2} = \langle x,j^*y\rangle_{H_{1/2}}
$$

If $y\in L^2$, then

$$
j^*y = \hat{y}(0) + \sum_{k\neq 0}(2\pi\vert k\vert)^{-1}\hat{y}(k)E_k
$$

The adjoint/pullback map also embeds $L^2$ into $H_1$, with

$$
\norm{j^*y}_{H_{1/2}}\leq \norm{j^*y}_{H_1}\leq \norm{y}_{L^2}
$$

</div>
<div class="proof-box" markdown=1 proof-name="">
From the definition of $j^*$, fix $x\in H_{1/2}$ and $y\in L^2$. The left hand side  becomes

$$
\begin{align}
\langle j(x), y\rangle_{L^2} &= \langle x,j^*y\rangle_{H_{1/2}} \\
&= \langle \fourier(jx),\fourier y\rangle_{l^2}\\
&= \sum \langle \hat{x}(k),\hat{y}(k)\rangle_{\complex^n}
\end{align}
$$

And RHS:

$$
\langle \hat{x}(0),\:(j^*y)^{\hat{\:}}(0)\rangle_{\complex^n} + 2\pi\sum_{k\neq 0}\vert k\vert\langle \hat{x}(k),\: (j^*y)^{\hat{\:}}(k)\rangle_{\complex^n}
$$

We equate both sides using a technique we will reuse in later sections, setting $x$ to an orthonormal basis vector with Fourier representation 

$$
x = E_ke_i\quad k\in\mathbb{Z}^n,\: 1\leq i\leq n
$$

(recall each $\hat{x}(k)$ is an element in $\complex^n$). The "$i$" in the exponent refers to the imaginary unit, while the "$i$" in the lower index is a dummy variable, and $$e_i = (0,\ldots,1,\ldots,0)$$ is a standard basis vector in $\complex^n$.

We see that $$\hat{y}(0) = (j^*y)^{\hat{\:}}(0)$$, and $$\hat{y}(k)=2\pi \vert k\vert (j^*y)^{\hat{\:}}(k)$$. Computing the $H_{1}$ norm of $j^*y$, we see

$$
\begin{align}
\norm{j^*y}^2_{H_{1}} &= \vert \hat{y}(0)\vert^2 + 2\pi\sum_{k\neq 0}\vert k\vert^2\biggl\vert \underbrace{2\pi\cdot\vert k\vert^{-1}\cdot\hat{y}(k)}_{\fourier(j^*y)(k)}\biggr\vert^2\\
&= \vert \hat{y}(0)\vert^2 + (2\pi)^{-1}\sum_{k\neq 0}\vert \hat{y}(k)\vert^2
\end{align}
$$

which is clearly less than $$\norm{\hat{y}}^2_{l^2} = \norm{y}^2_{L^2}$$, and $$\norm{j^*y}_{H_{1/2}}\leq \norm{j^*}_{H_1}$$ follows because norms increase.

</div>




















---


















