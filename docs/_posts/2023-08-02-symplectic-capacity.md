---
layout: article
title: Part 3 - Symplectic Capacities
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

## Monotonicity of $c_0$
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

## Conformality of $c_0$
To show conformality, fix a real number $\alpha\neq 0$. If $(M,\omega)$ is a symplectic manifold, so is $(M,\alpha\omega)$. The following result exploits the fact that regularity of a Hamiltonian function depends only on its **topological properties**.

<div class="theorem-box" markdown=1 name="">
Let $\psi: \hil(M,\omega)\to \hil(M,\alpha\omega)$, such that $\psi$ multiplies any regular Hamiltonian $H\in \hil(M,\omega)$ **pointwise** by $\vert\alpha\vert$. Meaning $\psi(H) = \vert\alpha\vert H$. Then,

- $\psi$ maps $\hil(M,\omega)$ into $\hil(M,\alpha\omega)$,
- $\psi$ is a bijection,
- $\psi(H)$ is admissable in $(M,\alpha\omega)$ iff $H$ is admissable in $(M,\omega)$.

</div>
<div class="proof-box" markdown=1 proof-name="">
The first two claims are obvious, since the pointwise multiplication of a $C^\infty(M)$ function does not change the **topological properties** of $F$, and $\vert\alpha\vert F\geq 0$. So $\psi$ maps into $\hil(M,\alpha\omega)$, and has the obvious inverse $F\mapsto \vert\alpha\vert^{-1}F$. 

Recall the associated HVF to a function $F\in C^\infty(M)$ is defined 

$$
X_F = -\hat{\omega}^{-1}(dF)\quad\text{and}\quad\omega(X_F,Y) = -dF(Y)\quad\forall Y\in \mathfrak{X}(M)
$$

Let $Y$ be a vector field on $M$, since $(M,\omega)$ and $(M,\alpha\omega)$ are **identical** as *smooth* manifolds (or diffeomorphic), $Y$ is a VF on both *symplectic* manifolds. Then,

$$
\begin{align}
(\alpha\omega)(X_{\psi(F)},Y) &= -\vert\alpha\vert dF(Y)\\
\omega(\alpha X_{\psi(F)}, Y) &= \vert\alpha\vert(-dF(Y))\\
&=\vert\alpha\vert\omega(X_{F}, Y)\\
&= \omega(\vert\alpha\vert X_{F},Y)
\end{align}
$$

Comparing the second and the last line, uniqueness follows from the non-degeneracy of $\omega$. Therefore

$$
\alpha X_{\psi(F)} = \vert\alpha\vert X_F\implies X_{\psi(F)} = \pm X_F
$$

Let $\theta_x(t)$ be a flow of $X_{\psi(F)}$, then so is $\theta_x(\pm t)$. Therefore their periodic solutions correspond to each other, and $F$ is admissable iff $\psi(F)$ is. Finally, a simple computation on the $c_0$ oscillation of $\psi(F)$ shows that $m(\psi(F)) = \vert\alpha\vert m(F)$. Therefore, $\vert\alpha\vert c_0(M,\omega) = c_0(M,\alpha\omega)$.

</div>


## Non-triviality of $c_0$
The proof for the non-triviality of $c_0$ is extremely long. An outline:

- By monotonicity and Gromov's Squeezing Theorem, it suffices to show $c_0 (B(1),\omega_0)\geq \pi$

    $$
    c_0(Z(1),\omega_0)\geq c_0(B(1), \omega_0)
    $$

    In general, there are three approaches to showing $\sup(A)\geq x$, namely 1) $x\in A$, 2) $x+\varepsilon\in A$, 3) $\\{x - n^{-1}\\}_{n\geq 1}\subseteq A$. We will use the third approach. 

    $$
    c_0(B(1),\omega_0) = \sup\bigset{m(F),\: F\in\hil_a(B(1),\omega_0)}
    $$

