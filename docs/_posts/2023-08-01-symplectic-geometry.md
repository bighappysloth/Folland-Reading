---
layout: article
title: Part 1 - Symplectic Geometry
date: 2023-08-01 14:37
category: 
tags: ['symplectic']
---

# Preliminaries

See the document 'Symplectic Geometry and Hamiltonian Systems' for a dicussion on Metric Vector Spaces, algebraic construcitons, etc. 

## Vector space isomorphsims
Let $V$ be a normed vector space over $\real$. If $f\in V^*$, and $x\in V$, we denote

$$
f(x) = \langle f,x\rangle_{(V^*, V)}
$$

If $V=\real^{k}$, and $f$ has simple matrix representation $A\in\real^{1\times k}$, identifying $x$ with its matrix representation,

$$
\langle f,x\rangle = Ax
$$


<div class="remark-box" markdown=1 name="">
$\real^{k}$ is also an inner product space with the non-singular billinear form $\langle\cdot,\cdot\rangle_{\real^k}$. By Riesz isomorphism, every covector $a\in (\real^{k})^*$ corresponds to a unique vector $a'\in\real^k$ that realizes $a$ through the inner product,


$$
\langle a,x\rangle_{( (\real^k)^*, \real^k)} = a(x) = \langle a', x\rangle_{\real^k}
$$


</div>




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
Let $M$ be a smooth manifold equipped with a smooth $2$-form $\omega$. If $X\in\mathfrak{X}(M)$ is a vector field, then it *defines* a covector field through interior multiplication  $X\lrcorner\omega\in\mathfrak{X}^*(M)$

$$
(X\lrcorner\omega)_p = X_p\lrcorner \omega_p\in T_p^* M
$$

</div>

<div class="definition-box" markdown=1 name="Interior Multiplication of $k$-forms on Manifolds">
If $\omega\in\Omega^k(M)$ is a $k$-form, and $X\in\mathfrak{X}(M)$. Interior multiplication by $X$ realized through the map 

$$\iota_X: \Omega^k(M)\to\Omega^{k-1}(M)$$

is linear over $C^\infty(M)$, and therefore corresponds to a smooth bundle homomorphism.
</div>

<div class="definition-box" markdown=1 name="Tangent-cotangent vector isomorphism on $\real^k$">
Let $f\in C^\infty(\real^k,\real)\Isomor{can}\Omega^0(\real^k)$. Denote the standard inner product on $\real^k$ by $E(\cdot,\cdot)$. $df$ is a covector field on $\real^k$.

The *gradient of $f$* is a vector field on $\real^k$. Defined by $\operatorname{grad}f = \nabla f = \hat{E}^{-1}(df)$ the Riesz map of $E$.
</div>


## Symplectic Manifolds
<div class="definition-box" markdown=1 name="Symplectic manifold">
A **symplectic manifold** is a real-smooth manifold of dimension $2n$ with a smooth, non-degenerate closed $2$-form.

Non degeneracy refers to: $\forall p\in M,\forall v\in T_pM, v\neq 0$, then the functional $v\lrcorner\omega = \omega(v,\cdot)$ is non-singular. For closed forms see [here]({{ site.baseurl }}/{% post_url 2023-08-03-derham-cohomology %}).
</div>


<div class="definition-box" markdown=1 name="Standard Symplectic Manifold $(\real^{2n},\omega_0)$">
Let $n$ be a positive integer, and $\omega_0$ be the standard symplectic form on the real vector space $\real^{2n}$, which is defined by the matrix 


$$
J = \begin{bmatrix} 0 & I_n \\ -I_n & 0\end{bmatrix}\quad\text{such that}\quad
\omega_0(u,v) = \langle Ju, v\rangle_{\real^{2n}}
$$

</div>

