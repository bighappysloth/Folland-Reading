---
layout: article
title: Calculations with piecewise functions
date: 2023-10-11 02:47
category: math
author: 
tags: ['arithmetic','shortcuts']
summary: 
---
# Introduction
This post will contain a collection of very computational results. Recall, we can write 

\begin{equation}
\max(x,y) = \dfrac{x + y + \vert x-y\vert}{2}
\label{eq:max}
\end{equation}

and 

\begin{equation}
\min(x,y) = \dfrac{x + y - \vert x-y\vert}{2}
\label{eq:min}
\end{equation}

one can interpret \eqref{eq:max} and \eqref{eq:min} as subtracting the 'radius' of the ball centered at the midpoint between $x,y$. We also define the signum function of a real number in \eqref{eq:signum}.

\begin{equation}
\sgn(x) = \vert x \vert x^{-1} \quad \forall x\neq 0\quad\text{and}\quad \sgn(0)=0
\label{eq:signum}
\end{equation}

## Equations

We can tap into our supremum/infimum muscle, and it is not hard to see that

<div class="lemma-box" markdown=1 name="">
Let $x,y,a\in\real$, then the following equations hold.

$$
\begin{align}
\max(x,y) &= \max(x-a,y-a)+a\\ 
\min(x,y) &= \min(x-a,y-a)+a\\ 
\max(x,y) &= (-1)\min(-x,-y)\\ 
\min(x,y) &= (-1)\max(-x,-y)
\end{align}
$$

</div>

An interesting application: we can model the diode with a constant voltage drop at $a\in\real$ by $\max(x-a,0)$. It is clear that $\max$ and $\min$ are continuous with respect to the product topology. A simple argument by contrapositive will show that it is impossible to write the unit step using compositions of $\max$, $\min$ (in fact they are interchangable), subtraction, addition, and the identity map $f(x) = x$.

<div class="remark-box" markdown=1 name="label">
We can produce a triangle jigsaw pattern by writing $x - floor(x)$. The floor function can be written as a pointwise sum of 

\begin{equation}
floor(x) = \frac{1}{4}\sum_{j\geq 1}\biggl(x-j + \vert x-j\vert+ 2\biggr) - \frac{1}{4}\vert x - 1\vert
\label{eq:floor-function}
\end{equation}

For every finite $x$, all but finitely many terms in \eqref{eq:floor-function} vanish. We will discuss the convergence properties of the sum in \eqref{eq:floor-function} at a later dtae.
</div>

## Piecewise ramps


## Integral of signum function
Let $a\leq b$, the closed form to the integral $\int_a^b\sgn(x)dx$ is given by \eqref{eq:signum-integral-value}.

\begin{equation}
\int_a^b\sgn(x)dx = \frac{1}{2}(b-a)[\sgn(a) + \sgn(b)] + \frac{1}{4}(b+a)[\sgn{b}+1][1-\sgn{a}]
\label{eq:signum-integral-value}
\end{equation}

The proof is shown below.

![]({{ site.baseurl }}{% link /images/signum-integral-proof.png %})


## Step function quantizer
Let $a\leq b$, and we define $g_{a,b}(x) =\max(\min(x-a,0), b-a)$. We obtain the [graph shown here](https://www.desmos.com/calculator/gnkbswheum). 

We can produce a 3-piecewise ramp function using the same $\max\min$ composition [shown here](https://www.desmos.com/calculator/1ewgezs0fz)

\begin{equation}
\min(\max(x-a_1,0),a_2) + \min(\max(x-a_3,0),a_4) - a_4
\label{eq:max-min-composition}
\end{equation}

for suitable scalars $a_i$ for $i = \underline{4}$

# Affine mappings of bounded sets
Let $K$ be bounded in a Banach space $E$, and $x\in E$ is non-zero, then 
$$
    a\vert {x}\vert \leq \vert{x + K}\vert \leq b\vert{x}\vert,
$$
in other words: 

$$
a\vert{x}\vert\leq\inf_{y\in K}\vert{x+y}\vert\leq\sup_{y\in K}\vert{x+y}\vert\leq b\vert{x}\vert.
$$


