---
layout: article
title: Notes on Symplectic Capacity
date: 2023-08-02 23:52
tags: ['symplectic']
---
# Symplectic Capacities

## Introduction

We define a map from the space of symplectic manifolds to $[0,+\infty]$. We only compare the symplectic capacities of symplectic manifolds of the same dimension. Let $(M,\omega)$ be a symplectic manifold of dimension $2n$. 

<div class="definition-box" markdown=1 name="Symplectic capacity">
A **symplectic capacity** $c$ is a map on the set of symplectic manifolds,
$$c: (M,\omega)\mapsto c(M,\omega)\in [0,+\infty]$$ 

satisfying the following properties

- **Monotonicity**: If $(M,\omega)$ embeds symplectically into $(N,\eta)$, where $M$ and $N$ are of the same dimension, 
    $$c(M,\omega)\leq c(N,\eta)$$

- **Conformality**: If $\alpha$ is a non-zero real number, then
    $$c(M,\alpha\omega) = \vert\alpha\vert c(M,\omega)$$

- **Non-triviality**: Let $B(1), Z(1)\subseteq\real^{2n}$ be the open unit ball and the *open symplectic cylinder*,
    
    $$
    \begin{align}
    B(r) &= \bigset{x\in\real^{2n},\: \sum_{j=1}^n x_j^2 + x_{n+j}^2 < r^2}\\
    Z(r) &= \bigset{x\in\real^{2n},\: x_1^2 + x_{n+1}^2< r^2}
    \end{align}
    $$
    
    then,
    $$
    c(B(1),\omega_0) = \pi = c(Z(1), \omega_0)
    $$

    Remark: we view $(B(r),\omega_0)$ as an open submanifold of codimension $0$, with the standard symplectic form inherited from $\real^{2n}$.
</div>

If $M$ and $N$ are symplectic manifolds of dimension $2n$, and are symplectically diffeomorphic, applying monotonicity twice gives $c(M,\omega) = c(N,\eta)$ for every capacity $c$. From the definitions, we can deduce additional properties (of which we will not prove) that apply to any capacity $c$
<div class="theorem-box" markdown=1 name="Properties of symplectic capacities">
- Homogeneity: $c(\lambda U)=\lambda^2 c(U)$
- Non-triviality on ellipsoids: If $E$ is an ellipsoid in $(\real^{2n},\omega_0)$, $c(E) = \pi [r_1(E)]^2$, where  $r_1$ is the 'largest' side of the ellipsoid.
- If $D\subseteq \real^{2}$ is a compact, connected domain that is the boundary of a smooth submanifold, then $c(D,\omega_0)=\operatorname{area}(D)$.
</div>
Roughly speaking, a symplectic capacity gives an upper bound on the area 'swept' by the quadratic forms.

<div class="definition-box" markdown=1 name="Inner regularity">
A symplectic capacity $c$ is **inner regular** if it can be approximated from below by capcaities of open submanifolds $c(U,\omega)$ that hide in the manifold boundary of $M$. In symbols,

$$
c(M,\omega) = \sup\bigset{c(U,\omega),\: U\subseteq M\text{ is open, and }\cl{U}\subseteq M\setminus\partial M}
$$


</div>

## Gromov width $D(M,\omega)$
One example of a symplectic capacity is the Gromov width,

<div class="definition-box" markdown=1 name="Gromov width">
Let $(M,\omega)$ be any symplectic manifold, we define its **Gromov width** by the following

$$
D(M,\omega) = \sup\bigset{\pi r^2,\: \varphi: B(r)\induces (M,\omega)}
$$

where $\varphi$ is a symplectic embedding of the open ball $$B(r) =\bigset{x\in\real^{2n},\: \vert x\vert < r}$$

</div>

<div class="theorem-box" markdown=1 name="">
The Gromov width is a symplectic capacity. It is also minimal, meaning if $c$ is any capacity, then $D\leq c$.
</div>
<div class="proof-box" markdown=1 proof-name="">
See Flexcil Notes Page 7
</div>

# The Symplectic capacity $c_0$

## Introduction
<div class = "definition-box" markdown=1 name="Regular Hamiltonians $\mathcal{H}(M,\omega)$">
A smooth function $H$ is called a **regular Hamiltonian**, or  $H\in\mathcal{H}(M,\omega)$ if all of the following hold

- There exists a **compact subset** $K\subseteq M\setminus \partial M$, where $H(M\setminus K)=m(H)$

- There exists an **open subset** $U\subseteq M$ where $H(U)=0$,

- $0\leq H(x)\leq m(H)$, for every $x\in M$, where $m(H) = \max H - \min H$. The quantity $m(H)$ is commonly referred to as the $c_0$ oscillation of $H$.
</div>
The following will be the most important definition for our purposes.
<div class="definition-box" markdown=1 name="Admissable Hamiltonians $\mathcal{H}_a(M,\omega)$">
A regular Hamiltonian $H$ is **admissable**, if **all periodic solutions of $H$ are either constant, or have period $T>1$**. We denote the class of admissable functions in $\mathcal{H}(M,\omega)$ by $\mathcal{H}_a(M,\omega)$.
</div>

We wish to show $c_0$ satisfies the definition of a symplectic capacity. This will be done in 3 parts.

