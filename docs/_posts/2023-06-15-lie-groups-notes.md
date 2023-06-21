---
layout: post
title: Notes on Lie Groups
date: 2023-06-15 16:59
category: math
tags: ['math','manifold']
---
# Definition of Lie Group
Lie Group $G$ is a group which is also a smooth manifold. 

# Definition of Lie Algebra
The tangent space of $G$ at the identity, it has a bilinear operation called the *Lie Bracket*. 

$$
G\times G\to G,\quad [\cdot,\: \cdot]\mapsto \cdot
$$

This makes the tangent space at the identity, a vector space with a bilinear form. It is an Algebra. The Lie Bracket satisfies the Jacobi identity.


# Circle group
Is the group of rotation matrices in $\real^2$.

$$
G = \bigset{\begin{bmatrix} \cos(\theta) & -\sin(\theta)\\ \sin(\theta) & \cos(\theta)\end{bmatrix},\quad \theta\in\real}
$$

# Special Linear Group $SL_2$
The space if matrices with determinant $1$.

$$
\operatorname{SL}_2(\real) = \bigset{\begin{bmatrix} a & b \\ c & d \end{bmatrix},\quad ad-bc = 1}
$$

The identity element is just the identity matrix $$\begin{bmatrix}1 & 0 \\ 0 & 1\end{bmatrix}$$



# Representation of a group $G$
is a group homomorphism $\phi: G\to GL(n,\mathbb{C})$. So for every element $g\in G$, we assign it an invertible matrix.

This is (logicallly) equivalent to saying that $G$ acts on a vector space with dimension $n$. 

# Representation of a Lie algebra $\mathcal{g}$
is a Lie algebra homomorphism $\phi: \mathcal{g}\to gl(n,\mathbb{C})$.

# Matirx Lie Group
is a subgroup $G$ of $GL(n,\mathbb{C})$, and $\{A_m\}\subseteq G$, has a limit, either $A\in G$, or $A$ is not invertible. Where we define convergence entrywise. This means $G$ is a closed subgroup of $GL(n,\mathbb{C})$ but not necessarily in $\mcal_n(\mathbb{C}$)).

- $GL(n,\mathbb{Q})$ is not a matrix lie group, because 
$$
A_n = \begin{bmatrix} 1 & x_n \\ 0 & 1\end{bmatrix}
$$

where $x_n$ is any rational sequence that converges to $\sqrt{2}$. 

- What are some of the closed subgroups? $SL(n,\mathbb{C})$ is a matrix lie group, with determinant $1$. Proof: Use the continuity of the determinant.


## Left and right Translations 
Let $g\in G$, define

# Left Translation

$$
L_g: G\to G,\quad h\mapsto gh
$$

# Right Translation

$$
R_g: G\to G,\quad h\mapsto hg
$$

Remark: 

- Translations are smooth.

- Translations commute $L_{g_1}\circ R_{g_2} = R_{g_2}\circ L_{g_1}$.

- $L_g$ and $R_g$ are diffeomorphisms, because $L^{-1} = L_{g^{-1}}$. Where $L_g$ is smooth in of itself (resp. for $R_g$).

## Lie Group homomorphisms

A *Lie Group homomorphism* is a smooth map between two lie groups $G$ and $H$.

$$
    F: G\to H
$$

that is also a group homomorphism.

Examples: 
- $\operatorname{exp}: \mathbb{C}\mapsto \mathbb{C}^\*$, where we define the punctured complex plane $\mathbb{C}^\* = \mathbb{C} \setminus \{0\}$.
- $\real\to S^1$, where we map $t\mapsto e^{2\pi i t}$
- The determinant for invertible matrices (with matrix multiplication and scalar multiplication on both sides) $\det: GL(n,\real)\to \real$




# Applications of LG homomorphisms
Theorem: every lie group homomorphism has constant rank.


Applications: 
1. $SL(n,\real) = \det^{-1}(1)$ is a regular submanifold of $GL(n,\real)$. 
2. $F$ is injective / surjective / bijection $\implies$ F$ is immersion / submersion / diffeomorphism.

# Lie subgroup of $G$
$H\subseteq G$ is a *lie subgroup* if it is the image of an injective lie group homomorphism. 
- (Injective) Smooth immersion, that is also a group homomorphism.
- Most of the time we onlly care about embedded subgroups.


# Identity component
$G_0\subseteq G$ is the connected component of $G$ containing $e$. 

$G_0$ is a lie subgroup, also open.



# Read
- Universal Covering Lie Group