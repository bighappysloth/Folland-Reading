---
layout: post
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

# Pullack of Flows
Lee Chap 8:
Let $F: M\to N$ and $X,Y$ be vector fields on $M$ and $N$ respectively. They are $F$-related if 

$$
dF_p(X_p) = Y_{F(p)}\quad dF \circ X = Y\circ F
$$

![Prop 9.6]({{ site.baseurl }}{% link /images/lee-prop-9-6.png %})

# Monotonicity of $c_0$.
First we define a class of Hamiltonians, a smooth function $H\in C^\infty(M,\real)$ is in $\mathcal{H}(M,\omega)$ if

- There exists a compact subset $K\subseteq M\setminus \partial M$, where $H(M\setminus K)=m(H)$

- There exists an open subset $U\subseteq M$ where $H(U)=0$,

- $0\leq H(x)\leq m(H)$, for every $x\in M$, where $m(H) = \max H - \min H$

A function $H\in\mathcal{H}(M,\omega)$ is *admissable*, if all periodic solutions of $H$ are either constant, or have period $T>1$. We denote the class of admissable functions in $\mathcal{H}(M,\omega)$ by $\mathcal{H}_a(M,\omega)$.

Let $(M,\omega)$ and $(N,\eta)$ be symplectic manifolds, and suppose $\varphi: M\to N$ is a symplectic embedding. Assume further $M$ and $N$ are both of dimension $2n$. Fix $H\in \mathcal{H}(M,\omega)$, define $\varphi^* H: N\to\real$ as

$$
(\varphi^*H)(x) = \begin{cases} H\circ \varphi^{-1}(x) &x\in \varphi(M)\\ m(H)&x\notin\varphi(M)\end{cases}
$$

we wish to show $\varphi^*H$ is
- smooth,
- is in $\mathcal{H}(N,\eta)$, and
- is in $\mathcal{H}_a(N,\eta)$ iff $H$ is in $\mathcal{H}(M,\omega)$.

*Proof for Smoothness*: We need to investigate the topological properties of $M$.