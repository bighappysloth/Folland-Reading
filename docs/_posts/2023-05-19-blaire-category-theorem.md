---
layout: article
title: blaire category theorem
date: 2023-05-19 22:59
category: math
tags: ['blaire category theorem','topology']
---
# Explanation for regularity, Munkres 48.2

## Statement of the Theorem
Let $\xx$ be a complete metric space, or a compact Hausdorff space, or a locally compact Hausdorff space. If $$\{A_n\}$$ is a countable sequence of closed, sets with empty interior, then its union (not-necessarily closed), has an empty interior. It suffices to show that if $U_0$ is an arbitrary non-empty open set, there exists a point $p\in U_0\setminus \bigcup A_n$. There exists a point $p$ that 'sticks out' form $U_0$, and $U_0$ cannot be a subset of the union. Since $U_0$ is arbitrary, this proves $\bigcup A_n$ has an empty interior.

## Proof

We assume $$\{A_n\}$$ is a sequence of closed sets with empty interiors in $\xx$. Let $U_0$ be any non-empty open set of $\xx$. Since $A_1$ is nowhere dense, 

$$
U_0\setminus A_1\neq\varnothing
$$

so we can pick $y\in U_0\cap A_1^c$, which is an open set. By regularity, there exists an open neighbourhood of $y$, denoted by $U_1$ that hides in $U_0$; and whose closure is disjoint from $A_1$. More precisely:

$$
y\in U_1\subseteq \cl{U_1}\subseteq U_0\cap A_1^c\implies \begin{cases}\cl{U_1}\subseteq U_0\\ \cl{U_1}\cap A_1=\varnothing\end{cases}
$$

Suppose $U_0,\ldots U_{n-1}$ have been chosen, so they are a nested sequence of sets that satisfy the finite intersection property. Since $U_{n-1}$ (the last open set that was chosen), is non-empty, we can pick another point $y\in U_{n-1}\setminus A_n\neq\varnothing$; this induces (again) a neighbourhood of $y$ such that

$$
    y\in U_{n}\subseteq\cl{U_n}\subseteq U_{n-1}\cap A_{n}^c\implies\begin{cases}\cl{U_n}\subseteq U_{n-1}\\ \cl{U_n}\cap A_n = \varnothing\end{cases}
$$

If $\xx$ is locally compact instead of compact, then we pick $U_0$ as the compact neighbourhood. Recall by Folland 4.30, compact neighbourhoods can be made as fine as any open set that wraps our initial point $y$. Thus the entire sequence of $U_0,U_1,\ldots$ would be open pre-compact sets, as their closures are subsets of the compact $U_0$. If $\xx$ is a compact Hausdorff space, then closed sets are compact, and we have nothing to prove.

If $\xx$ is a complete metric space, we demand the neighbourhoods shrink faster than a known rate that goes to $0$. See Folland Chapter 5.3 for details.


## Additional commentary
If a topological space satisfies the above property, then it is called a Blaire space, and the Blaire Category Theorem is equivalent to: if $$\{U_n\}_{n\geq 1}$$ is a countable sequence of open, dense sets of $\xx$, then $\cap U_n$ is dense in $\xx$ as well.


