---
layout: article
title: Determinant Formula
date: 2023-08-03 03:33
category: 
author: 
tags: ['symplectic']
summary: 
---

#### Lemma (Determinant Formula)
Let $x=(x_1,\ldots ,x_{2n})$ and $y=(y_1,\ldots,y_{2n})$, and denote the standard basis of $\real^{2n}$ by $(e_1,\ldots ,e_{2n})$, so that

$$
\begin{cases}x=\sum_{j=1}^n x_je_j + x_{n+j}e_{n+j}\\ y=\sum_{j=1}^n y_je_j + y_{n+j}e_{n+j}\end{cases}\implies \begin{cases}Jx=\sum_{j=1}^n x_{n+j}e_j - x_{j}e_{n+j}\\ Jy=\sum_{j=1}^n y_{n+j}e_j - y_{j}e_{n+j}\end{cases}
$$

Expanding the inner product, and indexing the sum in $x$ by $j$ and the sum in $y$ by $k$,

$$
\begin{align}
\langle -J\dot{x},y\rangle &= \sum_{j=1}^n\sum_{k=1}^n\biggl\langle -\dot{x}_{n+j}e_{j} + \dot{x}_je_{n+j},\: y_ke_k + y_{n+k}e_{n+k}\biggr\rangle \\
&= \sum_{j,k=1}^n\langle-\dot{x}_{n+j}e_j,y_{k}e_{k}\rangle + \langle-\dot{x}_{n+j}e_j,y_{n+k}e_{n+k}\rangle + \langle\dot{x}_{j}e_{n+j},y_{k}e_{k}\rangle + \langle\dot{x}_{j}e_{n+j},y_{n+k}e_{n+k}\rangle\\
&= \sum_{j=1}^n -\dot{x}_{n+j}y_k + \dot{x}_jy_{n+k}\\
&= \sum_{j=1}^n \det\biggl(\begin{bmatrix}\dot{x}_{j} & y_j\\ \dot{x}_{n+j} & y_{n+j}\end{bmatrix}\biggr)
\end{align}
$$ 