- Let $f:[0,1]\to[0,+\infty)$ be a smooth function that satisfies

    - $0\leq f'(t)<\pi$,
    - $f(t)=0$ for $t$ sufficiently near $0$,
    - $f(t)=\pi-\varepsilon$ for $t$ sufficiently near $1$.

    We will construct $f$ explicitly later. The rest of the proof is [here]({{ site.baseurl }}{% link /download/symplectic-excerpts/non-triviality-part1.pdf %}), in particular pages 3-4. Working thorugh the parts with the Poisson Bracket:

    <div class="note-box" markdown=1 name="Notes on Poisson Bracket">
    Let $G(x) = f(\vert x\vert^2)$, we wish to show the Euclidean norm $R(x) = 2^{-1}\vert x\vert^2$ is a **conserved quantity** of the H-system $(B(1),\omega_0, G)$.

    We do this by computing the **Poisson Bracket** between $G$ and $R$, denoted by $(G,R)_{\mathcal{P}}$

    $$
    (G,R)_{\mathcal{P}} = \omega_0(X_G,X_R) = dG(X_R) = \langle \nabla G, X_R\rangle
    $$

    Computing the HVF of $R$, $X_R(x) = J\nabla R(x) = Jx$ for $x\in B(1)$, so
    
    $$
    \begin{align}
    (G,R)_{\mathcal{P}} &= \langle \nabla G, Jx\rangle_{\real^{2n}} \\
    &= \langle 2f'(\vert x\vert^2)x, Jx\rangle\\
    &= 2f'(\vert x\vert^2)\langle x,Jx\rangle\\
    &= 0
    \end{align}
    $$

    therefore $R$ is conserved under the flow of $X_G$. Since $X_G = J\nabla G$, if $x(t)$ parametrizes an integral curve, then $2R(x(t))=\vert x\vert^2 =\tau$ is constant. Therefore

    $$
    X_G(x(t)) = J\nabla G(x(t)) = 2f'(\tau)Jx(t)
    $$
    
    Absorbing $2f'(\tau)J = aJ$ as a left-invariant VF on $B(1)$, $x(t)$ is therefore a solution of 

    $$
    \dot{x} = aJx
    $$

    Assuming $a\neq 0$ for the moment, we then compute the one-parameter subgroup of the LIVF $X_G$, $$(t, x(0))\mapsto x(0)\cdot \operatorname{exp}(aJt)$$, where 
    
    $$aJ = \begin{bmatrix} 0 & -aI_n \\ aI_n & 0 \end{bmatrix}$$

    which is $\frac{2\pi}{a}$ periodic, with the solution 

    $$
    x(t) = \cos(at)x(0) + \sin(at)Jx(0),\quad a = f'(\vert x\vert^2)
    $$

    and $\frac{2\pi}{a}>1$ for $a\neq 0$. If $a=0$ then $X_G(x)=0$, and $x(t)$ is a constant solution. Furthermore, 

    - $G$ is a non-negative smooth function, which vanishes in some neighbourhood of the origin, and is also *compactly supported* (when interpreted in the right way). Since $B(1)$ has empty manifold boundary, and attains its maximum outside some compact set: $m(G) = \max(G)-\min(G) = \pi-\varepsilon$. **This proves $G$ is regular**, with oscillation $\pi-\varepsilon$.

    - The argument we made shows that **all** solutions of $G$ are either constant or with period **strictly greater** than $1$, and **$G$ is admissable**.

    - Hence $c_0(B(1),\omega_0)\geq \pi-\varepsilon$ for every $\varepsilon>0$. As we have remarked earlier, this shows $$c_0(B(1),\omega_0)\geq \pi$$. 

    </div>

To prove the reverse inequality, 

$$
\pi\geq c_0(Z(1),\omega_0)
$$

we wish to show "**every regular Hamiltonian $H\in\hil(Z(1),\omega_0)$ with oscillation $m(H)>\pi$ must be non-admissable**, summarized in the following theorem:

<div class="theorem-box" markdown=1 name="">
For every $\varepsilon>0$, if $H$ is a regular Hamiltonian on $Z(1)$, that is: $H\in \hil(Z(1),\omega_0)$ with oscillation $m(H) = \pi+\varepsilon$. Then $F$ is not admissable (it contains a non-constant orbit of $T\in(0,1]$).

**We will prove something stronger, that $H$ contains a non-constant orbit of period $T=1$**.

