---
layout: article
title: Notes on Symplectic Geometry
date: 2023-08-01 14:37
category: 
tags: ['symplectic']
---

See the document 'Symplectic Geometry and Hamiltonian Systems' for a dicussion on Metric Vector Spaces, algebraic construcitons, etc. 

TODO: add almost complex structures on linear spaces, and almost complex structures on manifolds.

# Symplectic Manifolds
A symplectic manifold is a smooth manifold of dimension $2n$, where $n$ is a positive integer, equipped with a smooth $2$-form that is non-singular when restricted to the fiber of each tangent space $T_pM$.

# Standard Symplectic Manifold $(\real^{2n},\omega_0)$
Let $n$ be a positive integer, and $\omega_0$ be the standard symplectic form on the real vector space $\real^{2n}$. Define $$J = \begin{bmatrix} 0 & I_n \\ -I_n & 0\end{bmatrix}$$, notice $J$ resembles multiplication by $-i$ if we identify $\real^{2n}\cong\mathbb{C}$ (more on this later).

## Properties of $\omega_0$
We will list and prove most of the properties that we will need of $\omega$.

- We can write the $\omega_0$ in terms of the standard inner product on $\real^{2n}$ as a vector space (or the standard Euclidean metric on $(\real^{2n}, \langle\cdot,\cdot\rangle)$ as a Riemannian Manifold).

    $$
    \omega_0(u,v) = \langle Ju,v\rangle,\quad\text{and}\quad \omega(u,Jv) = \langle u,v\rangle\quad\forall u,v\in\real^{2n}
    $$

- $\omega_0$ is an exact $2$-form

    $$
    \omega_0 = \sum_{j=1}^n dy_j\wedge dx_j = d\lambda
    $$

    where $$\lambda = \sum_{j=1}^n y_j dx_j$$. Computing the exterior derivative $$d\lambda = \sum_{j=1}^n d(y_j dx_j) = \sum_{j=1}^N dy_j\wedge dx_j=\omega_0$$ as required.

## Symplectic Diffeomorphisms on $(\real^{2n},\omega_0)$
A diffeomorphism $\varphi\in\mathcal{D}(\real^{2n})$ is *symplectic* if it preserves the symplectic form $\omega_0$, that is

$$
\varphi^* \omega_0 = \omega_0,\quad (\varphi^* \omega_0)_p (a,b) = (\omega_0)_{\varphi(p)}(d\varphi_p(a),\: d\varphi_p(b)) = \omega_p(a,b),\: \forall p\in\real^{2n},\: a,b\in T_p\real^{2n}
$$

since $d\varphi_p$ corresponds precisely to the Jacobian matrix of $\varphi$ at $p$, which we will denote by $\varphi'$, and recall $\varphi^*$ is just the precomposition of $\omega_0$ with $d\varphi$. Writing everything in matrices,

$$
\biggl\langle J\varphi'(x)a,\varphi'(x)b\biggr\rangle =(\omega_0)_{\varphi(x)}(d\varphi_x(a), d\varphi_x(b)) = (\omega_0)_x(a,b) = \biggl\langle Ja,b\biggr\rangle
$$

Which implies $$\biggl\langle \varphi'(x)^T J \varphi'(x)a,b\biggr\rangle = \biggl\langle Ja,b\biggr\rangle$$, this holds for every $a,b\in T_x\real^{2n}\Isomor{L}\real^{2n}$, therefore

$$
    \varphi'(x)^TJ\varphi(x) = J,\quad\forall x\in\real^{2n}
$$

Since $\varphi'(x)$ is a symplectic matrix, it has determinant $1$.



## Symplectic Invariance of the action
Let $\gamma$ be a closed curve in $\real^{2n}$, we sometimes refer to closed curves as *closed characteristics*, we define the *symplectic action*, or *action* on $\gamma$ 

$$
    A(\gamma) =\int_{\gamma}\lambda\in\real
$$

