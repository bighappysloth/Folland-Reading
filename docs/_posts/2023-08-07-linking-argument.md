---
layout: article
title: Linking Argument
date: 2023-08-07 01:55
category: 
author: 
tags: ['symplectic']
summary: 
---
# Lang Manifolds
From Lang's Differential and Riemannian Manifolds,


## Category Theory
This section is for self-reference only.

Let $\operatorname{Fun}(U, U')$ be the space of covariant functors from the category $U$, and $U'$. Its objects are covariant functors, and its morphisms are called *natural transformations*. Let $\lambda,\mu\in\operatorname{Fun}(U,U')$, we define the $\operatorname{Mor}(\lambda,\mu)$ as follows.

![lang-natural-transformations]({{ site.baseurl }}{% link /images/lang-natural-transformations.png %})


## Topological Vector Space
We define the following symbols, let $E$ and $F$ be TVS in the usual sense. 

<div class="definition-box" markdown=1>
- Lang also refers to TVS as *Banachable spaces*. All TVS in the book will be over the reals.
- $L(E)=L(E,\real)$ is space of continuous real-valued linear functionals,
- $\operatorname{End}(E) = L(E,E)$ is the space of linear endomorphisms,
- $\operatorname{Laut}(E) \subseteq \operatorname{End}(E)$ is the space of linear automorphisms
</div>


# Differentiation on TVS



## Differentiability

### Little o(t)
<div class="definition-box" markdown=1>
A real-valued function in a real variable is called $o(t)$ if 

$$
    \lim_{t\to 0}o(t)/t = 0
$$

Note this implies $\lim o(t)=0$ as well.
</div>


### Tangent to $0$
Let $E$ and $F$ be TVS, a map $\varphi: U\to F$ where $U$ is an open neighbourhood of in $E$ into $F$, is *tangent to $0$* if

$$
\vert \varphi(y)\vert\leq \vert y \vert \psi(y)
$$

for some $\lim \psi(y)=0$ as $y\to 0$. This is a norm dependent definition. More generally, $\varphi: U\to F$ is tangent to $0$ if for every neighbourhood of the origin $W\subseteq F$, there exists a neighbourhood of the origin $V\subseteq E$ such that

$$
\varphi(tV)\subseteq o(t)W 
$$

where $tV = \bigset{tx,\: x\in V }$, and similarly for $o(t)W$. For $t>0$.
### Differentiability
<div class="definition-box" markdown=1>
Let $E$ and $F$ be TVS, and $f: U\to F$ be continuous on an open set $U\subseteq E$, we say $f$ is *differentiable* at $x_0\in U$ if there exists a continuous linear map $\lambda: E \to F$ such that

$$
f(x_0 + y) = f(x_0) + \lambda y + \varphi (y)
$$

where $\varphi: U\to F$ is *tangent to $0$*. A few more things

- We say $f'(x_0) = \lambda$, so we should view $f': U\to L(E,F)$, where $L(E,F)$ is the space of continuous linear mappings,
- $f$ is in $C^1$ if $f'$ is continuous,
- The second derivative $D^2 f$ is a map $D^2f: U\to L(E, L(E,F))$, 
- The $p$-th derivative $D^p f$ is defined as $D(D^{p-1}f)$, is a linear map of $U$ into the space of bounded linear maps $L(E, L(E,\ldots,))$,
- If $D^k f$ is continuous for $k=1,\ldots,p$, then $f\in C^p$.
</div>



# Extension Packs

## Tangent, cotangent bundle isomorphsim for Hilbert Manifold
Using the same notation $E = H^{1/2}$, is a Hilbert space, that is also a Hilbert manifold with the global chart $(E, \operatorname{can})$. The manifold structure we will put on $E$ is the $C^1$ structure. By Proposition 6.1 of Lang:


![Lang 6-1]({{ site.baseurl }}{% link /images/lang-6-1.png %})


# Minimax Argument
Want to use the minimax lemma on the gradient flow of $\Psi: E\to\real$, 

$$
\dot{x} = -\nabla \Psi(x),\: x\in E
$$

has a global flow, because it is globally Lipschitz continuous by Lemma 4, because it has gradient

$$
\nabla \Psi (x) = \nabla a(x) - \nabla b(x) = (P^+ - P^-)x - \nabla b(x)
$$

For $x,y\in E$, we have

$$
\begin{align}
\lVert\nabla \Psi (x) - \nabla \psi (y)\rVert_{\real}\: &\Lsim\: \norm{(P^+ - P^-)(x-y)} + \norm{\nabla b(x) - \nabla b(y)}\\
&\Lsim\: \norm{P^+ - P^-}\norm{x-y} + \norm{x-y}\\
&\Lsim\: \norm{x-y}
\end{align}
$$

Cauchy-Picard gives us the completeness of flows, see Lang 

## Integral Flows on Abstract Manifolds
In infinite dimensions, most of the proofs for manifolds do not work. However, we can still make statements about the algebraic structure of infinite-dimensional manifolds.

If $\xx$ is a manifold of class $C^p$, with $p\geq 2$, then its tangent bundle $\pi: T\xx \to \xx$ is of class $C^{p-1}$, $p\geq 1$. We define

<div class="definition-box" markdown=1>
**Time-independent vector field** on $\xx$ is a section of the tangent bundle, i.e a $C^{p-1}$ morphism $\zeta: \xx\to T\xx$, such that $\pi\circ \zeta = \id{\xx}$    
</div>

