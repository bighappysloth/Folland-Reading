---
layout: article
title: Notes on 'b' functional
date: 2023-08-05 20:10
tags: ['symplectic']
tao_link: 'https://terrytao.wordpress.com/2022/05/10/partially-specified-mathematical-objects-ambient-parameters-and-asymptotic-notation/'
---
# Useful estimates on our Hamiltonian
We must prove three important estimates that allow us to control the size of $H$, $\nabla H$, $H_{zz}$ and their integrals. 

## Estimates on $H$

In this section, $H$ will denote the special Hamiltonian which vanishes in some neighbourhood of the origin, and is quadratic ($H = Q$) at infinity. 


$$
Q(z) = (\pi + \varepsilon)q(z) = (\pi+\varepsilon)\biggl(z_1^2 + z_{n+1}^2 + N^{-2}\sum_{j=2}^{n} z_{j}^2 + z_{n+j}^2\biggr)
$$

First we begin with a useful estimate. 




<div class="lemma-box" markdown=1>

$$
\vert H(z)\vert\Lsim \vert z\vert^2
$$


</div>
<div class="proof-box" markdown=1 proof-name="">
There exists an open ball of radius $\delta < R$, $B(\delta)$ where $H(B(\delta))=0$. By the extreme value theorem, there exists an $M_0>0$ with 

$$
\vert H(z)\vert < \delta^2 M_0\implies \vert H(z)\vert \leq M_0\vert z\vert ^2,\quad\forall z\in \cl{B(R)}\setminus B(\delta)
$$

Since $\vert H(z)\vert \leq M_1 \vert z\vert ^2$ for $\vert z\vert > R$, set $M_2 = (M_1 + 1)(M_0 + 1)$ and the result follows.

</div>

<div class="lemma-box" markdown=1>
If $x\in L^2(S^1, \real^{2n})$, then $H(x(t))\in L^1(S^1,\real)$.
</div>
<div class="proof-box" markdown=1 proof-name="">
Use monotonicity of the integral.
</div>

<div class="lemma-box" markdown=1>

$$
\vert \nabla H(z)\vert\Lsim \vert\nabla q(z)\vert \Lsim \vert z\vert
$$


</div>
<div class="proof-box" markdown=1 proof-name="">
Similar to the previous Lemma, we can consider $\nabla H(z) = (f_1,\ldots f_{2n})$ as a vector valued function. Let $f_i$ be arbitrary, since all norms on finite-dimensional vector spaces are equivalent, it suffices to show

$$
\vert f_i(z)\vert \Lsim \vert \nabla q(z)\vert \Lsim \vert z\vert
$$

However, $Q$ and $q$ are comparable up to a constant multiple, and the gradient of $Q$ is given by:

$$
\begin{align}
\nabla Q(z) = 2(\pi+\varepsilon)\biggl(z_1, N^{-2}z_2,\ldots,N^{-2}z_n,z_{n+1},N^{-2}z_{n+2},\ldots,N^{-2}z_{2n}\biggr)
\end{align}
$$

or in matrix form

$$
\nabla Q(z) = 2(\pi+\varepsilon)\begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & \id{n-1}N^{-2} & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & \id{n-1}N^{-2}\end{bmatrix}\begin{bmatrix} z_1 \\ \vdots \\ \vdots \\ z_{2n}\end{bmatrix}
$$

so that $\nabla Q(z)$ is comparable to the standard norm $\vert z\vert$ for $\vert z\vert > R$. Next, apply the extreme value theorem to $f_i$  and obtain $M_0$ with

$$
\vert f_i(z)\vert \leq M_0(N+1)^{-1}\delta\leq M_0\vert\nabla q(z)\vert,\quad\forall z\in \cl{B(R)}
$$

Projections are norm-decreasing maps, hence $\vert f_i(z)\vert \leq \vert \nabla H(z)\vert\leq M_1 \vert\nabla q(z)\vert$ for $\vert z\vert > R$. Setting $M_2$ to be
 the maximum of $M_0$ and $M_1$ again completes the proof.
</div>



## Gradient of $H$

<div class="lemma-box" markdown=1>
Suppose the Hessian matrix of $H$, denoted by $H_{zz}$ is bounded above by a constant $M\in\real$. If $z$ and $a$ are arbitrary points in $\real^{2n}$, then

$$
\vert \nabla H(z+a) - \nabla H(z)\vert \Lsim \vert a \vert
$$


</div>

<div class="proof-box" markdown=1 proof-name="Proof of the inequality">
Write $H_{zz}(z) = (f_1(z),\ldots, f_{2n}(z))$. Using the fact that $\sup_{i} \vert f_i(z)\vert$ is comparable to $\vert H_{zz}(z)\vert $. For $i = 1,\ldots,2n$, we have

$$
\norm{f_i(z)}_{u} = \sup_{x\in \real^{2n}} \vert f_i (x)\vert\leq M
$$

The standard norm that measures $\vert H(z+a) - H(z)\vert$ is equivalent to $\sup_{i\leq 2n} \vert f_i(z+a) - f_i(z)\vert$. It suffices to show

