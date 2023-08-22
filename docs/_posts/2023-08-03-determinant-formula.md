---
layout: article
title: Determinant Formula
date: 2023-08-03 03:33
category: 
author: 
tags: ['symplectic']
summary: 
---

# Vector space tangent-cotangent isomorphisms
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



<div class="definition-box" markdown=1 name="Interior Multiplication on General Vector Spaces">
Let $V$ be a vector space with a non-singular billinear form $\mu: V\times V\to\real$. Let $a,b\in V$, and $f\in V^*$,

$$
\hat{\mu}(a) = a\lrcorner \mu\in V^* ,\quad\text{defined by}\quad \hat{\mu}(a)(b)=\mu(a,b)
$$

The inverse Riesz map through $\mu$ is denoted by $\hat{\mu}^{-1}: V^*\to V$

$$
\hat{\mu}^{-1}(f)\in V,\quad\text{where}\quad \mu\biggl(\hat{\mu}^{-1}(f), a\biggr) = f(a)
$$

Applying $\hat{\mu}^{-1}$ to a $f$ returns a vector $v$ that realizes $f$ through $\mu(v,\cdot)$.
</div>


<div class="definition-box" markdown=1 name="Interior Multiplication on Symplectic Vector Spaces ">
If $k=2n$ for $n\in\nat^+$, the standard symplectic form $\omega_0$ is non-singular. Let $\hat{\omega}_0: \real^{2n}\to (\real^{2n})^*$ denote the inverse-Riesz map, for every $a\in\real^{2n}$, and $x\in\real^{2n}$,

$$
\hat{\omega}_0(a) = \omega_0(a,\cdot)\in(\real^{2n})^* ,\quad\text{defined by}\quad \hat{\omega}_0(a)(x) = \omega_0(a,x)
$$

We also denote $\hat{\omega}_0(a)$ by $a\lrcorner\omega_0$ (reads: $a$ into $\omega_0$) by placing $a$ into the first slot of $\omega_0$. 
</div>


<div class="definition-box" markdown=1 name="Interior Multiplication of $2$-forms on Manifolds">
Let $M$ be a smooth manifold equipped with a smooth $2$-form $\omega$. If $X\in\mathfrak{X}(M)$ is a vector field, $X\lrcorner\omega\in\mathfrak{X}^*(M)$

$$
(X\lrcorner\omega)_p = X_p\lrcorner \omega_p\in T_p^* M
$$

</div>

<div class="definition-box" markdown=1 name="Interior Multiplication of $k$-forms on Manifolds">
If $\omega\in\Omega^k(M)$ is a $k$-form, and $X\in\mathfrak{X}(M)$. Interior multiplication by $X$ realized through the map 

$$\iota_X: \Omega^k(M)\to\Omega^{k-1}(M)$$

is linear over $C^\infty(M)$, and therefore orresponds to a smooth bundle homomorphism.
</div>

<div class="definition-box" markdown=1 name="Tangent-cotangent vector isomorphism on $\real^k$">
Let $f\in C^\infty(\real^k,\real)\Isomor{can}\Omega^0(\real^k)$. Denote the standard inner product on $\real^k$ by $E(\cdot,\cdot)$. $df$ is a covector field on $\real^k$.

The *gradient of $f$* is a vector field on $\real^k$. Defined by $\operatorname{grad}f = \nabla f = \hat{E}^{-1}(df)$ the Riesz map of $E$.
</div>


# Ellipsoids

## Quadratic Forms
<div class="definition-box" markdown=1 name="Quadratic Forms">
A quadratic form is a map $q: V\to\real$ such that 

$$
q(x) = 2^{-1}\hat{q}(x,x)\quad\forall x\in V
$$

where $\hat{q}$ is a symmetric billinear form. The quadratic form $q$ is **positive definite** if $\hat{q}$ defines an inner product on $V$, that is precisely when $\hat{q}$ is non-degenerate as a billinear form.

</div>

We now turn to the case where $(V,\omega)=(\real^{2n},\omega_0)$. Let $G=\operatorname{Sp}(n)$ be the **Symplectic Group** on $\real^{2n}$, the group of linear maps which preserve the symplectic form $\omega_0$. That is

$$
\forall\varphi\in G,\quad \varphi^* \omega_0 = \omega_0
$$

<div class="definition-box" markdown=1 name="$\operatorname{Sp}(n)$-action on $P$">
Let $P$ denote the space of positive definite quadratic forms on $\real^{2n}$. $G$ defines a group action on $P$ by its natural pullback. 

$$
P\times G: (q,\varphi)\mapsto q\circ\varphi
$$