<div class="theorem-box" markdown=1 name="Properties of $\omega_0$">
- We can write the $\omega_0$ in terms of the standard inner product on $\real^{2n}$ as a vector space (or the standard Euclidean metric on $(\real^{2n}, \langle\cdot,\cdot\rangle)$ as a Riemannian Manifold).

    $$
    \omega_0(u,v) = \langle Ju,v\rangle,\quad\text{and}\quad \omega_0(u,Jv) = \langle u,v\rangle\quad\forall u,v\in\real^{2n}
    $$

- $\omega_0$ is an exact $2$-form

    $$
    \omega_0 = \sum_{j=1}^n dy_j\wedge dx_j = d\lambda
    $$

    where $$\lambda = \sum_{j=1}^n y_j dx_j$$. We verify this by computing the exterior derivative of $\lambda$,
    
    $$
    d\lambda = \sum_{j=1}^n d(y_j dx_j) = \sum_{j=1}^N dy_j\wedge dx_j=\omega_0
    $$

- $J$ is skew symmetric, and $J^T = -J = J^{-1}$.

- For every $x,y\in\real^{2n}$,

$$
\langle -Jx,y\rangle_{\real^{2n}} = \sum_{i\leq n}\det\biggl(\begin{bmatrix}x_j & y_j \\ x_{n+j} & y_{n+j}\end{bmatrix}\biggr) = -\omega_0(x,y)
$$

</div>

<!-- <div class="definition-box" markdown=1 name="Symplectic Diffeomorphism on $(\real^{2n},\omega_0)$">
A diffeomorphism $\varphi\in\mathcal{D}(\real^{2n})$ is **symplectic** if it preserves the symplectic form $\omega_0$, that is

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

</div> -->


## Symplectic Diffeomorphisms on $(M,\omega)$
In this section, we recall some facts about cotangent fields. $(M,\omega)$ and $(N,\eta)$ will denote symplectic manifolds of dimension $2n$, and $u: C^\infty(M,N)$ will be a diffeomorphism.

<div class="definition-box" markdown=1 name="Pullback of symplectic form">
$u^*$ denotes the tensor field pullback through $u$, by precomposing $\eta$ with $u$ and $du$ in its arguments.

$$
(u^*\eta)_p(v_1,v_2) = \eta_{u(p)}\biggl(du_p(v_1),\: du_p(v_2)\biggr) = \omega_p(v_1,v_2)
$$

</div>

<div class="definition-box" markdown=1 name="Symplecitic Diffeomorphism">
A diffeomorphism $u$ is symplectic if the pullback of $\eta$ is equal to $\omega$. That is, $\omega$ and $\eta$ are *$u$-related*.

$$
u^*\eta = \omega
$$

</div>

<div class="definition-box" markdown=1 name="Pullback of smooth functions">
We define the pullback of a $0$-form (which is also a tensor),

$$
u^*: C^\infty(N)\to C^\infty(M),\quad (u^*f)(p) = (f\circ u)(p),\:\forall f\in C^\infty(N)
$$

</div>

<div class="definition-box" markdown=1 name="Pullback of vector fields">
Let $Y$ be a vector field on $N$, then $u^* Y$ is a vector field on $M$, such that for every $p\in M$, we define $$u^*Y (p) = ((du^{-1})_{u(p)}) ( Y_{u(p)} )$$, or

$$
( u^*Y ) = \biggl((du)^{-1}\circ Y\circ u\biggr)
$$

Here, $u$ is required to be a diffeomorphism for $(du)^{-1}$ to be defined.

<!-- https://q.uiver.app/#q=WzAsNyxbMCwwLCIoTSxcXG9tZWdhKSJdLFsyLDAsIihOLFxcZXRhKSJdLFswLDIsIlRNIl0sWzIsMiwiVE4iXSxbMCw0LCJDXlxcaW5mdHkoTikiXSxbMCw2LCJcXG1hdGhmcmFre1h9XiooTikiXSxbMiw2LCJcXG1hdGhmcmFre1h9KE4pIl0sWzAsMSwidSJdLFswLDIsInVeKlhfSCIsMl0sWzEsMywiWF9IIl0sWzMsMiwiZHVeey0xfSJdLFs0LDUsImQiLDJdLFs1LDYsIi1cXGhhdHtcXGV0YX0iLDJdLFs0LDYsIi1cXGhhdHtcXGV0YX1eey0xfVxcY2lyYyBkIl0sWzksOCwidV4qIiwwLHsic2hvcnRlbiI6eyJzb3VyY2UiOjIwLCJ0YXJnZXQiOjIwfSwic3R5bGUiOnsiYm9keSI6eyJuYW1lIjoiZG90dGVkIn19fV1d -->
<iframe class="quiver-embed" src="https://q.uiver.app/#q=WzAsNyxbMCwwLCIoTSxcXG9tZWdhKSJdLFsyLDAsIihOLFxcZXRhKSJdLFswLDIsIlRNIl0sWzIsMiwiVE4iXSxbMCw0LCJDXlxcaW5mdHkoTikiXSxbMCw2LCJcXG1hdGhmcmFre1h9XiooTikiXSxbMiw2LCJcXG1hdGhmcmFre1h9KE4pIl0sWzAsMSwidSJdLFswLDIsInVeKlhfSCIsMl0sWzEsMywiWF9IIl0sWzMsMiwiZHVeey0xfSJdLFs0LDUsImQiLDJdLFs1LDYsIi1cXGhhdHtcXGV0YX0iLDJdLFs0LDYsIi1cXGhhdHtcXGV0YX1eey0xfVxcY2lyYyBkIl0sWzksOCwidV4qIiwwLHsic2hvcnRlbiI6eyJzb3VyY2UiOjIwLCJ0YXJnZXQiOjIwfSwic3R5bGUiOnsiYm9keSI6eyJuYW1lIjoiZG90dGVkIn19fV1d&embed" width="400" height="400" style="border-radius: 8px; border: none;"></iframe>
[Diagram](https://q.uiver.app/#q=WzAsNyxbMCwwLCIoTSxcXG9tZWdhKSJdLFsyLDAsIihOLFxcZXRhKSJdLFswLDIsIlRNIl0sWzIsMiwiVE4iXSxbMCw0LCJDXlxcaW5mdHkoTikiXSxbMCw2LCJcXG1hdGhmcmFre1h9XiooTikiXSxbMiw2LCJcXG1hdGhmcmFre1h9KE4pIl0sWzAsMSwidSJdLFswLDIsInVeKlhfSCIsMl0sWzEsMywiWF9IIl0sWzMsMiwiZHVeey0xfSJdLFs0LDUsImQiLDJdLFs1LDYsIi1cXGhhdHtcXGV0YX0iLDJdLFs0LDYsIi1cXGhhdHtcXGV0YX1eey0xfVxcY2lyYyBkIl0sWzksOCwidV4qIiwwLHsic2hvcnRlbiI6eyJzb3VyY2UiOjIwLCJ0YXJnZXQiOjIwfSwic3R5bGUiOnsiYm9keSI6eyJuYW1lIjoiZG90dGVkIn19fV1d)

</div>




## Hamiltonian Vector Fields

<div class="definition-box" markdown=1 name="Hamiltonian VF on $(N,\eta)$">
Let $K\in C^\infty(N)$ be a smooth function, it defines a *unique* vector field, called the *Hamiltonian Vector Field* associated with $K$, denoted by $X_K\in\mathfrak{X}(N)$ through

$$
\eta(X_K(x), a) = -dK(x)(a),\quad\forall x\in N,\: a\in T_x N
$$

</div>
<div class="remark-box" markdown=1 name="">
Uniqueness comes from Riesz map induced by the non-singular billinear form on the vector space $T_xN$, $\eta_x: T_xN\times T_xN\to \real$. Smoothness of the vector field comes a certain bundle isomorphism argument. There are two actions associated with the symbol $\hat{\eta}$, we can view it as the pointwise Riesz map, or a bundle isomorphism - which we will explain below.
</div>

<div class="theorem-box" markdown=1 name="Natural bundle isomorphism induced by non-singular billinear form">
Any non-singular smooth covariant $2$-tensor field on $N$ induces a natural bundle isomorphism between $TN$ and $T^*N$.

For any $x\in N$, $v_x\in T_xN$, for any $a\in T_xN$, 

$$\hat{\eta}_x: T_xN\to T_x^* N,\quad v\mapsto v_x\lrcorner \eta_x\in T_x^* N$$

simply 'takes the transpose' with respect to $\eta_x$, so 

$$(v_x\lrcorner\eta_x)(a) = \eta_x(v_x, a)$$

It is clear $\hat{\eta}$ defines a smooth bundle isomorphism, we now define the second action associated to $\eta$ which **is an isomorphism between vector fields to covector fields**

$$
\hat{\eta}:\mathfrak{X}(N)\to\mathfrak{X}^*(N),\quad X\lrcorner\eta=\hat{\eta}(X)(Y) = \eta(X,Y)\quad\forall X,Y\in\mathfrak{X}(N)
$$

Furthermore, if $A$ is a covector field, **it defines a unique vector field** by $\hat{\eta}^{-1}:\mathfrak{X}^*(N)\to\mathfrak{X}(N)$, with

$$
\hat{\eta}^{-1}\mathfrak{X}^*(N)\to\mathfrak{X}(N)
$$

If $B = \hat{\eta}^{-1}(A)$, it is the unique VF that satisfies 

$$
\eta(B,X)=A(X)\quad\forall X\in\mathfrak{X}(N)
$$

The "existence and uniqueness" of the isomorphism on sections is justified by

- *(Lee) Prop 10.26*: Suppose $E$ and $E'$ are smooth vector bundles over a smooth manifold $M$ with or without boundary, and $F: E\to E'$ is a bijective smooth bundle homomorphism over $M$, then $F$ is a smooth bundle isomorphism.

- *(Lee) Prop 10.29*: Smooth bundle homomorphisms (resp. isomorphisms) send smooth sections to smooth sections.
</div>
<div class="remark-box" markdown=1 name="Tangent, cotangent bundle isomorphsim in infinite dimensions">
We will work in infinite dimensional manifolds, specifically Hilbert manifolds in the next section. If $E$ is a Hilbert space, that is also a Hilbert manifold with the global chart $(E, \operatorname{can})$. The manifold structure we will put on $E$ is the $C^1$ structure. By Proposition 6.1 of Lang:


![Lang 6-1]({{ site.baseurl }}{% link /images/lang-6-1.png %})

induces a natural bundle isomorphism.
</div>

With this, if $(M,\omega)$ is a **symplectic of Riemannian/Hilbert manifold**, we **define** the HVF associated to a smooth function $F\in C^\infty(M)$ by the unique VF

$$
X_F = -\hat{\omega}^{-1}(dF)
$$

In these notes, we will mostly work with the standard symplectic structure. The following will be useful.
<div class="definition-box" markdown=1 name="Hamiltonian Vector Fields on $\real^{2n}$">
Let $(\real^{2n},\omega_0)$ be the standard symplectic structure. If $H\in C^\infty(\real^{2n})$, the **Hamiltonian Vector Field associated to $H$** is defined

$$
X_H = -\hat{\omega}_0^{-1}(dH)
$$

Identifying $\mathfrak{X}(\real^{2n})\Isomor{L}C^\infty(\real^{2n},\real^{2n})$ (because $\real^{2n}$ is parallelizable). For every $x\in\real^{2n}$, and $a\in T_x\real^{2n}\Isomor{L}\real^{2n}$,

$$
\begin{align}
\omega_0(X_H(x), a) &= -dH(x)(a)\\[2ex]
\langle JX_H(x),a\rangle_{\real^{2n}} &= \langle -dH(x), a\rangle_{((\real^{2n})^*, \real^{2n})}\\[2ex]
&= \langle (-dH(x))^T,a\rangle_{\real^{2n}}\\[2ex]
&=\langle -\nabla H(x), a\rangle_{\real^{2n}}
\end{align}
$$

This holds for an arbitrary $a\in\real^{2n}$, so $JX_H(x) = -\nabla H(x)\implies X_H(x) = J\nabla H(x)$.
</div>

<div class="theorem-box" markdown=1 name="Independence of Hamiltonian defining hypersurfaces">
Let $S$ is a (compact) regular hypersurface on a symplectic manifold $(M,\omega)$ defined by $F,H\in C^\infty(M,\real)$,

$$
S = \{F=c\} = \{H=c'\},\quad\text{and}\quad dF\vert_S,\: dH\vert_S\neq 0
$$

We claim there exists a **smooth, nowhere vanishing function** $\rho: S\to\real$ (take) such that

- $dF(x) = \rho(x)dH(x)$ for all $x\in S$,
- If $\varphi^s(x)$ and $\theta^t(x)$ are flows of the HVFs $X_F$ and $X_H$ on $S$. The following IVP provides **a unique solution that relates the two flows by reparametrization**. $\dfrac{dt}{ds}=\rho(\varphi^s(x)),\: t(0)=0$ So that $\varphi^s(x) = \theta^{\alpha(s,x)}(x)$ for some smooth, nowhere vashing function $\alpha(\cdot,x)$
- **$X_F$ and $X_H$ define the same periodic orbits on $S$**, if any.

</div>


<div class="proof-box" markdown=1 proof-name="">
Both $F$ and $H$ are global definining functions for the embedded submanifold $S$, if $p\in S$ is arbitrary, the **exterior tangent space** of $p$ coincides precisely with the $\ker{dF_p} = \ker{dH_p}$ (Lee 5.38, 5.40).

$$
\ker{dH_p} = T^{ext}_p S = \ker{dF_p}
$$

Using the canonical identifications 

- $T_{F(p)}\real \cong\real\cong T_{H(p)}$,
- $T^{ext}_p S\cong\real^{2n}$,
- $T_p M\cong\real^{2n}$,

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

We now search for a parametrization, or a function $t(s,x)$ such that the integral curves above agree,

$$
\psi^s(x) = \varphi^t(x),\quad \forall x\in S,\: t(0,x)=0
$$

We differentiate both sides and use the chain rule, 

$$
X_F(\psi^s(x)) = X_H(\varphi^t(x))\dfrac{dt}{ds}\biggr\vert_s\implies X_F = \rho X_H = X_H\dfrac{dt}{ds}\biggr\vert_s
$$

We come to $$\dfrac{dt}{ds} = \rho(\varphi^t(x)) =\rho(\psi^s(x))$$, or $$t(s,x) = \int_0^s \rho(\varphi_x(u))du$$. The latter is strictly monotonic, and the constant (resp. non-constant) periodic solutions of $X_F$ correspond precisely to those of $X_H$.
</div>


<div class="theorem-box" markdown=1 name="Naturality of HVF Pullbacks ">
Let $(M,\omega)$ and $(N,\eta)$ be symplectic manifolds of dimension $2n$, and $u: M\to N$ is a symplectic diffeomorphism. We claim the following

- $H\in C^\infty(N)$ defines a HVF on $N$, denoted by $X_H$. Let $u^* $ and $\hat{\omega}$, $\hat{\eta}$ be defined as above, and $K = u^* H = H\circ u\in C^\infty(M)$. Then,

    $$
    X_K = u^* {X_H},\quad\text{or}\quad -\hat{\omega}^{-1}\circ u^* = u^*\circ (-\hat{\eta}^{-1})
    $$

    this can be represented in the following commutative diagram

    <!-- https://q.uiver.app/#q=WzAsNixbMCwwLCJDXlxcaW5mdHkoTikiXSxbMCwyLCJcXG1hdGhmcmFre1h9XiooTikiXSxbMiwyLCJcXG1hdGhmcmFre1h9KE4pIl0sWzYsMCwiQ15cXGluZnR5KE0pIl0sWzYsMiwiXFxtYXRoZnJha3tYfV4qKE0pIl0sWzQsMiwiXFxtYXRoZnJha3tYfShNKSJdLFswLDEsImQiLDJdLFsxLDIsIi1cXGhhdHtcXGV0YX1eey0xfSIsMl0sWzAsMiwiLVxcaGF0e1xcZXRhfV57LTF9XFxjaXJjIGQiLDFdLFswLDMsInVeKiJdLFs0LDUsIi1cXGhhdHtcXG9tZWdhfV57LTF9Il0sWzMsNCwiZCJdLFszLDUsIi1cXGhhdHtcXG9tZWdhfV57LTF9XFxjaXJjIGQiLDFdLFsyLDUsInVeKiIsMCx7InN0eWxlIjp7InRhaWwiOnsibmFtZSI6Im1vbm8ifX19XV0= -->
    <iframe class="quiver-embed" src="https://q.uiver.app/#q=WzAsNixbMCwwLCJDXlxcaW5mdHkoTikiXSxbMCwyLCJcXG1hdGhmcmFre1h9XiooTikiXSxbMiwyLCJcXG1hdGhmcmFre1h9KE4pIl0sWzYsMCwiQ15cXGluZnR5KE0pIl0sWzYsMiwiXFxtYXRoZnJha3tYfV4qKE0pIl0sWzQsMiwiXFxtYXRoZnJha3tYfShNKSJdLFswLDEsImQiLDJdLFsxLDIsIi1cXGhhdHtcXGV0YX1eey0xfSIsMl0sWzAsMiwiLVxcaGF0e1xcZXRhfV57LTF9XFxjaXJjIGQiLDFdLFswLDMsInVeKiJdLFs0LDUsIi1cXGhhdHtcXG9tZWdhfV57LTF9Il0sWzMsNCwiZCJdLFszLDUsIi1cXGhhdHtcXG9tZWdhfV57LTF9XFxjaXJjIGQiLDFdLFsyLDUsInVeKiIsMCx7InN0eWxlIjp7InRhaWwiOnsibmFtZSI6Im1vbm8ifX19XV0=&embed" width="400" height="200" style="border-radius: 8px; border: none;"></iframe>

    

- Furthermore, if $\theta: \mathcal{O}\to N$, $\varphi: \mathcal{P}\to M$ denote the flows of $X_H$ and $X_K$, they are related by the equation

    $$
    \theta^t\circ u = u\circ \varphi^t
    $$

    for every $t\in\real$ where any side is defined.
</div>
<div class="proof-box" markdown=1 proof-name="Proof of diagram">
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
<iframe class="quiver-embed" src="https://q.uiver.app/#q=WzAsMTMsWzIsNiwiVE4iXSxbMiw4LCJOIl0sWzYsNiwiVE0iXSxbNiw4LCJNIl0sWzAsMywiXFxtYXRoZnJha3tYfV4qKE4pIl0sWzgsMywiXFxtYXRoZnJha3tYfV4qKE0pIl0sWzAsNiwiVF4qTiJdLFs4LDYsIlReKk0iXSxbMiwzLCJcXG1hdGhmcmFre1h9KE4pIl0sWzYsMywiXFxtYXRoZnJha3tYfShNKSJdLFs2LDAsIkNeXFxpbmZ0eShNKSJdLFsyLDAsIkNeXFxpbmZ0eShOKSJdLFs0LDNdLFswLDIsInVeKiIsMV0sWzMsMSwidSJdLFswLDEsIlxccGlfTiIsMV0sWzIsMywiXFxwaV9NIiwxXSxbMCw2LCItXFxoYXR7XFxldGF9IiwxXSxbMiw3LCItXFxoYXR7XFxvbWVnYX0iLDFdLFs4LDksIlhfSFxcbWFwc3RvIChkdV57LTF9XFxjaXJjIFhfSFxcY2lyYyB1KSIsMCx7Im9mZnNldCI6LTF9XSxbNCw4LCItXFxoYXR7XFxldGF9Il0sWzksNSwiLVxcaGF0e1xcb21lZ2F9IiwwLHsic3R5bGUiOnsidGFpbCI6eyJuYW1lIjoiYXJyb3doZWFkIn0sImhlYWQiOnsibmFtZSI6Im5vbmUifX19XSxbNCw1LCJ1XioiLDIseyJjdXJ2ZSI6LTUsInN0eWxlIjp7ImJvZHkiOnsibmFtZSI6ImRvdHRlZCJ9LCJoZWFkIjp7Im5hbWUiOiJlcGkifX19XSxbMTEsMTAsInVeKiIsMl0sWzEwLDUsImQiXSxbMTEsNCwiZCIsMl0sWzExLDgsIi1cXGhhdHtcXGV0YX1eey0xfVxcY2lyYyBkIiwxXSxbMTAsOSwiLVxcaGF0e1xcb21lZ2F9XnstMX1cXGNpcmMgZCIsMV0sWzEzLDEyLCJcXG9wZXJhdG9ybmFtZXtIb219KFxcb3BlcmF0b3JuYW1le1ZCfV9OLFxcb3BlcmF0b3JuYW1le1ZCfV9NKSIsMix7ImxldmVsIjoxLCJzdHlsZSI6eyJib2R5Ijp7Im5hbWUiOiJkb3R0ZWQifSwiaGVhZCI6eyJuYW1lIjoiZXBpIn19fV1d&embed" width="400" height="400" style="border-radius: 8px; border: none;"></iframe>
</div>
<div class="proof-box" markdown=1 proof-name="Proof for integral flows">
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
</div>


## Symplectic Action on $\real^{2n}$: $A(\gamma) = \int_{\gamma}\lambda$

<div class="definition-box" markdown=1 name="Symplectic action">
Let $\gamma$ be a closed curve in $\real^{2n}$, we sometimes refer to closed curves as *closed characteristics*, we define the *symplectic action*, or *action* on $\gamma$ 

$$
    A(\gamma) =\int_{\gamma}\lambda\in\real
$$

</div>

<div class="theorem-box" markdown=1 name="Symplectic invariance of the action">
If $\varphi\in \operatorname{Sp}(n)$, then $A(\varphi\circ \gamma) = A(\gamma)$. 
</div>


First we need a lemma.


<div class="lemma-box" markdown=1>
The $1$-form $\lambda -\varphi^*\lambda$ is exact iff $\varphi$ is a symplectic diffeomorphism on $\real^{2n}$. 
</div>
<div class="proof-box" markdown=1>
Indeed, 

$$
d(\lambda-\varphi^* \lambda)=d\lambda - \varphi^* (d\lambda) = \omega_0-\omega_0=0
$$

since the exterior product commutes with tensor pullbacks (Lee 14.23d). So $\lambda-\varphi^* \lambda$ is a closed form. Poincare's Lemma, which states the $k$-th [de Rham cohomology group]({{ site.baseurl }}/{% post_url 2023-08-03-derham-cohomology %}), of a contractible domain is trivial for $k\geq 1$, therefore $\lambda-\varphi^* \lambda$ is exact.
</div>

<div class="proof-box" markdown=1 proof-name="Proof of Invariance">
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

</div>


<div class="proof-box" markdown=1 proof-name="Proof of symplectic invariance of $A$">
By Lee Prop 11.37, the line integral is invariant under *forward reparametrizations*. (More generally, the integral over forms is an invariant under the precomposition of orientation preserving diffeomorphisms). If $\gamma$ is a (not necessarily closed) curve on $M$, and $f$ is a diffeomorphism on $\real$ which is strictly increasing, then 

$$
\int_{\gamma}\lambda = \int_{\gamma\circ f}\lambda,\quad\forall\lambda\in\mathfrak{X}^*(M)
$$

With this, let $\gamma$ be reparametrized so that it has period $1$. We will prove the following formula

$$
A(\gamma) = \int_\gamma \lambda = 2^{-1}\int_0^1\biggl\langle -J\dot{\gamma},\:\gamma\biggr\rangle dt
$$


- Let $(x_1,\ldots,x_n,x_{n+1},\ldots x_{2n})$ be the standard coordinates on $\real^{2n}$, and $\gamma = (\gamma_1\,\ldots,\gamma_{2n})$. The left hand side becomes 

    $$
    A(\gamma) = \int_0^1\sum_{j=1}^n \gamma_{n+j}\dot{\gamma}_{j}dt
    $$

- Right hand side: examining the integrand using the Lemma below, 

    $$
    2^{-1}\biggl\langle -J\dot{\gamma},\: \gamma\biggr\rangle = 2^{-1}\sum_{j=1}^n \det\biggl(\begin{bmatrix} \dot{\gamma}_j & \gamma_j \\ \dot{\gamma}_{n+j} & \gamma{n+j} \end{bmatrix}\biggr) = 2^{-1}\sum_{j=1}^n \dot{\gamma}_{j}\gamma_{n+j} - \dot{\gamma}_{n+j}\gamma_{j} dt
    $$

- Integrating the right hand side, we obtain

    $$
    \int_0^1 2^{-1}\biggl\langle -J\dot{\gamma},\gamma\biggr\rangle dt = \int_0^1 2^{-1}\sum_{j=1}\dot{\gamma}_{j}\gamma_{n+j} - \dot{\gamma}_{n+j}\gamma_j dt
    $$

- Using the note below, 

    $$
    \int_0^1 2^{-1}\biggl\langle -J\dot{\gamma},\gamma\biggr\rangle dt = 2^{-1}\int_\gamma\lambda + (-1)2^{-1}\int_\gamma\lambda = \int_\gamma\lambda = A(\gamma)
    $$

</div>

### Proof for Formulas
<div class="lemma-box" markdown=1 name="Determinant formula for the action">
Let $x,y\in L^2(S^1)$, where $S^1$ denotes the $1$-torus. Define

$$
a(x,y) = 2^{-1}\int_0^1\langle-J\dot{x},y\rangle dt
$$

if $x = (x_1,\ldots x_{2n})$, and $y = (y_1,\ldots,y_{2n})$, the integrand becomes

$$
\langle -J\dot{x},y\rangle = \sum_{j=1}^n\operatorname{det}\biggl(\begin{bmatrix}\dot{x}_j & y_j\\ \dot{x}_{n+j} & y_{n+j}\end{bmatrix}\biggr)
$$

The whole integral becomes

$$
a(x,y) = 2^{-1}\sum_{j=1}^n\int_0^1 \operatorname{det}\biggl(\begin{bmatrix}\dot{x}_j & y_j\\ \dot{x}_{n+j} & y_{n+j}\end{bmatrix}\biggr) dt
$$

</div>



<div class="proof-box" markdown=1 proof-name="">
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

</div>

<div class="note-box" markdown=1 name="Integration by parts">

$$
\int_0^1 \sum_{j=1}^n \gamma_j\dot{\gamma}_{n+j} dt = (-1)\int_0^1\sum_{j=1}^n \gamma_{n+j}\dot{\gamma}_{j}dt
$$

Where $\gamma = (\gamma_1,\ldots,\gamma_{2n})$ is periodic. Indeed, by integration by parts. Recall $\int_X a\dot{b} = ab\vert_{\partial X} - \int_X \dot{a}b$,

$$
\text{LHS} = \underbrace{\sum_{j=1}^n\gamma_j \gamma_{n+j}\biggr\vert^1_0 }_{=0} - \int_0^1\sum_{j=1}^n\gamma_{n+j}\dot{\gamma}_{j}dt = \text{RHS}
$$

</div>

# Darboux's Theorem