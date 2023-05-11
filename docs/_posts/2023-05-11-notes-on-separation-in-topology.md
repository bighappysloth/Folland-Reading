---
layout: post
title: separation mechanisms in topology
date: 2023-05-11 14:10
category: math
tags: ['topology','hausdorff','regular','separation','normal','urysohn']
---
# Pattern
There is an interesting pattern/mechanism that keeps on reappearing. Let $U$ and $V$ be disjoint open sets. It is true that:
- $U$ does not contain any adherent point of $V$, and
- $V$ does not contain any adherent point of $U$,

Proof: Taking complements reads

$$
\underbrace{U^c}_{\text{closed set}}\supseteq V\implies U^c\supseteq \cl{V}\implies \cl{V}\cap U =\varnothing
$$

Repeating the same argument gives

$$
\begin{cases}
\cl{V}\cap U=\varnothing\\
\cl{U}\cap V = \varnothing
\end{cases}
$$

# Applications?
## Hausdorff Spaces 
Let $\xx$ be Hausdorff, and fix two points $x\neq y$. Then we can find disjoint open sets $U$ and $V$ which wrap the two points.

Moreover, the closure of $U$ does not contain $y$, neither does the closure of $V$ contain $x$.

$$
\begin{cases}
\underbrace{U}_{\text{contains }x}\cap \cl{V}=\varnothing\\
\underbrace{V}_{\text{contains }y }\cap \cl{U}=\varnothing\\
\end{cases}\implies \begin{cases}
x\notin V, & x\notin \cl{V} \\
y\notin U, & y\notin \cl{U}
\end{cases}
$$

## Regular spaces


## Normal Spaces
Let $A$ and $B$ be disjoint closed sets, and $U$ and $V$ be open separations of them. We see that

$$
\begin{cases}
A\subseteq U\subseteq \cl{U}\subseteq V^c \subseteq B^c\\
B\subseteq V\subseteq \underbrace{\cl{V}\subseteq U^c \subseteq A^c}_{\text{ focus here}}
\end{cases}
\implies \begin{cases}
A\subseteq U\subseteq\cl{U}, & \cl{U}\cap B = \varnothing\\ 
B\subseteq V\subseteq\cl{V}, & \cl{V}\cap A = \varnothing
\end{cases}, \quad {\text{even the closures are disjoint}}
$$

