---
layout: article
title: hamiltonian flows
date: 2023-08-01 14:37
category: 
author: 
tags: []
summary: 
---


# Computations
Let $$J = J_2 = \begin{bmatrix}0 & 1\\ -1 & 0\end{bmatrix}$$, let $(x_1, y_1)$ be the basis of $\real^2$. If $z = ax_1 + by_1$, then $Jz = bx_1 - ay_1$. More generally, let $$J = \begin{bmatrix} 0 & I_n\\ -I_n & 0\end{bmatrix}$$, and $(x_1,\ldots, x_n, y_1,\ldots, y_n)$ be a basis for $\real^{2n}$. 

$$
z = \sum_{j=1}^n a_jx_j + b_jy_j\quad\text{then}\quad Jz = \sum_{j=1}^n b_jx_j - a_jy_j
$$

Let $q(z)$ be a quadratic form in normal coordinates, so $0<r_1(q)\leq r_2(q)\leq\cdots\leq r_n(q)$, where

$$
q(z) = \sum_{j=1}^n \dfrac{x_j^2 + y_j^2}{r_j^2}
$$

for standard coordinates described above. We will calculate the induced Hamiltonian Vector Field of $q(z)$,

$$
\nabla\biggl(\dfrac{x_1^2 + y_1^2}{r_1^2}\biggr) = \biggl(\dfrac{2x_1}{r_1^2},\dfrac{2y_1}{r_1^2},\ldots,\biggr)^{\#}
$$

where # denotes the musical isomorphism. By linearity,

$$
\nabla q(z) = \sum_{j=1}^{n} \dfrac{2x_j}{r_j^2}\dfrac{\partial}{\partial x_j} + \dfrac{2y_j}{r_j^2}\dfrac{\partial}{\partial y_j}\implies J\nabla q(z) = \sum_{j=1}^{n} \dfrac{2y_j}{r_j^2}\dfrac{\partial}{\partial x_j} - \dfrac{2x_j}{r_j^2}\dfrac{\partial}{\partial y_j}
$$

## Ellipsoid equations
Alternatively, we write

$$
q(z) = 2^{-1}\sum_{j=1}^n\lambda_j(x_j^2 + y_j^2)\implies \dfrac{1}{r_j^2} = \dfrac{\lambda}{2}
$$

with $0<\lambda_n\leq\lambda_{n-1}\leq\cdots\leq\lambda_1$, it is true that $\pm i\lambda_j$ are precisely the eigenvalues of the linear Hamiltonian vector field induced by $q$.


When computing the orbit on the boundary of the ellipse, we need the following identifications. Let $A = \lambda J$, where $$J = J_2 =\begin{bmatrix}0&1\\-1&0\end{bmatrix}$$, and $z = (x,y)\in\real^2$. $z(0) = (x(0), y(0))$, and to the Hamiltonian vector field $X_q = J\nabla q$, $z\in \partial E(q)=\bigset{z\in\real^2,\quad q(z)=1}$ has the flow

$$
z(t) = e^{t\lambda J}z(0)
$$

$$
\langle -JA e^{At}z(0),e^{At}z(0)\rangle
$$

# Determinant Formula Action
Let $x,y\in L^2(S^1)$, where $S^1$ denotes the $1$-torus. Define

$$
a(x,y) = 2^{-1}\int_0^1\langle-J\dot{x},y\rangle dt
$$

if $x = (x_1,\ldots x_{2n})$, and $y = (y_1,\ldots,y_{2n})$, the integrand becomes

$$
\langle -J\dot{x},y\rangle = \sum_{j=1}^n\operatorname{det}\biggl(\begin{bmatrix}\dot{x}_j & y_j\\ \dot{x}_{n+j} & y_{n+j}\end{bmatrix}\biggr)
$$

This is proven using the formula above. Now, the whole integral becomes

$$
a(x,y) = 2^{-1}\sum_{j=1}^n\int_0^1 \operatorname{det}\biggl(\begin{bmatrix}\dot{x}_j & y_j\\ \dot{x}_{n+j} & y_{n+j}\end{bmatrix}\biggr) dt
$$


---


# Symplectic Diffeomorphisms
Let $(M,\omega)$ and $(N,\eta)$ be symplectic manifolds of dimension $2n$. Suppose $u: M\to N$ is a symplectic diffeomorphism, meaning it is a diffeomorphism between smooth manifolds; and for every $p\in M$, $v_1, v_2\in T_pM$, 

## Pullback of symplectic form
$$
(u^*\eta)_p(v_1,v_2) = \eta_{u(p)}\biggl(du_p(v_1),\: du_p(v_2)\biggr) = \omega_p(v_1,v_2)
$$

where $u^*$ denotes the tensor field pullback through $u$, by precomposing $\eta$ with $u$ and $du$ in its arguments.

# Pullback of smooth functions
We define the pullback of a $0$-form (which is also a tensor),

$$
u^*: C^\infty(N)\to C^\infty(M),\quad (u^*f)(p) = (f\circ u)(p),\:\forall f\in C^\infty(N)
$$

## Pullback of vector fields
Let $Y$ be a vector field on $N$. $u^* Y$ is a vector field on $M$, such that for every $p\in M$, we define $$u^*Y (p) = ((du^{-1})_{u(p)}) ( Y_{u(p)} )$$, or

$$
( u^*Y ) = \biggl((du)^{-1}\circ Y\circ u\biggr)
$$

<!-- https://q.uiver.app/#q=WzAsNyxbMCwwLCIoTSxcXG9tZWdhKSJdLFsyLDAsIihOLFxcZXRhKSJdLFswLDIsIlRNIl0sWzIsMiwiVE4iXSxbMCw0LCJDXlxcaW5mdHkoTikiXSxbMCw2LCJcXG1hdGhmcmFre1h9XiooTikiXSxbMiw2LCJcXG1hdGhmcmFre1h9KE4pIl0sWzAsMSwidSJdLFswLDIsInVeKlhfSCIsMl0sWzEsMywiWF9IIl0sWzMsMiwiZHVeey0xfSJdLFs0LDUsImQiLDJdLFs1LDYsIi1cXGhhdHtcXGV0YX0iLDJdLFs0LDYsIi1cXGhhdHtcXGV0YX1eey0xfVxcY2lyYyBkIl0sWzksOCwidV4qIiwwLHsic2hvcnRlbiI6eyJzb3VyY2UiOjIwLCJ0YXJnZXQiOjIwfSwic3R5bGUiOnsiYm9keSI6eyJuYW1lIjoiZG90dGVkIn19fV1d -->
<iframe class="quiver-embed" src="https://q.uiver.app/#q=WzAsNyxbMCwwLCIoTSxcXG9tZWdhKSJdLFsyLDAsIihOLFxcZXRhKSJdLFswLDIsIlRNIl0sWzIsMiwiVE4iXSxbMCw0LCJDXlxcaW5mdHkoTikiXSxbMCw2LCJcXG1hdGhmcmFre1h9XiooTikiXSxbMiw2LCJcXG1hdGhmcmFre1h9KE4pIl0sWzAsMSwidSJdLFswLDIsInVeKlhfSCIsMl0sWzEsMywiWF9IIl0sWzMsMiwiZHVeey0xfSJdLFs0LDUsImQiLDJdLFs1LDYsIi1cXGhhdHtcXGV0YX0iLDJdLFs0LDYsIi1cXGhhdHtcXGV0YX1eey0xfVxcY2lyYyBkIl0sWzksOCwidV4qIiwwLHsic2hvcnRlbiI6eyJzb3VyY2UiOjIwLCJ0YXJnZXQiOjIwfSwic3R5bGUiOnsiYm9keSI6eyJuYW1lIjoiZG90dGVkIn19fV1d&embed" width="487" height="944" style="border-radius: 8px; border: none;"></iframe>

## Hamiltonian Vector Field
Let $K\in C^\infty(N)$ be a smooth function, it defines a *unique* vector field $X_K\in\mathfrak{X}(N)$ through

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

---


*Proof of the diagram*: It suffices to show $-\hat{\omega}^{-1}\circ u^* = u^*\circ (-\hat{\eta}^{-1})$, and by linearity we can remove the negative signs.

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

*Proof for integral flows*: Since $X_k = u^* X_H$, we unbox the definitions, and see that

$$
X_K = (du)^{-1}\circ X_H\circ u\iff du\circ X_K = X_H\circ u
$$

Let $p\in M$, $q\in N$ be arbitrary, the above expression reads

$$
du_p\circ X_K(p) = X_H\circ u(p),\quad\text{and}\quad (du^{-1})_q\circ X_H = X_K\circ u^{-1}(q)
$$

Therefore $X_K$ and $X_H$ are related by $u$, $u^{-1}$ Lee Prop 9.6 tells us their integral curves are related by $u$, $u^{-1}$. More precisely, if $f(t), g(t)$ are integral curves of $X_K$ and $X_H$, then $u\circ f(t)$, $u^{-1}\circ g(t)$ are integral curves of $X_H$ and $X_K$ respectively.


![Prop 9.6]({{ site.baseurl }}{% link /images/lee-prop-9-6.png %})


---


# Special symplectic capacity $c_0$
First we define a class of Hamiltonians, a smooth function $H\in C^\infty(M,\real)$ is in $\mathcal{H}(M,\omega)$ if

- There exists a compact subset $K\subseteq M\setminus \partial M$, where $H(M\setminus K)=m(H)$

- There exists an open subset $U\subseteq M$ where $H(U)=0$,

- $0\leq H(x)\leq m(H)$, for every $x\in M$, where $m(H) = \max H - \min H$

A function $H\in\mathcal{H}(M,\omega)$ is *admissable*, if all periodic solutions of $H$ are either constant, or have period $T>1$. We denote the class of admissable functions in $\mathcal{H}(M,\omega)$ by $\mathcal{H}_a(M,\omega)$.

We wish to show $c_0$ satisfies the definition of a symplectic capacity.

## Monotonicity of $c_0$.

Let $(M,\omega)$ and $(N,\eta)$ be symplectic manifolds, and suppose $\varphi: M\to N$ is a symplectic embedding. Assume further $M$ and $N$ are both of dimension $2n$. Fix $H\in \mathcal{H}(M,\omega)$, define $\varphi^* H: N\to\real$ as

$$
(\varphi^*H)(x) = \begin{cases} H\circ \varphi^{-1}(x) &x\in \varphi(M)\\ m(H)&x\notin\varphi(M)\end{cases}
$$

we wish to show $\varphi^*H$ is
- smooth,
- is in $\mathcal{H}(N,\eta)$, and
- is in $\mathcal{H}_a(N,\eta)$ iff $H$ is in $\mathcal{H}(M,\omega)$.

### Proof of $\varphi^* H\in C^{\infty} (N,\real)$
We need to investigate the topological properties of $M$.

The inclusion map is smooth, so it maps compact sets onto compact sets. Suppose $x\notin\varphi(K)$, there are two possibilities:

- If $x\in \varphi(M)$, then $x\in\varphi(M)\setminus\varphi(K)$ if and only if $\varphi^{-1}(x)\notin K$. So $\varphi^*H(x) = H\circ\varphi^{-1}(x) = H(\varphi^{-1}(x))=m(H)$, since $\varphi^{-1}(x)\notin K$.

- If $x\notin \varphi(M)$, by definition $\varphi^*H(x)=m(H)$. 

    In both cases, $\varphi^* H(x) = m(H)$. Since $\varphi(K)$ is compact, it is closed. Its complement is an open set containig $x$ where $\varphi^*H$ is constant.

The restriction of $\varphi^* H $ onto the $\varphi(K)$ is just $H\circ \varphi^{-1}$, it is a composition of smooth maps, which is again smooth. Therefore $\varphi^* H$ is a smooth function.

### Proof $\varphi^*H \in \mathcal{H}(N,\eta)$
The first property of $\mathcal{H}(N,\eta)$ is trivially satisfied. 

### Problem with the second property

To prove the second, we need to find an open set $W\subseteq N$ where $\varphi^*H (U)\equiv 0$. Ideas so far

- Our original Hamiltonian $H\subseteq M\setminus \partial M$. By Lee 1.x, the manifold interior is an open submanifold of codimension $0$, so $U$ is an open subset of $\operatorname{Int}(M)$.

- Use the local $0$-slice criterion. For every $p\in U\subseteq M\setminus \partial M$, it is in the image of a local defining function. $F:W\to\real^n$? This does not ensure the set is open.

- Final answer: Use a triple inclusion setup, let $U$ be an open submanifold of $\operatorname{Int}(M)$ which is again an open submanifold of $M$, so

    $$
    U\hookrightarrow \operatorname{Int}(M)\hookrightarrow M\hookrightarrow N
    $$

    The image of $U$ is then an embedded submanifold of codimension $0$. It has an empty boundary.

    ![manifolds-with-boundary]({{ site.baseurl }}{% link /images/manifolds-with-boundary.png %})

    hence $\varphi(U)$ is open in $N$.

### Third property
The third property is easily satisfied since $0\leq \varphi^* H(x)\leq m(\varphi^* H) = m(H)$. Therefore $\varphi^* H\in \mathcal{H}(N,\eta)$.

#### Proof $\varphi^*H \in\mathcal{H}_a(N,\eta)$ iff $H\in\mathcal{H}(M,\omega)$

Let $\gamma: J\to M$ be an integral curve for the vector field $X_H$, since $X_H$ and $X_{\varphi^* H}$ are related $\varphi^{-1}$. If $\gamma$ is a non-constant periodic orbit iff $\varphi\circ \gamma$ is a non-constant periodic orbit for $X_{\varphi^* H}$. Conversely, if $\theta$ is a non-constant periodic orbit of $X_{\varphi^* H}$, this forces the range of $\theta$ to lie in the support of $X_{\varphi^* H}$, which is contained in the image of $\varphi(M)$. So $\varphi^{-1}\circ\theta$ is a non-constant periodic orbit of $X_H$.

In a word: the non-constant periodic orbits of $X_H$ and $X_{\varphi^* H}$ differ up to a reparametrization. This proves the claim.