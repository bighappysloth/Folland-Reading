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

\begin{remark}
We can produce a triangle jigsaw pattern by writing $x - floor(x)$.
\end{remark}

The usual step function quantizer can be written as:


