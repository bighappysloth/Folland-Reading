---
layout: post
title: vector calculus
date: 2023-05-11 19:20
category: math
tags: ['vector calculus']
---
Will be reading from Folland's Advanced Calculus. Never took vector calculus before now I need it for manifolds.

Will list the different notions of differentiability

# single variable $f: U\to\real$
$f$ is differentiable at $a\in U$, where $U$ is open (more on this later), if there exists a $m\in\real$, st

$$
    \lim_{h\to 0}\dfrac{\overbrace{f(a+h) - f(a) - mh}^{\real^1}}{\underbrace{h}_{\real^1}} = 0
$$

$U$ is required to be open for the limit, 'directed by reverse inclusion of open balls about $a$' to make sense.

If $f$ is differentiable, it is permissible to write; at least for some small $h$

$$
    \underbrace{f(a+h)}_{\text{shifted by }h} = f(a) + mh + \underbrace{E(h)}_{\real^1}
$$

where $E(h)=o(h)$ means $\lim_{h\to 0}\dfrac{E(h)}{h}$

# parametrized curve $f: \underbrace{U}_{\real^1}\to\real^m$
in this case, $f$ is called differentaible at $a$, (as usual $f$ has to be defined in some nbhd of $a$), if

$$
f'(a) = \lim_{h\to 0}\dfrac{\overbrace{f(a+h)-f(a)}^{\real^m}}{\underbrace{h}_{\real^1}}\text{ exists}
$$

the scaling in the denominator is fine because $\real^m$ is a vector space over the field $\real$.

because $\real^m$ is endowed with the product topology, the the above limit exists, iff the limit converges for all components. more precisely, let $\pi_j$ be the usual coordinate map, for $1\leq j\leq m$, then

$$
f'(a) = \bigbrackets{\dfrac{d}{dt}\underbrace{\pi_1 f(t)}_{\text{scalar function}}\biggr|_{t=a},\:\ldots\ldots\:,\dfrac{d}{dt}\pi_m f(t)\biggr|_{t=a}}
$$

perhaps more compactly, if $f_j = \pi_j f$, then 

$$
    f'(a) = \bigbrackets{f'_1(a),\:\ldots\ldots\:,f'_m(a)}
$$

# partial derivatives $f:\realn\to\real^m$
let $a$ be contained in some ball where $f$ is defined, then the partial derivative at the $j$-th component

$$
    \partial_j f(a) = \lim_{h\to 0}\dfrac{ \overbrace{f(a+he_j)-f(a)}^{\real^m} }{\underbrace{h}_{\real^1}}
$$

again, the denominator makes sense, (we are not dividing by vectors).


# multivariate $f:\realn\to\real^m$
Let us warm up to the previous notions of a derivative, if $f$ is differentiable, there exists a quantity $mh$ we can add on top of the numerator st the limit of the difference quotient vanishes. and we call the derivative at the point $a$, $m$.

The linear approximation $l:\realn\to\realm$, $l(x) = b + Mx$, where $M\in\real^{m\times n}$ is a linear map  (or a matrix), st 

- $l(a) = f(a)$, the approximation to be exact, this forces $l(x) = f(a) + M(x-a)$, and
- The difference quotient must converge to $0$

$$
\dfrac{\norm{f(x) - l(x)}}{\norm{x-a}}\to 0,\: \text{ as }x\to a

$$

We denote the derivative of $f$ at $a$ by $D_af(x)$, which is just a matrix. The subscript $a$ emphasizes its dependence 'at the point $a$'

$$
\dfrac{\norm{f(x) - D_af(x)}}{\norm{x-a}}\to 0,\: \text{ as }x\to a
$$

special case when $m=1$, we have:

$$D_af=\nabla f(a)$$, if we consider $D_af$ as a matrix entrywise, then

$$
D_af = \begin{bmatrix}
\nabla f_1(a)\\
\nabla f_2(a)\\
\vdots\\
\nabla f_m(a)
\end{bmatrix} = \begin{bmatrix}
\partial f_1/\partial x_1 & \partial f_1/\partial x_2 & \cdots & \partial f_1/\partial x_n\\
\partial f_2/\partial x_1 & \partial f_2/\partial x_2 & \cdots & \partial f_2/\partial x_n\\
\vdots & \vdots & \vdots & \vdots \\
\partial f_n/\partial x_1 & \partial f_n/\partial x_2 & \cdots & \partial f_n/\partial x_n\\
\end{bmatrix}
$$

# Chain Rule
Let $f$ $g$ be differentiable in an open set containing everything everything below, so that it maeks sense, then the product $h = f\circ g$ is differentiable at $a$.

$$
Dh(a) = Df(g(a))Dg(a)
$$


# Implicit function theorem
[Wiki page](https://en.wikipedia.org/wiki/Implicit_function_theorem)


# Some vector calculus identities
[First Derivative Identities](https://en.wikipedia.org/wiki/Vector_calculus_identities#First_derivative_identities)

[Differential Algebra](https://en.wikipedia.org/wiki/Derivation_(differential_algebra))