</div>
Since the proof for this theorem is too long to be contained in one section, we conclude this section with two reductions we can make to $H$.

### Reductions
<div class="theorem-box" markdown=1 name="">
Let $\varepsilon>0$ and $H$ a regular Hamiltonian on $Z(1)$ with oscillation $\pi+\varepsilon$. To show $H$ is *not* admissable, 

- Reduction 1) We can assume $H$ vanishes on a neighbourhood of the origin,
- Reduction 2) We can "extend" $H$ to be a smooth function on $\real^{2n}$ that defines a HVF. **Our choice of extension will be specially tailored for our purposes.**

</div>
<div class="note-box" markdown=1 name="">
For full proof, see [this document]({{ site.baseurl }}{% link /download/symplectic-excerpts/hofer-reductions-1-2.pdf %})
</div>
<div class="proof-box" markdown=1 proof-name="Proof of first reduction">
The proof of the first reduction is rather geometric. Since $H$ is regular, there exists a $z_0\in U$ where $U$ is an open subset of $Z(1)$ on which $H$ vanishes. We will construct a **compactly supported HVF**, and use the **time-one map of its flow**, as the symplectomorphism that relates $H$ and $H\circ \theta$. 

Define the subset $$L = \bigset{tz_0,\: 0\leq t\leq 1}$$. $L$ is clearly compact, thus admits an open, precompact $\varepsilon$-[fattening]({{ site.baseurl }}/{% post_url 2023-07-28-compact-fattenings %}), $B_{\varepsilon}(L)\subseteq Z(1)$. It is clear $B_{\varepsilon2^{-1}}(L)$ has compact closure, by the smooth Urysohn's Lemma, there exists a $$\rho\in C_c^\infty(Z(1))$$ with $$\rho(\cl{B_{\varepsilon2^{-1}}}(L)) = 1$$, and $$\supp{\rho}\subseteq B_{\varepsilon}(L)$$.

Let $K(z)$ define the following Hamiltonian, whose HVF is *engineered* so that $X_K$ always **points in the direction of $z_0$**

$$
K(z) = \rho(z)\cdot(-Jz_0\lrcorner E_{\real^{2n}})
$$

where $E_{\real^{2n}}:\real^{2n}\times\real^{2n}\to\real$ is the standard Euclidean product. It is clear for every $z\in V = B_{\varepsilon2^{-1}}(L)$, 

$$
dK(z) = 1\cdot(-Jz_0)\lrcorner E_{\real^{2n}}
$$

and by definition of the gradient with respect to $E_{\real^{2n}}$, $\nabla K = -Jz_0$, which implies $X_K = J\nabla K = z_0$. 

<div class="note-box" markdown=1 name="">
Two things: 
- The differential of a linear map is the linear map itself. 
- Recall $J^{-1} = -J$, so the $\nabla K = J^{-1}z_0$.
</div>

Now, $K$ is *compactly supported* as a smooth function, so $X_K$ is *compactly supported* as a HVF. Let $\theta$ be the global flow of $X_K$, and because the origin, $0\in L\subseteq V$, there exists an open neighbourhood about $0$ where $\rho = 1$. By existence and uniqueness, if $\theta_0(t)$ is the integral curve starting at the origin, and 

$$
\theta_0(t) = \theta_0(t) - \theta_0(0) = \int_0^t z_0 dt = tz_0\forall 0\leq t\leq 1
$$

<div class="note-box" markdown=1 name="">
The bounds placed on $t$ are necessary otherwise $\theta_0(t)$ escapes $V$ where $\rho=1$.
</div>

Relabel $\theta^1 = \theta$ as the time-one map of $\theta$. By the properties of a global flow: 

- $\theta^1$ is a diffeomorphism between  $$\bigset{x\in Z(1),\: (1,x)\in\dzz(\theta)}$$ and $$\bigset{x\in Z(1),\: (-1,x)\in\dzz}$$. Both sets are equal to $Z(1)$ itself, and $$\theta^1\vert_{A^c}=\id{A^c}$$ for some compact $A\subseteq Z(1)$ (this is because $X_K$ is compactly supported, so the integral curves starting outside $A$ are constant).
- Since $X_K$ is an HVF, its integral flows preserve the symplectic form, 

    $$
    \mathcal{L}_{X_K} \omega_0 = 0\quad\text{equivalently}\quad \theta_x^* \omega_0 = \omega_0
    $$

    where $\mathcal{L}$ denotes the Lie-derivative. 
