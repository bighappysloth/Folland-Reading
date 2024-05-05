---
layout: article
title: limit approximations
date: 2024-05-05 17:11
category: 
author: 
tags: []
summary: 
---
# Cauchy Sequences and Upper Limits
<div class="theorem-box" markdown=1 name="Characterization fo Cauchy Sequences">
Let $f: X\times X\to\real$ with $(x_m)$ and $(y_n)\subseteq X$, suppose that $\lim_{N\to\infty}\sup_{\min(m,n)\geq N}\vert f(x_m, y_n)\vert = 0$, then 

$$
\limsup_{m\to\infty}\limsup_{n\to\infty}\vert f(x_m, y_n)\vert = 0 = \limsup_{n\to\infty}\limsup_{m\to\infty} \vert f(x_m, y_n)\vert
$$

</div>
<div class="proof-box" markdown=1 name="Proof">
The proof is pretty easy. To each $\varepsilon>0$ we obtain $N_\varepsilon\geq 1$ such that 

$$
\vert f(x_m, y_n)\vert \leq \varepsilon\quad\forall m,n\geq N_{\varepsilon}
$$
We can take the supremum over $n$, which gives

$$
\limsup_n \vert f\vert \leq \sup_{n\geq N_{\varepsilon}}\vert f\vert \leq \varepsilon\quad\forall m\geq N_{\varepsilon}
$$

Repeating the same argument proves the first equality, and swapping the roles of $m$ and $n$ gives the second.
</div>
<div class="theorem-box" markdown=1 name="Uniform Convergence">
Let $(f_n)\subseteq BC(X,\mathbb{C})$ be a uniformly Cauchy sequence, then there exists $f\in BC(X)$ such that $f_n \to f$ in $\norm{\cdot}_u$.
</div>
<div class="proof-box" markdown=1 name="Proof">
By completeness of the codomain, let $f(x) = \lim f_n(x)$. We first show that $f_n\to f$ uniformly, $f\in B(X)$, then $f\in BC(X)$ follows because $BC(X)$ is closed in $B(X)$.

Fix $x\in X$, by continuity of the norm in $\mathbb{C}$, the quantity $\vert f_n(x) - f(x)\vert$ is the limit of $\vert f_n(x) - f_m(x)\vert$ as $m$ tends to infinity. Hence 

$$
\abs{f_n(x) - f(x)} \leq \liminf_{m\to\infty} \abs{f_n(x) - f_m(x)}\leq\liminf_{m\to\infty}\norm{f_n - f_m}_u
$$

This holds for all $x\in X$, so that $$\norm{f_n - f}_u\leq \liminf_{m\to\infty}\norm{f_n - f_m}_u$$. It is also easy to see that $f\in B(X)$, because 

$$
\norm{f}_u\leq\liminf_{m\to\infty}\norm{f_n-f_m}_u + \norm{f_n}_u.
$$

Using the Cauchy Characterization: we see that 

$$\limsup_{n\to\infty}\norm{f_n - f}_u\leq \limsup_{n\to\infty}\limsup_{m\to\infty}\norm{f_n - f_m}_{u}=0
$$ 

and the proof is complete.
</div>

# Triangle Inequality
Let $(X,d)$ be a metric space, the distance function $d$ must satisfy the triangle inequality, that is:

$$
d(x_1, x_2) \leq d(x_1, z) + d(x_2, z)\quad\forall x_1, x_2, z\in X.
$$

<div class="theorem-box" markdown=1 name="Boosted Triangle Inequality">
Let $(X,d)$ be a metric space, for all $x_1, x_2, z_1, z_2\in X$, 

$$
\biggl\vert d(x_1, z_1) - d(x_2, z_2)\biggr\vert\leq d(x_1, z_1) + d(x_2, z_2).
$$