We claim, if $\varphi\in \operatorname{Sp}(n)$, then $A(\varphi\circ \gamma) = A(\gamma)$. First we need a lemma.


### Lemma
The $1$-form $\lambda -\varphi^*\lambda$ is exact iff $\varphi$ is a symplectic diffeomorphism on $\real^{2n}$. Indeed, 

$$
d(\lambda-\varphi^* \lambda)=d\lambda - \varphi^* (d\lambda) = \omega_0-\omega_0=0
$$

since the exterior product commutes with tensor pullbacks (Lee 14.23d). So $\lambda-\varphi^* \lambda$ is a closed form. Poincare's Lemma, which states the $k$-th [de Rham cohomology group]({{ site.baseurl }}/{% post_url 2023-08-03-derham-cohomology %}), of a contractible domain is trivial for $k\geq 1$, therefore $\lambda-\varphi^* \lambda$ is exact.


### Proof of Invariance
If $M$ is a smooth manifold, and $\gamma$ is any curve (not necessarily closed) on $M$. The line integral of a $1$-form $\lambda\in\mathfrak{X}^* (M)$ over the curve $\gamma$ is defined

$$
\int_\gamma \lambda = \int_{[a,b]}\gamma^* \lambda\quad \gamma^* (\lambda)\in\mathfrak{X}^*(\real)
$$

since $\mathfrak{X}^* (\real)$ is one-dimensional, we can write $\gamma^* (\lambda)$ in terms of the global frame $dt$. There exists a unique $f(t)\in C^\infty(\real)$ where

$$
f(t)dt = \gamma^* (\lambda)
$$

The closed line integral over exact forms is $0$, so

$$
A(\gamma) = \int_\gamma \lambda = \int_\gamma \varphi^* \lambda = \int_{\varphi\circ \gamma}\lambda = A(\varphi\circ\gamma)
$$

### Action computations
By Lee Prop 11.37, the line integral is invariant under *forward reparametrizations*. If $\gamma$ is a (not necessarily closed) curve on $M$, and $f$ is a diffeomorphism on $\real$ which is strictly increasing, then 

$$
\int_{\gamma}\lambda = \int_{\gamma\circ f}\lambda,\quad\forall\lambda\in\mathfrak{X}^*(M)
$$

With this, let $\gamma$ be reparametrized so that it has period $1$. We will prove the following formula
{:.info}

$$
A(\gamma) = \int_\gamma \lambda = 2^{-1}\int_0^1\biggl\langle -J\dot{\gamma},\:\gamma\biggr\rangle dt
$$


- Let $(x_1,\ldots,x_n,x_{n+1},\ldots x_{2n})$ be the standard coordinates on $\real^{2n}$, and $\gamma = (\gamma_1\,\ldots,\gamma_{2n})$. The left hand side becomes 

    $$
    A(\gamma) = \int_0^1\sum_{j=1}^n \gamma_{n+j}\dot{\gamma}_{j}dt
    $$

- Right hand side: examining the integrand using the [Lemma 1 (determinant formula)]({{ site.baseurl }}/{% post_url 2023-08-03-determinant-formula %}), 

    $$
    2^{-1}\biggl\langle -J\dot{\gamma},\: \gamma\biggr\rangle = 2^{-1}\sum_{j=1}^n \det\biggl(\begin{bmatrix} \dot{\gamma}_j & \gamma_j \\ \dot{\gamma}_{n+j} & \gamma{n+j} \end{bmatrix}\biggr) = 2^{-1}\sum_{j=1}^n \dot{\gamma}_{j}\gamma_{n+j} - \dot{\gamma}_{n+j}\gamma_{j} dt
    $$

- Integrating the right hand side, we obtain

    $$
    \int_0^1 2^{-1}\biggl\langle -J\dot{\gamma},\gamma\biggr\rangle dt = \int_0^1 2^{-1}\sum_{j=1}\dot{\gamma}_{j}\gamma_{n+j} - \dot{\gamma}_{n+j}\gamma_j dt
    $$

