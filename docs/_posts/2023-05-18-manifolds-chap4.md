---
layout: post
title: manifolds chap 4 resources
date: 2023-05-18 19:50
category: math
tags: ['math','manifolds']
---
I used Chapter 9 of Rudin's Principle of Mathematical Analysis for vector calculus. Some useful links I have found for Chapter 4 in particular.

[On the Rank Theorem](https://math.stackexchange.com/questions/2508104/rank-theorem-on-manifolds?rq=1). 

Why the open cube is necessarily for the rank theorem. (It is not, but it simplifies the proof a lot, because it is an open and convex set, and we can take the  $x$-sections across and explicitly write down an open set that contains $F(\wig{U_0})$). [Discussion here](https://math.stackexchange.com/questions/3029464/question-about-proof-of-the-rank-theorem-from-lees-smooth-manifolds)


[More on the Rank Theorem](https://math.stackexchange.com/questions/1016191/rank-theorem-proof)

Shrinking process:

- first we center charts at the origin for the domain and the range.
- complete the square for the matrix, and apply inverse function theorem, this gives another open connected subset in $\real^m$.
- we can send this subset back and take the intersection with the original chart.
- 

# Definitions


# Question.
Does anyone know why the cube is necessary for the highlighted part?

I understand why the cube was necessary (to simplify the proof) for the second time he used it but not the first time. 

If all partials of the form $\dfrac{\partial \wig{R}^k}{\partial y^j}$ for $k,j>r$ vanish identically on a connected open set, doesn't that already imply $\wig{R}^k$ is independent of the coordinates $y^j$ for $k,j>r$?

![Rank Theorem 1]({{ site.baseurl }}{% link /images/rank-theorem-1.png %})

![Rank Theorem 2]({{ site.baseurl }}{% link /images/rank-theorem-2.png %})

# Tu Tangent Spaces
Example 8.19
View matrices as $n\times n$ manifolds not as linear maps themselves. Find the basis vectors in $$T_{gI}GL(n,\real)$$ then apply the derivation to the basis vectors, leaving the coefficients unchanged. But the coeffients are exactly the ones get 'carried through' from matrix multiplication. So we pack the coefficients together, and the nice result follows. [Details here](https://math.stackexchange.com/questions/3246481/an-introduction-to-manifolds-loring-w-tu-example-8-19)