---
layout: post
title: normed balls
date: 2023-05-19 17:44
category: math
tags: ['normed vector spaces']
---
# Notation
Throughout this post, $\xx$ and $\yy$ will denote normed vector spaces, and $L(\xx,\yy)$ refers to the vector space of bounded linear maps from $\xx$ to $\yy$.

# Translations and dilations are homeomorphisms
Proof: Let $f:\xx\to\xx$, with $x\mapsto x + a$,w here $a\in\xx$ as well. It is clear that $f$ is a bijection with inverse $f^{-1}(x) = x-a$. To show $f$ is continuous, fix $x$ and $y\in \xx$, then

$$
\norm{f(x)-f(y)} = \norm{x-y}\to 0\quad\text{as }\norm{x-y}\to 0 
$$

$f$ is an open map as well, simply replace $a$ with $-a$ and repeat the argument. 

Let $g:\xx\to\xx$ be a dilation, for $\norm{a}\neq 0$, $a\in\mathbb{C}$, $x\mapsto ax$. $g$ is a bounded linear map with $$\norm{g}=\norm{a}$$, and $g^{-1}\in L(\xx,\xx)$ with 

$$\norm{g^{-1}}=\norm{a^{-1}}$$

So $g$ is a homeomorphism.


# Induced metric is continuous
Let $x\in \xx$, and define a function $f$ that measures how far points are away from $x$.

$$
f:\xx\to\real,\quad f(y) = \norm{x-y}
$$

Let $z_1$ and $z_2$ be points in $\xx$, by the Triangle inequality:

$$
\norm{f(z_1) - f(z_2)} \leq \norm{z_1 - z_2}\to 0
$$

# Estimate concerning normed balls.
The following is a useful estimate,

$$
    \underbrace{\cl{\bigset{y,\in\xx,\: d(x,y)<r}}}_{=\cl{B}}\subseteq \underbrace{\bigset{y\in \xx,\: d(x,y)\leq r}}_{=W}
$$

The reverse inclusion does not hold if we consider the discrete topology on $$ [0,1] $$. It suffices to show $W$ is closed. Let $f(y) = \norm{x-y}$, since $f$ is continuous, and 

$$
W^c = f^{-1}(r,+\infty)
$$

$W$ is a closed set containing $B$, hence it contains its closure.