- Using [Lemma 2]({{ site.baseurl }}/{% post_url 2023-08-03-determinant-formula %}), 

    $$
    \int_0^1 2^{-1}\biggl\langle -J\dot{\gamma},\gamma\biggr\rangle dt = 2^{-1}\int_\gamma\lambda + (-1)2^{-1}\int_\gamma\lambda = \int_\gamma\lambda = A(\gamma)
    $$

## Hamiltonian Vector Fields on $\real^{2n}$
Let $(\real^{2n},\omega_0)$ be the standard symplectic structure. If $H\in C^\infty(\real^{2n})$, the *Hamiltonian Vector Field associated to $H$* is defined

$$
X_H = (-1)\hat{\omega}_0^{-1}(dH)
$$

Identifying $\mathfrak{X}(\real^{2n})\Isomor{L}C^\infty(\real^{2n},\real^{2n})$ (because $\real^{2n}$ is parallelizable). For every $x\in\real^{2n}$, and $a\in T_x\real^{2n}\Isomor{L}\real^{2n}$,

$$
\begin{align}
\omega_0(X_H(x), a) &= (-1)dH(x)(a)\\
\langle JX_H(x),a\rangle_{\real^{2n}} &= \langle -dH(x), a\rangle_{((\real^{2n})^*, \real^{2n})}\\
&= \langle (-dH(x))^T,a\rangle_{\real^{2n}}\\
&=\langle -\nabla H(x), a\rangle_{\real^{2n}}
\end{align}
$$

This holds for an arbitrary $a\in\real^{2n}$, so $JX_H(x) = -\nabla H(x)\implies X_H(x) = J\nabla H(x)$.
{:.warning}

## Independence of Hamiltonian defining hypersurfaces
Let $S$ is a (compact) regular hypersurface on $\real^{2n}$ defined by $F,H\in C^\infty(\real^{2n},\real)$,