We also write $\varphi^* q = q\circ\varphi$ since the group action mimcs the 'pullback' of linear maps. 
</div>

Here are some properties of this $G$-action on $P$

<div class="theorem-box" markdown=1 name="Properties of $P$">
For every $q\in P$, there exists a symplectic map $\varphi\in \operatorname{Sp}(n)$ with

$$
q\circ\varphi = 2^{-1}\sum_{i\leq n}\lambda_j (x_j^2 + x_{n+j}^2)\quad 0< \lambda_n\leq\lambda_{n-1}\leq\cdots\leq \lambda_1
$$

We call this the **canonical form of $q$**, or the **normal coordinates of $q$**. 

- Making the substituion $\lambda_j = 2r_j^{-2}$, we can write

    $$
    q\circ\varphi = \sum_{i\leq n}\dfrac{x_j^2 + x_{n+j}^2}{r_j}\quad 0< r_1(q)\leq r_2(q)\leq\cdots\leq r_n(q)
    $$
- We define $r(q) = (r_1,\ldots r_n)\in \real^{n}$, and $r$ is **invariant under $G$-action**, or

    $$
    r(q) = r(\varphi^* q)\quad\forall \varphi\in\operatorname{Sp}(n)
    $$
- Furthermore, $r$ is a **complete invariant** under $G$. More precisely, if $q$ and $q'$ are members in $P$, if $r(q) = r(q')$, there exists a symplectic map $\varphi$ that makes them $\varphi$ related, that is

    $$
    \varphi^* q' = q,\quad\text{equivalently}\quad q'(\varphi(x)) = q(x)\quad\forall x\in\real^{2n}
    $$

</div>

## Orbits on Ellipsoids
In this section, we **assume all quadratic forms are positive definite**. 
<div class="definition-box" markdown=1 name="Associated open Ellipsoid">
Let $q\in P$, it defines an open set called the **associated open ellipsoid of $q$**, denoted by $E(q)$ or $E_q$ 

$$
E(q) = \bigset{x\in\real^{2n},\: q(x)< 1} = [ q<1 ] 
$$

</div>
<div class="definition-box" markdown=1 name="$\operatorname{Sp}(n)-action on ellipsoids">
Let $\varphi\in G$, we define the group action $G\times E(P) \to E(P)$ by 

$$
\varphi^{-1}(E(q)) = E(\varphi^* q)
$$

characterized by

$$
x\in E(\varphi^* q)\iff \varphi^*q(x)<1\iff (q\circ\varphi)(x)<1\iff \varphi(x)\in E(q)\iff x\in\varphi^{-1}(E(q))
$$


</div>
<div class="theorem-box" markdown=1 name="Properties of Ellipsoids">
Let $E$ and $F$ be ellipsoids, if $r(E)$ represents the $n$-vector of numbers which induce $E$, (resp. $r(F)$), then 

- $r(\varphi(E)) = r(E)$, and
- $r(E) = r(F)$ if and only if there exists a symplectic map $\varphi$ such that $\varphi(E) = F$.
- $E$ is a subset of $F$ implies $r_j(E)\leq r_j(F)$ for $1\leq j\leq n$
- $r_j(E)\leq r_j(F)$ for $1\leq j\leq n$ if and only if there exists a symplectic map $\varphi$ with $\varphi(E)\subseteq F$.
</div>
Let $q$ be a quadratic form on $(\real^{2n},\omega_0)$, and $E = E(q)$ be the associated ellipsoid. The boundary of $E$ is the set

$$
\partial E = \bigset{z\in\real^{2n},\: q(z)=1} = [q=1]
$$

We wish to compute the HVF an its flows on $\partial E$. Writing $q$ in normal form,

$$
q = \sum_{j\leq n}\dfrac{x_j^2 + x_{n+j}^2}{r_j^2} = \sum_{j\leq n}\lambda_j(x_j^2 + x_{n+j}^2)
$$