$$
\sup_{i}\vert f_i(z+a) - f_i(z)\vert\Lsim \vert a\vert 
$$

To wit, use Stokes' Theorem for $1$-forms. Let $i=1,\ldots,2n$, and $\gamma:[0,1]\to \real^{2n}$ be any smooth curve such that $\gamma(0)=z$ and $\gamma(1) = z+1$. For concreteness, set $\gamma(t) = z+ta$, and by the Fundamental Theorem

$$
f_i(z+a) - f_i(z) = \int_\gamma df_i = \int_0^1 df_i(\gamma(t))(\dot{\gamma}(t))dt
$$

By tangent-cotangent isomorphism on $\real^{2n}$, the above reads

$$
\int_\gamma df_i = \int_{[0,1]}\gamma^*df_i = \int_0^1 \langle \nabla f_i(\gamma), \nabla \gamma\rangle dt
$$

but $\nabla \gamma(t) = a$, hence 

$$
\biggl\vert\int_\gamma df_i \biggr\vert \leq \int_0^1 \vert f_i(\gamma)\cdot a\vert dt\leq \vert a\vert\cdot \norm{f_i}_{u}
$$

Therefore, 

$$
\vert f_i(z+a) - f_i(z)\vert\Lsim \vert a\vert,\:\forall i\leq 2n\implies \sup_{i\leq 2n}\vert f_i(z+a) - f_i(z)\vert\Lsim \vert a\vert
$$

and this proves the claim.
</div>


<div class="lemma-box" markdown=1>
If $x\in L^2(S^1,\real^{2n})$, then $\nabla H(x(t))\in L^2(S^1,\real^{2n})$
</div>
<div class="proof-box" markdown=1 proof-name="">
Set $z = 0$ in the previous Lemma, and $a = x(t)$ for $t\in[0,1]$, then

$$
\vert H(x)\vert\Lsim \vert x\vert\implies \norm{H(x)}_{L^2}\Lsim \norm{x}_{L^2}<+\infty
$$


</div>

<div class="lemma-box" markdown=1>
If $x$ and $h$ are in $L^2(S^1,\real^{2n})$, then $$\langle H(x(t)), \: h(t)\rangle \in L^1(S^{1},\real)$$.
</div>
<div class="proof-box" markdown=1 proof-name="">
By the previous lemma, both $\nabla H(x(t))$ and $h(t)$ are in $L^2(S^1,\real^{2n})$. Using Holder's Inequality twice yields the result.
</div>

## Hessian of $H$

<div class="lemma-box" markdown=1>
The Hessian of $H$, denoted by $H_{zz}(z)$ is uniformly bounded. There exists $M\in\real$ such that

$$
\vert H_{zz}(z)\vert \leq M,\quad\forall z\in\real^{2n}
$$


</div>
<div class="proof-box" markdown=1 proof-name="Proof of bounded Hessian:">
Computing the [Hessian]({{ site.baseurl }}/{% post_url 2023-08-11-Hessian %}) of $Q$ gives

$$
Q_{zz}(z) = 2(\pi+\varepsilon)\begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & \id{n-1}N^{-2} & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & \id{n-1}N^{-2}\end{bmatrix}
$$

All norms on finite-dimensional vector spaces are equivalent, so $\vert H_{zz}(z)\vert\leq M$ for $z\in \real^{2n}\setminus \cl{B(R)}$. On the other hand, the extreme value theorem tells us $H_{zz}$ is bounded on $\cl{B(R)}$.
</div>

# Differentiability of $b$
In this section, we will discuss and prove the properties of the map $\hat{b}: L^2\to \real$, where

$$\hat{b}(x) = \int_0^1 H(x(t)) dt\in\real$$ 

Note the integral defining $\hat{b}$ converges absolutely for $x\in L^2$ by the previous section. Furthermore, we denote the restriction of $\hat{b}$ onto $E = H^{1/2}\subseteq L^2$, by $b = \hat{b}\circ j$, where 

$$
j: H^{1/2}\to L^2\quad\text{and}\quad j^*: L^2\to H^{1/2}
$$

denote the inclusion map and the adjoint of the inclusion map respectively.