</div>
<div class="proof-box" markdown=1 name="Proof of Boosted Triangle Inequality">
Recall that $\abs{a} = \max(a,-a)$, it suffices to show that $d(x_1, z_1) - d(x_2, z_2)$ is bounded above by the sum of distances because we can replace $x_1$ with $x_2$ and $z_1$ with $z_2$ to obtain the desired estimate. By adding and subtracting a factor of $d(x_1, z_2)$ and using the triangle-lipschitz inequality twice, 

$$
d(x_1, z_1) - d(x_2, z_2) \pm d(x_1, z_2) \leq \biggl[d(x_1, z_1) - d(x_1, z_2)\biggr] + \biggl[d(x_1, z_2) - d(x_2, z_2)\biggr]
$$

the absolute values of two squared terms on the right hand side are controlled by $d(z_1, z_2)$ and $d(x_1, z_2)$ respectively, in symbols:

$$
\abs{d(x_1, z_1) - d(x_1, z_2)}\leq d(z_1, z_2)\quad\text{and}\quad \abs{d(x_1, z_2) - d(x_2, z_2)}\leq d(x_1, x_2)
$$

Combining the last two estimates finishes the proof.
</div>
<div class="theorem-box" markdown=1 name="Continuity of Maximum, Minimum">
Let $x_1, x_2, z_1, z_2\in\real$, then 

$$
\biggl\vert\max(\abs{x_1}, \abs{z_1}) - \max(\abs{x_2}, \abs{z_2})\biggr\vert \leq \abs{x_1 - x_2} + \abs{z_1 - z_2},
$$

the same estimate holds for $\max$ replaced with $\min$. This means that we can estimate the difference of maxima (resp. minima) by comparing 'coordinate-wise'.
</div>
<div class="proof-box" markdown=1 name="Proof of Continutiy of Maximum, Mininimum">
Use the boosted triangle inequality and expand max, min using absolute values.
</div>

## Estimating bilinear differences
<div class="theorem-box" markdown=1 name="Estimating bilinear differences">
Let $X,Y,Z$ be normed vector spaces and $\varphi: X\times Y\to Z$ be continuous and bilinear, meaning there exists some $\abs{\varphi}\in[0,+\infty)$ where 

$$
\abs{\varphi(x,y)}\leq\abs{\varphi}\norm{x}\norm{y}.
$$

Then, there exists some $C \geq 0$ such that 

$$
\abs{\varphi(x,y) - \varphi(x', y')}\leq C\left( \norm{x - x'} + \norm{y - y'}\right),
$$

where $C = \abs{\varphi}\max(\norm{x},\norm{x'},\norm{y},\norm{y'})$ works.
</div>
<div class="proof-box" markdown=1 name="Proof of estimating bilinear differences">
The proof is quite creative, we can write the difference using an operator matrix, in the case of Banach space where $\varphi$ is the evaluation map, and $y$, $y'$ are functionals $T_1, T_2$, and $$x, x' = x_1, x_2$$, then 

$$
\langle T_1, x_1\rangle - \langle T_2, x_2\rangle\cong\begin{bmatrix}
1 & 0 \\
0 & -1
\end{bmatrix} = \begin{bmatrix} 1 & -1 \\ 0 & 0 \end{bmatrix} + \begin{bmatrix} 0 & 1 \\ 0 & -1\end{bmatrix}\cong \langle T_1, x_1-x_2\rangle + \langle T_1 - T_2, x_2\rangle.
$$

Similarly, we can write

$$
\langle T_1, x_1\rangle - \langle T_2, x_2\rangle\cong\begin{bmatrix}
1 & 0 \\
0 & -1
\end{bmatrix} = \begin{bmatrix} 1 & 0 \\ -1 & 0 \end{bmatrix} + \begin{bmatrix} 0 & 0 \\ 1 & -1\end{bmatrix}\cong \langle T_1-T_2, x_1\rangle + \langle T_2, x_1 - x_2\rangle.
$$

Which gives the desired result, a similar argument proves the general case. One can find a generalized verison of this in my notes.
</div>