Relabelling coordinates we can assume $z_j = (x_j, x_{n+j})$ for $1\leq j\leq n$, and the normal form of $q$ corresponds to [the maximal hyperbolic decomposition]({{ site.baseurl }}/{% post_url 2023-08-12-folland-distribution-excerpts %}#excerpts-form-roman) of $(\real^{2n},\omega_0)$. Where

$$
\real^{2n} = \bigoplus_{j\leq n}V_j
$$

Computing the HVF $X_q(x) = J\nabla q(x)$ reads (see Note 0.1)

$$
\nabla q(z) = \sum_{j=1}^{n} \dfrac{2x_j}{r_j^2}\dfrac{\partial}{\partial x_j} + \dfrac{2x_{n+j}}{r_j^2}\dfrac{\partial}{\partial x_{n+j}}\implies J\nabla q(z) = \sum_{j=1}^{n} \dfrac{2x_{n+j}}{r_j^2}\dfrac{\partial}{\partial x_j} - \dfrac{2x_j}{r_j^2} \dfrac{\partial}{\partial x_{n+j}}
$$

Using $$\dfrac{1}{r_j^2} = \dfrac{\lambda_j}{2}\:\forall j=1,\ldots,n$$, 

$$
\begin{align}
J\nabla q(x) &= \sum_{j\leq n} \lambda_jx_{n+j}\dfrac{\partial}{\partial x_j} - \lambda_j x_j\dfrac{\partial}{\partial x_{n+j}}\\[2ex]
&=\sum_{j\leq n}\lambda_j\begin{bmatrix}\dfrac{\partial}{\partial x_{j}} & \dfrac{\partial}{\partial x_{n_j}}\end{bmatrix}\begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}\begin{bmatrix} x_j \\ x_{n+j}\end{bmatrix}\\[2ex]
&=\sum_{j\leq n}\begin{bmatrix}\dfrac{\partial}{\partial x_{j}} & \dfrac{\partial}{\partial x_{n_j}}\end{bmatrix}\lambda_j J\begin{bmatrix} x_j \\ x_{n+j}\end{bmatrix}
\end{align}
$$

Suppose $z(t) = \biggl(z_1(t),\ldots,z_n(t)\biggr)$ is a solution to the HVF $X_q$. It is clear that the $z_j$'s are pairwise independent of each other, and each $z_j$ must satisfy

$$
\begin{bmatrix}\dot{x}_j \\ \dot{x}_{n+j}\end{bmatrix} = \lambda_j J \begin{bmatrix}{x_j} \\ {x_{n+j}}\end{bmatrix}\implies z_j(t) = e^{\lambda_j Jt}z_j(0)\quad \forall t\in\real
$$

where $0<\lambda_n\leq\lambda_{n-1}\leq\cdots\leq\lambda_1$, and that $\pm i\lambda_j$ are **precisely the eigenvalues** of the linear HVF induced by $q$. More is true, we claim that

$$
\pi r_1^2 = \inf\bigset{\vert A(z)\vert,\quad z\text{ is a closed characteristic on }\partial E }
$$

where this infimum is attained. Recall $A$ denotes the action of a closed characteristic on $(\real^{2n},\omega_0)$, which is defined

$$
A(z) = 2^{-1}\int_{0}^T \langle -J\dot{z},\: z\rangle_{\real^{2n}}
$$

The proof of this is straightforward, but requires two equations.

<div class="note-box" markdown=1 name="Formula for multiplication by $J$">
Let $$J = J_2 = \begin{bmatrix}0 & 1\\ -1 & 0\end{bmatrix}$$, let $(x_1, y_1)$ be the basis of $\real^2$. If $z = ax_1 + by_1$, then $Jz = bx_1 - ay_1$. More generally, let $$J = \begin{bmatrix} 0 & I_n\\ -I_n & 0\end{bmatrix}$$, and $(x_1,\ldots, x_n, y_1,\ldots, y_n)$ be a basis for $\real^{2n}$. 

$$
z = \sum_{j=1}^n a_jx_j + b_jy_j\quad\text{then}\quad Jz = \sum_{j=1}^n b_jx_j - a_jy_j
$$

</div>
<div class="note-box" markdown=1 name="Matrix Exponential of $J$">
Suppose $J=J_2$, the matrix exponential $e^{\lambda 2\pi Jt} = \Epsilon_{\lambda}(t)$ is given by the equation

$$
\Epsilon_{\lambda}(t) = \begin{bmatrix}\cos(2\pi \lambda t) & \sin(2\pi \lambda t) \\ -\sin(2\pi\lambda t) & \cos(2\pi\lambda t)\end{bmatrix} = \begin{bmatrix} c_\lambda & s_\lambda \\ -s_\lambda & c_\lambda \end{bmatrix}
$$

Abbreviating $\cos(2\pi\lambda t) = c_\lambda$, and respectively for $s_\lambda$. If $J = J_{2n}$, it becomes

$$
\Epsilon_\lambda(t) = \begin{bmatrix} c_\lambda & s_\lambda \\ -s_\lambda & c_\lambda \end{bmatrix}_{n\times n\text{ blocks}}
$$

Furthermore, we can write $$\Epsilon_s x = e^{sJ}x = \cos(s)x + \sin(x)Jx$$.

</div>


Now, let $\omega_j(t)$ be the solution that has lives on $V_j$ exclusively, meaning

$$
\omega_j(t) = \biggl(0,\ldots,z_j(t),0,\ldots,0\biggr)
$$

Define $z_j(0)\in V_j\cap \partial E$, so that $q(z_j(0))=1$, and $\vert z_j(0)\vert^2 = r_j^2$. Using the determinant formula to compute the action,

<div class="note-box" markdown=1 name="Cosine and Sine computaitons">
Let $x_j(t) = \cos(\lambda_j t)x_j(0) + \sin(\lambda_j t)x_{n+j}(0)$, and $x_{n+j}(t) = -\sin(\lambda_j t)x_j(0) + \cos(\lambda_j t)x_{n+j}(0)$. Abbreviating by $c_{\lambda_j}$, and $s_{\lambda_j}$, and define $a = x_j(0)$, $b = x_{n+j}(0)$. Then,

$$
\begin{align}
\dot{x}_j &= \lambda_j(-s_{\lambda_j}a + c_{\lambda_j}b) = \lambda_j x_{n+j}\\[2ex]
\dot{x}_{n+j} &= \lambda_j(-c_{\lambda_j}a - s_{\lambda_j}b) = -\lambda_j x_{j}\\[2ex]
\end{align}
$$

Evaluating the integrand (the determinant) pointwise, $\forall t\in [0, 2\pi\lambda_j^{-1}]$

$$
\begin{align}
\det\biggl(\begin{bmatrix}\dot{x}_j & x_j \\ \dot{x}_{n+j} & x_{n+j}\end{bmatrix}\biggr) &= \dot{x}_jx_{n+j}-\dot{x}_{n+j}x_{j} = \lambda_j(\vert x_j\vert^2 + \vert x_{n+j}\vert ^2)\\[2ex]
&= \lambda_j\vert z_j\vert^2 = \lambda_jr_j^2\\[2ex]
&= 2\lambda_j^{-1}
\end{align}
$$

where $z_j = (x_j, x_{n_j})$.

</div>


<div class="remark-box" markdown=1 name="">
The whole proof is a bit awkward because we wish to consider $z_j(t)$ as coefficients that can be summed to $z(t)$, i.e

$$
z(t) =\sum_{j\leq n}x_j(t)e_j + y_j(t)e_{n+j}
$$

but at the same time we want 

$$
z(t) = \sum_{j\leq n}z_j(t)
$$

</div>

So the action is pointwise equal to $2\lambda_j^{-1}$. But $\omega_j$ has period $2\pi\lambda_j^{-1}$, therefore 

$$A(z) = 2^{-1}\int_0^{2\pi\lambda_j^{-1}} 2\lambda_j^{-1} dt= 2\pi\lambda_j^{-2}=\pi r_j^2$$

It is clear that every closed characteristic must be the sum of these eigenmodes, and the claim follows immediately from linearity of the **integrand form of the determinant formula**, which is used in [the previous section]({{ site.baseurl }}/{% post_url 2023-08-01-symplectic-geometry %}#proof-for-formulas).

<div class="remark-box" markdown=1 name="">
We summarize this section:

The orbits of ellipsoids depend upon the numbers $r_j$, and solutions to a the HVF induced by a quadratic form is precisely the sum of the linear eigenmodes, $e^{\lambda_j J_2 t}$. These eigenmodes live on disjoint hyperbolic planes, and they correspond to solutions with period $2\pi\lambda_j^{-1}$
</div>

# Smooth Transition Function
<div class="theorem-box" markdown=1>
On page 74, we require a function $f:\real\to\real$ that satisfies

- $f(s) = m(H)$ for $s\leq 1$,
- $f(s) \geq (\pi + \varepsilon)s$ for all $s\in\real$,
- $f(s) = (\pi+\varepsilon)s$ for $s$ large 
</div>
<div class="proof-box" markdown=1 proof-name="Proof of Smooth Transition Function:">

The following is a smooth transition function that transistions from a constant to a linear function, computing its derivative,

<iframe src="https://www.desmos.com/calculator/zmuh9vgmb3?embed" width="800" height="800" style="border: 1px solid #ccc" frameborder=0></iframe>

[Desmos](https://www.desmos.com/calculator/rcxvs2bzvd)

Computation of the derivatives is an easy task, verification later

The upper bound on the derivative controls $T$ of any periodic orbit of $X_{\cl{H}}$.

- Include the argument of separating the integral curves in and outside the ellipsoid $E$.
</div>