$$
S = \{F=c\} = \{H=c'\},\quad\text{and}\quad dF\vert_S,\: dH\vert_S\neq 0
$$

We claim there exists a smooth, nowhere vanishing function $\rho: S\to\real$ (take) such that

- $dF(x) = \rho(x)dH(x)$ for all $x\in S$,
- If $\varphi^s(x)$ and $\theta^t(x)$ are flows of the HVFs $X_F$ and $X_H$ on $S$. The following IVP provides a unique solution that relates the two flows by reparametrization. $\dfrac{dt}{ds}=\rho(\varphi^s(x)),\: t(0)=0$ So that $\varphi^s(x) = \theta^{\alpha(s,x)}(x)$ for some smooth, nowhere vashing function $\alpha(\cdot,x)$
- $X_F$ and $X_H$ define the same periodic orbits on $S$, if any.

### Proof

Both $F$ and $H$ are global definining functions for the embedded submanifold $S$, if $p\in S$ is arbitrary, the *exterior tangent space* of $p$ coincides precisely with the $\ker{dF_p} = \ker{dH_p}$ (Lee 5.38, 5.40).

$$
\ker{dH_p} = T^{ext}_p S = \ker{dF_p}
$$

Using the canonical identifications 

- $T_{F(p)}\real \cong\real\cong T_{H(p)}$,
- $T^{ext}_p S\cong\real^{2n}$,
- $T_p \real^{2n}\cong\real^{2n}$,

By the First Isomorphism Theorem, then by Riesz Isomorphism, there exists unique vectors $f_p,h_p\in\real^{2n}$ such that for every $v\in T_p \real^{2n}$,

$$
dF_p(v) = f_p^Tv \quad\text{and}\quad dH_p(v) = h_p^Tv
$$

Since $T_p^{ext}S$ has codimension $1$, it is clear there exist a nowhere vanishing $\rho(p)\in\real$ with

$$
f_p = \rho(p)h_p
$$

To show $\rho: S\to\real$ is smooth, we normalize $dF$ and $dH$ along $S$. Let $(X_1,\ldots, X_{2n})$ be the global coordinate frame on $\real^{2n}$, 

$$
L_F(p) = \sqrt{\sum_{j=1}^{2n}\vert (X_jF)(p) \vert^2},\quad\text{and}\quad L_H(p) = \sqrt{\sum_{j=1}^{2n}\vert (X_jH)(p) \vert^2}
$$

Both $L_F$ and $L_H$ are smooth functions on $S$ (with respect to the structure on $S$), and $\rho = L_H/L_F$ means $\rho$ is smooth is as well. Next, $dF = \rho dH$ means $(dF)^T = (\rho dH)^T$, 
    
$$
X_F = J\nabla F = \rho J\nabla H = \rho X_H
$$

#### Searching for parametrization
In search for a function $t(s,x)$ such that the integral curves agree,

$$
\psi^s(x) = \varphi^t(x),\quad \forall x\in S,\: t(0,x)=0
$$

We differentiate both sides and use the chain rule, 

$$
X_F(\psi^s(x)) = X_H(\varphi^t(x))\dfrac{dt}{ds}\biggr\vert_s\implies X_F = \rho X_H = X_H\dfrac{dt}{ds}\biggr\vert_s
$$

We come to $$\dfrac{dt}{ds} = \rho(\varphi^t(x)) =\rho(\psi^s(x))$$, or $$t(s,x) = \int_0^s \rho(\varphi_x(u))du$$. The latter is strictly monotonic, and the constant (resp. non-constant) periodic solutions of $X_F$ correspond precisely to those of $X_H$.


# Symplectic Diffeomorphisms on $(M,\omega)$
Let $(M,\omega)$ and $(N,\eta)$ be symplectic manifolds of dimension $2n$. Suppose $u: M\to N$ is a symplectic diffeomorphism, meaning it is a diffeomorphism between smooth manifolds; and for every $p\in M$, $v_1, v_2\in T_pM$, 

## Pullback through $u$

### Pullback of symplectic form
$$
(u^*\eta)_p(v_1,v_2) = \eta_{u(p)}\biggl(du_p(v_1),\: du_p(v_2)\biggr) = \omega_p(v_1,v_2)
$$

where $u^*$ denotes the tensor field pullback through $u$, by precomposing $\eta$ with $u$ and $du$ in its arguments.

### Pullback of smooth functions
We define the pullback of a $0$-form (which is also a tensor),

$$
u^*: C^\infty(N)\to C^\infty(M),\quad (u^*f)(p) = (f\circ u)(p),\:\forall f\in C^\infty(N)
$$

### Pullback of vector fields
Let $Y$ be a vector field on $N$. $u^* Y$ is a vector field on $M$, such that for every $p\in M$, we define $$u^*Y (p) = ((du^{-1})_{u(p)}) ( Y_{u(p)} )$$, or

$$
( u^*Y ) = \biggl((du)^{-1}\circ Y\circ u\biggr)
$$

<!-- https://q.uiver.app/#q=WzAsNyxbMCwwLCIoTSxcXG9tZWdhKSJdLFsyLDAsIihOLFxcZXRhKSJdLFswLDIsIlRNIl0sWzIsMiwiVE4iXSxbMCw0LCJDXlxcaW5mdHkoTikiXSxbMCw2LCJcXG1hdGhmcmFre1h9XiooTikiXSxbMiw2LCJcXG1hdGhmcmFre1h9KE4pIl0sWzAsMSwidSJdLFswLDIsInVeKlhfSCIsMl0sWzEsMywiWF9IIl0sWzMsMiwiZHVeey0xfSJdLFs0LDUsImQiLDJdLFs1LDYsIi1cXGhhdHtcXGV0YX0iLDJdLFs0LDYsIi1cXGhhdHtcXGV0YX1eey0xfVxcY2lyYyBkIl0sWzksOCwidV4qIiwwLHsic2hvcnRlbiI6eyJzb3VyY2UiOjIwLCJ0YXJnZXQiOjIwfSwic3R5bGUiOnsiYm9keSI6eyJuYW1lIjoiZG90dGVkIn19fV1d -->
<iframe class="quiver-embed" src="https://q.uiver.app/#q=WzAsNyxbMCwwLCIoTSxcXG9tZWdhKSJdLFsyLDAsIihOLFxcZXRhKSJdLFswLDIsIlRNIl0sWzIsMiwiVE4iXSxbMCw0LCJDXlxcaW5mdHkoTikiXSxbMCw2LCJcXG1hdGhmcmFre1h9XiooTikiXSxbMiw2LCJcXG1hdGhmcmFre1h9KE4pIl0sWzAsMSwidSJdLFswLDIsInVeKlhfSCIsMl0sWzEsMywiWF9IIl0sWzMsMiwiZHVeey0xfSJdLFs0LDUsImQiLDJdLFs1LDYsIi1cXGhhdHtcXGV0YX0iLDJdLFs0LDYsIi1cXGhhdHtcXGV0YX1eey0xfVxcY2lyYyBkIl0sWzksOCwidV4qIiwwLHsic2hvcnRlbiI6eyJzb3VyY2UiOjIwLCJ0YXJnZXQiOjIwfSwic3R5bGUiOnsiYm9keSI6eyJuYW1lIjoiZG90dGVkIn19fV1d&embed" width="487" height="944" style="border-radius: 8px; border: none;"></iframe>

## Hamiltonian Vector Fields
Let $K\in C^\infty(N)$ be a smooth function, it defines a *unique* vector field, called the *Hamiltonian Vector Field* associated with $K$, denoted by $X_K\in\mathfrak{X}(N)$ through

$$
\eta(X_K(x), a) = -dK(x)(a),\quad\forall x\in N,\: a\in T_x N
$$

*Remember the negative sign*.

*Remark*: Uniqueness comes from Riesz map induced by the non-singular billinear form on the vector space $T_xN$, $\eta_x: T_xN\times T_xN\to \real$. Smoothness of the vector field comes a certain bundle isomorphism argument. There are two actions associated with the symbol $\hat{\eta}$, we can view it as the pointwise Riesz map


-  Any non-singular smooth covariant $2$-tensor field on $N$ induces a natural bundle isomorphism between $TN$ and $T^*N$.

    For any $x\in N$, $v_x\in T_xN$, for any $a\in T_xN$, 

    $$\hat{\eta}_x: T_xN\to T_x^* N,\quad v\mapsto v_x\lrcorner \eta_x\in T_x^* N$$

    simply 'takes the transpose' with respect to $\eta_x$, so 
    
    $$(v_x\lrcorner\eta_x)(a) = \eta_x(v_x, a)$$

    It is clear $\hat{\eta}$ defines a smooth bundle isomorphism, we now define the second action,

    $$
    \hat{\eta}:\mathfrak{X}(N)\to\mathfrak{X}^*(N),\quad \hat{\eta}(X)(Y) = \eta(X,Y)\:\forall X,Y\in\mathfrak{X}(N)
    $$

    This is justified by the following theorem. 

    *(Lee) Prop 10.26*: Suppose $E$ and $E'$ are smooth vector bundles over a smooth manifold $M$ with or without boundary, and $F: E\to E'$ is a bijective smooth bundle homomorphism over $M$, then $F$ is a smooth bundle isomorphism.

    *(Lee) Prop 10.29*: Smooth bundle homomorphisms (resp. isomorphisms) send smooth sections to smooth sections.

## Naturality of HVF Pullbacks 
Let $(M,\omega)$ and $(N,\eta)$ be symplectic manifolds of dimension $2n$, and $u: M\to N$ is a symplectic diffeomorphism. We claim the following

- $H\in C^\infty(N)$ defines a HVF on $N$, denoted by $X_H$. Let $u^* $ and $\hat{\omega}$, $\hat{\eta}$ be defined as above, and $K = u^* H = H\circ u\in C^\infty(M)$. Then,

    $$
    X_K = u^* {X_H},\quad\text{or}\quad -\hat{\omega}^{-1}\circ u^* = u^*\circ (-\hat{\eta}^{-1})
    $$

    this can be represented in the following commutative diagram

<!-- https://q.uiver.app/#q=WzAsNixbMCwwLCJDXlxcaW5mdHkoTikiXSxbMCwyLCJcXG1hdGhmcmFre1h9XiooTikiXSxbMiwyLCJcXG1hdGhmcmFre1h9KE4pIl0sWzYsMCwiQ15cXGluZnR5KE0pIl0sWzYsMiwiXFxtYXRoZnJha3tYfV4qKE0pIl0sWzQsMiwiXFxtYXRoZnJha3tYfShNKSJdLFswLDEsImQiLDJdLFsxLDIsIi1cXGhhdHtcXGV0YX1eey0xfSIsMl0sWzAsMiwiLVxcaGF0e1xcZXRhfV57LTF9XFxjaXJjIGQiLDFdLFswLDMsInVeKiJdLFs0LDUsIi1cXGhhdHtcXG9tZWdhfV57LTF9Il0sWzMsNCwiZCJdLFszLDUsIi1cXGhhdHtcXG9tZWdhfV57LTF9XFxjaXJjIGQiLDFdLFsyLDUsInVeKiIsMCx7InN0eWxlIjp7InRhaWwiOnsibmFtZSI6Im1vbm8ifX19XV0= -->
<iframe class="quiver-embed" src="https://q.uiver.app/#q=WzAsNixbMCwwLCJDXlxcaW5mdHkoTikiXSxbMCwyLCJcXG1hdGhmcmFre1h9XiooTikiXSxbMiwyLCJcXG1hdGhmcmFre1h9KE4pIl0sWzYsMCwiQ15cXGluZnR5KE0pIl0sWzYsMiwiXFxtYXRoZnJha3tYfV4qKE0pIl0sWzQsMiwiXFxtYXRoZnJha3tYfShNKSJdLFswLDEsImQiLDJdLFsxLDIsIi1cXGhhdHtcXGV0YX1eey0xfSIsMl0sWzAsMiwiLVxcaGF0e1xcZXRhfV57LTF9XFxjaXJjIGQiLDFdLFswLDMsInVeKiJdLFs0LDUsIi1cXGhhdHtcXG9tZWdhfV57LTF9Il0sWzMsNCwiZCJdLFszLDUsIi1cXGhhdHtcXG9tZWdhfV57LTF9XFxjaXJjIGQiLDFdLFsyLDUsInVeKiIsMCx7InN0eWxlIjp7InRhaWwiOnsibmFtZSI6Im1vbm8ifX19XV0=&embed" width="800" height="400" style="border-radius: 8px; border: none;"></iframe>

    

- Furthermore, if $\theta: \mathcal{O}\to N$, $\varphi: \mathcal{P}\to M$ denote the flows of $X_H$ and $X_K$, they are related by the equation

    $$
    \theta^t\circ u = u\circ \varphi^t
    $$

    for every $t\in\real$ where any side is defined.

### Proof of Diagram
It suffices to show $-\hat{\omega}^{-1}\circ u^* = u^*\circ (-\hat{\eta}^{-1})$, and by linearity we can remove the negative signs.

$$
\hat{\omega}^{-1}\circ u^* = u^* \circ \hat{\eta}^{-1}
$$

Fix $A\in \mathfrak{X}^*(N)$, and $B\in\mathfrak{X}(N)$ be the unique vector field such that $B\lrcorner\eta = A$. The right hand side becomes 

$$
(u^*\circ \hat{\eta}^{-1})(A) = u^*(B)\in \mathfrak{X}(M)
$$

Denote the left hand side by $X\in\mathfrak{X}(M)$, where $X\lrcorner\omega = u^* (A)$ by definition. We will show the two vector fields are equal, by demonstrating equality as derivations at each tangent space of $M$. Indeed, fix $p\in M$ and $Y_p\in T_pM$. By non-singularity of $\omega_p$, $X_p$ is the unique tangent vector with

$$
\omega(X_p, Y_p)=u^*(A)_p(Y_p) = A_{u(p)}(du_p(Y_p))
$$

Write $\omega = u^* \eta$, and using $B\lrcorner\eta = A$, but restricted onto the tangent space $T_{u(p)}N$, 

$$
\eta_{u(p)}(du_p(X_p), du_p(Y_p))= u^* \eta(X_p,Y_p) = \eta_{u(p)}(B_{u(p)}, du_p(Y_p))
$$

Since $du_p$ is invertible, and $\eta$ is non-singular pointwise, this implies $du_p(X_p) = B_{u(p)}$. Therefore 

$$
(u^*\circ \hat{\eta}^{-1})(A)_p=(u^* B)(p)=(du_p)^{-1}(B\circ u)(p) = X(p) =(\hat{\omega}^{-1}\circ u^*)(A)_p
$$

Since $p$ and $A$ are arbitrary, the proof is complete.

<!-- https://q.uiver.app/#q=WzAsMTMsWzIsNiwiVE4iXSxbMiw4LCJOIl0sWzYsNiwiVE0iXSxbNiw4LCJNIl0sWzAsMywiXFxtYXRoZnJha3tYfV4qKE4pIl0sWzgsMywiXFxtYXRoZnJha3tYfV4qKE0pIl0sWzAsNiwiVF4qTiJdLFs4LDYsIlReKk0iXSxbMiwzLCJcXG1hdGhmcmFre1h9KE4pIl0sWzYsMywiXFxtYXRoZnJha3tYfShNKSJdLFs2LDAsIkNeXFxpbmZ0eShNKSJdLFsyLDAsIkNeXFxpbmZ0eShOKSJdLFs0LDNdLFswLDIsInVeKiIsMV0sWzMsMSwidSJdLFswLDEsIlxccGlfTiIsMV0sWzIsMywiXFxwaV9NIiwxXSxbMCw2LCItXFxoYXR7XFxldGF9IiwxXSxbMiw3LCItXFxoYXR7XFxvbWVnYX0iLDFdLFs4LDksIlhfSFxcbWFwc3RvIChkdV57LTF9XFxjaXJjIFhfSFxcY2lyYyB1KSIsMCx7Im9mZnNldCI6LTF9XSxbNCw4LCItXFxoYXR7XFxldGF9Il0sWzksNSwiLVxcaGF0e1xcb21lZ2F9IiwwLHsic3R5bGUiOnsidGFpbCI6eyJuYW1lIjoiYXJyb3doZWFkIn0sImhlYWQiOnsibmFtZSI6Im5vbmUifX19XSxbNCw1LCJ1XioiLDIseyJjdXJ2ZSI6LTUsInN0eWxlIjp7ImJvZHkiOnsibmFtZSI6ImRvdHRlZCJ9LCJoZWFkIjp7Im5hbWUiOiJlcGkifX19XSxbMTEsMTAsInVeKiIsMl0sWzEwLDUsImQiXSxbMTEsNCwiZCIsMl0sWzExLDgsIi1cXGhhdHtcXGV0YX1eey0xfVxcY2lyYyBkIiwxXSxbMTAsOSwiLVxcaGF0e1xcb21lZ2F9XnstMX1cXGNpcmMgZCIsMV0sWzEzLDEyLCJcXG9wZXJhdG9ybmFtZXtIb219KFxcb3BlcmF0b3JuYW1le1ZCfV9OLFxcb3BlcmF0b3JuYW1le1ZCfV9NKSIsMix7ImxldmVsIjoxLCJzdHlsZSI6eyJib2R5Ijp7Im5hbWUiOiJkb3R0ZWQifSwiaGVhZCI6eyJuYW1lIjoiZXBpIn19fV1d -->
<iframe class="quiver-embed" src="https://q.uiver.app/#q=WzAsMTMsWzIsNiwiVE4iXSxbMiw4LCJOIl0sWzYsNiwiVE0iXSxbNiw4LCJNIl0sWzAsMywiXFxtYXRoZnJha3tYfV4qKE4pIl0sWzgsMywiXFxtYXRoZnJha3tYfV4qKE0pIl0sWzAsNiwiVF4qTiJdLFs4LDYsIlReKk0iXSxbMiwzLCJcXG1hdGhmcmFre1h9KE4pIl0sWzYsMywiXFxtYXRoZnJha3tYfShNKSJdLFs2LDAsIkNeXFxpbmZ0eShNKSJdLFsyLDAsIkNeXFxpbmZ0eShOKSJdLFs0LDNdLFswLDIsInVeKiIsMV0sWzMsMSwidSJdLFswLDEsIlxccGlfTiIsMV0sWzIsMywiXFxwaV9NIiwxXSxbMCw2LCItXFxoYXR7XFxldGF9IiwxXSxbMiw3LCItXFxoYXR7XFxvbWVnYX0iLDFdLFs4LDksIlhfSFxcbWFwc3RvIChkdV57LTF9XFxjaXJjIFhfSFxcY2lyYyB1KSIsMCx7Im9mZnNldCI6LTF9XSxbNCw4LCItXFxoYXR7XFxldGF9Il0sWzksNSwiLVxcaGF0e1xcb21lZ2F9IiwwLHsic3R5bGUiOnsidGFpbCI6eyJuYW1lIjoiYXJyb3doZWFkIn0sImhlYWQiOnsibmFtZSI6Im5vbmUifX19XSxbNCw1LCJ1XioiLDIseyJjdXJ2ZSI6LTUsInN0eWxlIjp7ImJvZHkiOnsibmFtZSI6ImRvdHRlZCJ9LCJoZWFkIjp7Im5hbWUiOiJlcGkifX19XSxbMTEsMTAsInVeKiIsMl0sWzEwLDUsImQiXSxbMTEsNCwiZCIsMl0sWzExLDgsIi1cXGhhdHtcXGV0YX1eey0xfVxcY2lyYyBkIiwxXSxbMTAsOSwiLVxcaGF0e1xcb21lZ2F9XnstMX1cXGNpcmMgZCIsMV0sWzEzLDEyLCJcXG9wZXJhdG9ybmFtZXtIb219KFxcb3BlcmF0b3JuYW1le1ZCfV9OLFxcb3BlcmF0b3JuYW1le1ZCfV9NKSIsMix7ImxldmVsIjoxLCJzdHlsZSI6eyJib2R5Ijp7Im5hbWUiOiJkb3R0ZWQifSwiaGVhZCI6eyJuYW1lIjoiZXBpIn19fV1d&embed" width="800" height="800" style="border-radius: 8px; border: none;"></iframe>

---

#### Proof for integral flows 
Since $X_k = u^* X_H$, we unbox the definitions, and see that

$$
X_K = (du)^{-1}\circ X_H\circ u\iff du\circ X_K = X_H\circ u
$$

Let $p\in M$, $q\in N$ be arbitrary, the above expression reads

$$
du_p\circ X_K(p) = X_H\circ u(p),\quad\text{and}\quad (du^{-1})_q\circ X_H = X_K\circ u^{-1}(q)
$$

Therefore $X_K$ and $X_H$ are related by $u$, $u^{-1}$ Lee Prop 9.6 tells us their integral curves are related by $u$, $u^{-1}$. More precisely, if $f(t), g(t)$ are integral curves of $X_K$ and $X_H$, then $u\circ f(t)$, $u^{-1}\circ g(t)$ are integral curves of $X_H$ and $X_K$ respectively.


![Prop 9.6]({{ site.baseurl }}{% link /images/lee-prop-9-6.png %})


# Darboux's Theorem