## Monotonicity of $c_0$.
To show monotonicity, we fix a regular Hamiltonian $H$on $(M,\omega)$. We will construct an extension of $H$ using the symplectic embedding, so that this extension is regular on $(N,\eta)$. Denoting the extension by $\varphi^* H$, we show that $H$ is admissable on $(M,\omega)$ iff $\varphi^* H$ is admissable on $(N,\eta)$, and this extension preserves '$c_0$' oscillation of $H$ is equal to that of $\varphi^* H$, more precisely

$$
\max H(x) - \min H(x) = m(H) = m(\varphi^* H) - \max \varphi^* H(x) - \min \varphi^* H(x)
$$

Since $\varphi^*: \mathcal{H}_a(M,\omega)\to \mathcal{H}_a(N,\eta)$,  this proves

$$
\sup\bigset{m(H),\: H\in\mathcal{H}_a(M,\omega)}\leq \sup\bigset{m(H),\: H\in\mathcal{H}_a(N,\eta)}
$$

and monotonicity follows immediately.

<div class="theorem-box" markdown=1 name="Naturality of Hamiltonian Extensions">
Let $(M,\omega)$ and $(N,\eta)$ be symplectic manifolds, and suppose $\varphi: M\to N$ is a symplectic embedding. Assume further $M$ and $N$ are both of dimension $2n$. Fix $H\in \mathcal{H}(M,\omega)$, define $\varphi^* H: N\to\real$ as

$$
(\varphi^*H)(x) = \begin{cases} H\circ \varphi^{-1}(x) &x\in \varphi(M)\\ m(H)&x\notin\varphi(M)\end{cases}
$$

To this, we claim $\varphi^* H$ satisfies the three properties in Definition 2.1. That is, 1) $\varphi^* H$ is a smooth function, 2) is in $\mathcal{H}(N,\eta)$, and 3) is in $\mathcal{H}_a(N,\eta)$ iff $H$ is in $\mathcal{H}_a(M,\omega)$.
</div>
<div class="proof-box" markdown=1 proof-name="Proof of Naturality of Hamiltonian Extensions">
We first show smoothness, recalling the properties of $M$ being a *embedded submanifold of $N$*, 

The inclusion map is smooth, so it maps compact sets onto compact sets. Suppose $x\notin\varphi(K)$, there are two possibilities:

- If $x\in \varphi(M)$, then $x\in\varphi(M)\setminus\varphi(K)$ if and only if $\varphi^{-1}(x)\notin K$. So $\varphi^*H(x) = H\circ\varphi^{-1}(x) = H(\varphi^{-1}(x))=m(H)$, since $\varphi^{-1}(x)\notin K$.

- If $x\notin \varphi(M)$, by definition $\varphi^*H(x)=m(H)$. 

    In both cases, $\varphi^* H(x) = m(H)$. Since $\varphi(K)$ is compact, it is closed. Its complement is an open set containig $x$ where $\varphi^*H$ is constant.

The restriction of $\varphi^* H $ onto the $\varphi(K)$ is just $H\circ \varphi^{-1}$, it is a composition of smooth maps, which is again smooth. Therefore $\varphi^* H$ is a smooth function.

We now show the regularity of $\varphi^* H$. The first property (the compactness of the "support" of the induced HVF) of $\mathcal{H}(N,\eta)$ is trivially satisfied. 

To prove the second, we need to find an open set $W\subseteq N$ where $\varphi^*H (U)\equiv 0$. Ideas so far

- Our original Hamiltonian $H\subseteq M\setminus \partial M$. By Lee 1.x, the manifold interior is an open submanifold of codimension $0$, so $U$ is an open subset of $\operatorname{Int}(M)$.

- Use the local $0$-slice criterion. For every $p\in U\subseteq M\setminus \partial M$, it is in the image of a local defining function. $F:W\to\real^n$? This does not ensure the set is open.

- Final answer: Use a triple inclusion setup, let $U$ be an open submanifold of $\operatorname{Int}(M)$ which is again an open submanifold of $M$, so

    $$
    U\hookrightarrow \operatorname{Int}(M)\hookrightarrow M\hookrightarrow N
    $$

    The image of $U$ is then an embedded submanifold of codimension $0$. It has an empty boundary.

    ![manifolds-with-boundary]({{ site.baseurl }}{% link /images/manifolds-with-boundary.png %})

    hence $\varphi(U)$ is open in $N$, and this proves the 'second property'; $\varphi^* H$ admits an open set on which it vanishes.

The proof of the third property is simple. We see that for every $x\in N$, 

$$0\leq \varphi^* H(x)\leq m(\varphi^* H) = m(H)$$

Therefore $\varphi^* H\in \mathcal{H}(N,\eta)$. Finally, we show that $H$ is admissable iff its extension $\varphi^* H$ is.

Let $\gamma: J\to M$ be an integral curve for the vector field $X_H$, since $X_H$ and $X_{\varphi^* H}$ are related $\varphi^{-1}$. If $\gamma$ is a non-constant periodic orbit iff $\varphi\circ \gamma$ is a non-constant periodic orbit for $X_{\varphi^* H}$. Conversely, if $\theta$ is a non-constant periodic orbit of $X_{\varphi^* H}$, this forces the range of $\theta$ to lie in the support of $X_{\varphi^* H}$, which is contained in the image of $\varphi(M)$. So $\varphi^{-1}\circ\theta$ is a non-constant periodic orbit of $X_H$.

In a word: **the non-constant periodic orbits of $X_H$ and $X_{\varphi^* H}$ differ up to a reparametrization**. This proves the claim.
</div>

