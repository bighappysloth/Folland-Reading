---
layout: article
title: Determinant Formula
date: 2023-08-03 03:33
category: 
author: 
tags: ['symplectic']
summary: 
---

#### Lemma 1 (Determinant Formula)
Let $x=(x_1,\ldots ,x_{2n})$ and $y=(y_1,\ldots,y_{2n})$, and denote the standard basis of $\real^{2n}$ by $(e_1,\ldots ,e_{2n})$, so that

$$
\begin{cases}x=\sum_{j=1}^n x_je_j + x_{n+j}e_{n+j}\\ y=\sum_{j=1}^n y_je_j + y_{n+j}e_{n+j}\end{cases}\implies \begin{cases}Jx=\sum_{j=1}^n x_{n+j}e_j - x_{j}e_{n+j}\\ Jy=\sum_{j=1}^n y_{n+j}e_j - y_{j}e_{n+j}\end{cases}
$$

Expanding the inner product, and indexing the sum in $x$ by $j$ and the sum in $y$ by $k$,

$$
\begin{align}
\langle -J\dot{x},y\rangle &= \sum_{j=1}^n\sum_{k=1}^n\biggl\langle -\dot{x}_{n+j}e_{j} + \dot{x}_je_{n+j},\: y_ke_k + y_{n+k}e_{n+k}\biggr\rangle \\
&= \sum_{j,k=1}^n\langle-\dot{x}_{n+j}e_j,y_{k}e_{k}\rangle + \langle-\dot{x}_{n+j}e_j,y_{n+k}e_{n+k}\rangle + \langle\dot{x}_{j}e_{n+j},y_{k}e_{k}\rangle + \langle\dot{x}_{j}e_{n+j},y_{n+k}e_{n+k}\rangle\\
&= \sum_{j=1}^n -\dot{x}_{n+j}y_k + \dot{x}_jy_{n+k}\\
&= \sum_{j=1}^n \det\biggl(\begin{bmatrix}\dot{x}_{j} & y_j\\ \dot{x}_{n+j} & y_{n+j}\end{bmatrix}\biggr)
\end{align}
$$ 

#### Lemma 2
We wish to show

$$
\int_0^1 \sum_{j=1}^n \gamma_j\dot{\gamma}_{n+j} dt = (-1)\int_0^1\sum_{j=1}^n \gamma_{n+j}\dot{\gamma}_{j}dt
$$

Where $\gamma = (\gamma_1,\ldots,\gamma_{2n})$ is periodic. Indeed, by integration by parts. Recall $\int_X a\dot{b} = ab\vert_{\partial X} - \int_X \dot{a}b$,

$$
\text{LHS} = \underbrace{\sum_{j=1}^n\gamma_j \gamma_{n+j}\biggr\vert^1_0 }_{=0} - \int_0^1\sum_{j=1}^n\gamma_{n+j}\dot{\gamma}_{j}dt = \text{RHS}
$$

### Tangent-cotangent isomorphisms
Let $V$ be a normed vector space over $\real$. If $f\in V^*$, and $x\in V$, we denote

$$
f(x) = \langle f,x\rangle_{(V^*, V)}
$$

If $V=\real^{k}$, and $f$ has simple matrix representation $A\in\real^{1\times k}$, identifying $x$ with its matrix representation,

$$
\langle f,x\rangle = Ax
$$

$\real^{k}$ is also an inner product space with the non-singular billinear form $\langle\cdot,\cdot\rangle_{\real^k}$. By Riesz isomorphism, every covector $a\in (\real^{k})^*$ corresponds to a unique vector $a'\in\real^k$ that realizes $a$ through the inner product,
{:.info}

$$
\langle a,x\rangle_{((\real^k)^*, \real^k)} = a(x) = \langle a', x\rangle_{\real^k}
$$


#### Interior Multiplication on General Vector Spaces
Let $V$ be a vector space with a non-singular billinear form $\mu: V\times V\to\real$. Let $a,b\in V$, and $f\in V^*$,

$$
\hat{\mu}(a) = a\lrcorner \mu\in V^* ,\quad\text{defined by}\quad \hat{\mu}(a)(b)=\mu(a,b)
$$

The inverse Riesz map through $\mu$ is denoted by $\hat{\mu}^{-1}: V^*\to V$

$$
\hat{\mu}^{-1}(f)\in V,\quad\text{where}\quad \mu\biggl(\hat{\mu}^{-1}(f), a\biggr) = f(a)
$$

Applying $\hat{\mu}^{-1}$ to a $f$ returns a vector $v$ that realizes $f$ through $\mu(v,\cdot)$.

#### Interior Multiplication on Symplectic Vector Spaces 
If $k=2n$ for $n\in\nat^+$, the standard symplectic form $\omega_0$ is non-singular. Let $\hat{\omega}_0: \real^{2n}\to (\real^{2n})^*$ denote the inverse-Riesz map, for every $a\in\real^{2n}$, and $x\in\real^{2n}$,

$$
\hat{\omega}_0(a) = \omega_0(a,\cdot)\in(\real^{2n})^* ,\quad\text{defined by}\quad \hat{\omega}_0(a)(x) = \omega_0(a,x)
$$

We also denote $\hat{\omega}_0(a)$ by $a\lrcorner\omega_0$ (reads: $a$ into $\omega_0$) by placing $a$ into the first slot of $\omega_0$. 

#### Interior Multiplication on Manifolds
Let $M$ be a smooth manifold equipped with a smooth $2$-form $\omega$. If $X\in\mathfrak{X}(M)$ is a vector field, $X\lrcorner\omega\in\mathfrak{X}^*(M)$

$$
(X\lrcorner\omega)_p = X_p\lrcorner \omega_p\in T_p^* M
$$

#### General Case
If $\omega\in\Omega^k(M)$ is a $k$-form, and $X\in\mathfrak{X}(M)$. Interior multiplication by $X$ realized through the map 

$$\iota_X: \Omega^k(M)\to\Omega^{k-1}(M)$$

is linear over $C^\infty(M)$, and therefore orresponds to a smooth bundle homomorphism.

#### Tangent-cotangent vector isomorphism on $\real^k$
Let $f\in C^\infty(\real^k,\real)\Isomor{can}\Omega^0(\real^k)$. Denote the standard inner product on $\real^k$ by $E(\cdot,\cdot)$. $df$ is a covector field on $\real^k$.

The *gradient of $f$* is a vector field on $\real^k$. Defined by $\operatorname{grad}f = \nabla f = \hat{E}^{-1}(df)$ the Riesz map of $E$.
{:.info}