- And $\theta^1 = \theta$ is a symplectic diffeomorphism. We have proven earlier that Hamiltonian functions $\cl{H}$ and $H$ that are **symplectomorphically related**, to each other (meaning $\cl{H} = H\circ \theta$) have periodic orbits that correspond precisely to one another. Moreover, and their integral flows are conjugated by $\theta$.
- Assuming $\cl{H}$ is a regular Hamiltonian: **$H$ is not admissable if and only if $\cl{H}=H\circ\theta$ is not admissable**, and Reduction 1) is valid.

<div class="note-box" markdown=1 name="">
We prove $\cl{H}$ is regular. Smoothness is easy to check, and there exists an open set $\cl{U} = \theta^{-1}(U)$ on which $\cl{H}$ vanishes, since 

$$
\cl{H}(\cl{U}) = H(\theta(\theta^{-1}(U)))=H(U)=0
$$

Let $A$ be the compact subset of $Z(1)$ where $H(Z(1)\setminus A)=m(H)$, then $\cl{A}=\supp{\rho}\cup \theta^{-1}(A)$ is again compact in $Z(1)$, as $\theta$ is a homeomorphism hence a proper map.


</div>

</div>
<div class="proof-box" markdown=1 proof-name="Proof of second reduction">
See the document linked [here]({{ site.baseurl }}{% link /download/symplectic-excerpts/hofer-reductions-1-2.pdf %}).

By suppressing $\varepsilon$, we can assume $m(H)>\pi$, and $\varepsilon>0$ is a constant so that 

$$
m(H)> \pi + \varepsilon > \pi
$$

Set $\delta = m(H)-(\pi + \varepsilon)$, and let $\Phi$ be the **standard mollifier** supported on $[-\delta, +\delta]$. We outline the construction of $\Phi$ in the following note

<div class="note-box" markdown=1 name="">
Let $\phi = \operatorname{exp}(1/(x^2 - 1))$ for $\vert x\vert < 1$, and $\phi = 0$ for $\vert x\vert \geq 1$. In symbols:


$$
\phi(x) = \begin{cases}\operatorname{exp}(1/(x^2 - 1)) & \vert x \vert < 1 \\ 0 & \vert x \vert \geq 1\end{cases}
$$

It is well known $\phi$ is smooth (and compactly supported). Let $A$ be the integral of $\phi$. Relabel $\phi = A^{-1}\phi$. We also agree, if $t>0$ to denote the **$t$ shrinkage of $\phi$** by

$$
\phi_t(x) = t^{-1}\phi(xt^{-1}),\quad \int\phi_t = \int \phi = 1
$$

set $t = \delta$, and define $\Phi = \phi_\delta$. $\Phi$ integrates to $1$, and is smooth and compactly supported on $[-\delta, + \delta]$.

</div>

<div class="theorem-box" markdown=1>
We require a function $f:\real\to\real$ that satisfies

- $f(s) = m(H)$ for $s\leq 1$,
- $f(s) \geq (\pi + \varepsilon)s$ for all $s\in\real$,
- $f(s) = (\pi+\varepsilon)s$ for $s$ large 
- $0<f'(s)<\pi+\varepsilon$ for $s>1$
</div>
<div class="proof-box" markdown=1 proof-name="Proof of Smooth Transition Function:">

The following is a smooth transition function that transistions from a constant to a linear function, computing its derivative,

<iframe src="https://www.desmos.com/calculator/zmuh9vgmb3?embed" width="800" height="800" style="border: 1px solid #ccc" frameborder=0></iframe>

[Desmos](https://www.desmos.com/calculator/rcxvs2bzvd)

Computation of the derivatives is an easy task, verification later

The upper bound on the derivative controls $T$ of any periodic orbit of $X_{\cl{H}}$.

- Include the argument of separating the integral curves in and outside the ellipsoid $E$.
</div>

</div>