We show the [Gateaux derivative](https://en.wikipedia.org/wiki/Gateaux_derivative) of $\hat{b}$ exists in $L^2$. We then compute $d\hat{b}: L^2\to L^2$ using an isomorphism. 

Using the chain rule with the inclusion map, we also compute $db: H^{1/2}\to H^{1/2}$ and prove several regularity properties of $\nabla b$. 


<div class="lemma-box" markdown=1>
For any $z,\zeta\in\real^{2n}$,

$$
H(z+\zeta) = H(z) + \langle \nabla H(z),\zeta\rangle + \int_0^1 \langle\nabla H(z+t\zeta) - \nabla H(z),\zeta\rangle dt
$$

</div>

<div class="proof-box" markdown=1 proof-name="">
By Stokes' Theorem for $1$-forms, $\gamma: [0,1]\to\real^{2n}$, with $\gamma(t) = z + t\zeta$ is a smooth path connecting $z$ and $z + \zeta$. We obtain obtain the following: 

$$
\begin{align}
H(x+\zeta) - H(z) &= \int_\gamma dH \\
&= \int_{[0,1]} dH(\gamma(t))(\gamma'(t))dt\\
&= \int_0^1 \langle \nabla H(\gamma(t)), \gamma'(t) \rangle dt\\
&= \int_0^1 \langle \nabla H(z + t\zeta), \zeta\rangle dt
\end{align}
$$

Adding $\langle \nabla H(z),\zeta\rangle$ to both sides proves the equation. 
</div>


<div class="theorem-box" markdown=1>
$\hat{b}$ is Gateaux differentiable on $L^2$. Moreover, 

$$
d\hat{b}(x)(h) = \langle \nabla H(x),\: h\rangle_{L^2(S^{1}, \real^{2n})} = \int_0^1 \langle \nabla H(x(t)),\: h(t)\rangle_{\real^{2n}}\: dt
$$

and we define the gradient (through the natural Riesz map on $L^2$) of $\hat{b}$ to be

$$
\nabla \hat{b}(x) = \nabla H(x)
$$


</div>
<div class="proof-box" markdown=1 proof-name="">
Building upon the result of the previous lemma. Let $x$ and $h$ be in $L^2(S^1,\real^{2n})$, the following holds pointwise for each $t\in [0,1]$

$$
\begin{multline}
H(x(t)+h(t)) = H(x(t)) + \biggl\langle \nabla H(x(t)),\: h(t)\biggr\rangle \\ 
+ \int_0^1 \biggl\langle \nabla H(x(t) + yh(t)) - \nabla H(x(t)),\: h(t)\biggr\rangle dy
\end{multline}
$$


The results from the previous section tell us 

- Both $x$ and $h$ are in $L^2(S^1)$, so the integral over the first two terms converge absolutely.
- The third term is in $L^1$, and

    $$
    \begin{align}
    \biggl\vert \int_0^1 \biggl\langle  \nabla H(x(t)),\: h(t)\biggr\rangle dt \biggr\vert &\leq \int_0^1 \biggl\vert\biggl\langle  \nabla H(x(t)),\: h(t)\biggr\rangle\biggr\vert dt
    \end{align}
    $$

Furthermore, the size of last term is controlled by $\vert h(t)\vert^2$,

$$
\begin{align}
\biggl\vert \int_0^1 \biggl\langle \nabla H(x(t) + yh(t)) - \nabla H(x(t)),h(t)\biggr\rangle dy \biggr\vert &\leq \int_0^1 \vert yh(t)\vert_{\real^{2n}}\cdot\vert h(t)\vert_{\real^{2n}}dy\\ 
&= \vert h(t)\vert^2\int_0^1 y dy\\[1ex]
&\Lsim \vert h(t)\vert^2
\end{align}
$$

It follows immediately that the last term is $L^1$ with respect to the integral over $t$. As

$$
\begin{align}
\int_0^1 \biggl\vert \int_0^1 \biggl\langle \nabla H(x(t) + yh(t)) - \nabla H(x(t)),h(t)\biggr\rangle dy \biggr\vert dt 
&\Lsim \int_0^1 \vert h(t)\vert^2 dt\\[2ex]
&\Lsim \norm{h}_{L^2(S^1,\real^{2n})}^2 \\
&< +\infty
\end{align}
$$

Now, integrating over both sides of the first equation (in this proof) gives us the following in $\hat{b}$,

$$
\hat{b}(x+h) = \hat{b}(x) + \int_0^1 \langle\nabla H(x(t)),\: h(t)\rangle dt + o(\norm{h}_{L^2(S^1,\real^{2n})})
$$

see [little-o notation reference]({{ site.baseurl }}/{% post_url 2023-08-07-linking-argument %}) subsection 'Differentiation on TVS', and [Tao's post]({{ page.tao_link }}). The integral in the last equation is *precisely* the inner product of two $L^2(S^1,\real^{2n})$ functions. Therefore

$$
\hat{b}(x+h) = \hat{b}(x) + \langle \nabla H(x),\: h\rangle_{L^2} + o(\norm{h}_{L^2})
$$

since $h\mapsto \langle \nabla H(x),\: h\rangle_{L^2}$ is in $\mathcal{L}(L^2, \real)$. Therefore $\hat{b}$ is differentiable at every $x\in L^2$. 

If $$d\hat{b}: L^2\to \mathcal{L}(L^2, \real)=(L^2)^*$$ represents the Gateaux derivative, the *gradient* of $\hat{b}$ is the unique map that realizes $d\hat{b}$ through the $L^2$ product.

$$
\langle\nabla \hat{b}(x), h\rangle_{L^2} = d\hat{b}(x)(h) = \langle \nabla H(x), h\rangle_{L^2}\implies\nabla \hat{b}(x) = \nabla H(x)
$$


</div>
