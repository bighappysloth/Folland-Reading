---
layout: article
title: Probability 1
date: 2023-10-09 11:19
category: probability
author: 
tags: []
summary: 
---
# Introduction
Not sure if I will ever write a complete set of notes on probability. But I will record the proofs that are interesting/admit simplifications. We will follow Klenke's text, and I will try to simplify the proofs as much as possible.

## Basic Measure Theory
Some terminology we will use,
- FDU = finite disjoint union
- $\nat$DU = countable disjoint union
- List notation, see the Introduction section of [my notes on Banach spaces]({{ site.baseurl }}{% link /download/Calculus-on-Banach-Spaces-Compiled.pdf %}).
- $\sum^\wedge x_i$ denotes a finite sum indexed by $i$,
- $\sum x_{\underline{k}} = \sum_{i=1}^k x_i$,

We define the following families of subsets of $X\neq\varnothing$. 
- Elementary Family = $(\varnothing,\cap,\text{complements are FDU})$ ,
- Semiring = $(\varnothing,\cap,\text{differences are FDU})$,
- Ring = $(\varnothing,\setminus,\cup)$,
- $\sigma$-ring = $(\varnothing,\setminus,\sigma\cup)$,
- Algebra = $(X,\setminus,\cup)$,
- $\sigma$-algebra = $(X,\setminus, \sigma\cup)$,
- $\lambda$ system = $(\varnothing, B\setminus A \text{ whenever }B\supseteq A, \text{every }\nat DU)$.
<div class="theorem-box" markdown=1 name="Lemma 1.31">
If $\mcal$ is a semiring = $(\varnothing,\cap, \text{differences are FDU})$, and $\mu$ a content on $\mcal$ (meaning $\mu\geq 0$, finite additivity and $\varnothing\mapsto 0$), then

{% comment %} ITEMIZE PLACEHOLDER {% endcomment %}
- $\mu$ is monotonic, and 
- $\mu$ is finitely subadditive.
{% comment %} ITEMIZE PLACEHOLDER END {% endcomment %}

</div>

<div class="proof-box" markdown=1 name="">
Fix two members in $\mcal$, $A\subseteq B$ we know that $B\setminus A = FDU(E_i)$, a simple calculation shows (even though $B\setminus A$ is not necessarily in $\mcal$)
\begin{equation}
\mu(B) = \mu(B\cap A) + \sum^\wedge \mu(E_i) \geq \mu(A)
\label{eq:monotonic-calculation-1}
\end{equation}
Before proving the next claim, we prove a small equation. Suppose $A,B$ are members of $\mcal$, and $B\setminus A = FDU(E_i)$, then \ref{eq:subadditivity-calculation-lemma} holds.

\begin{equation}
\mu(B)\geq \sum^{\wedge} \mu(E_i)
\label{eq:subadditivity-calculation-lemma}
\end{equation}

This is easy to show, since $B = FDU((E_i), A\cap B)$ implies $\mu(B) = \sum^\wedge \mu(E_i) +\mu(A\cap B)$.

Suppose $A_{\underline{k}}\in\mcal$, and $B\subseteq\cup A_{\underline{k}}$, $B\in\mcal$. It suffices to show $\mu(B)\leq\sum^{\wedge}\mu(A_{\underline{k}})$. We will break $B$ into finite disjoint unions as follows. Notice $B = \cup A_{\underline{k}}\cap B$, where each member in the union is guaranteed to be in $\mcal$. For $$i = 1+\underline{k-1}$$, we write \eqref{eq:subadditivity-calculation-1}

\begin{equation}
A_i\setminus \biggl(\cup A_{\underline{i-1}}\biggr) = \cap (A_{i}\setminus A_{\underline{i-1}})
\label{eq:subadditivity-calculation-1}
\end{equation}

Denote set in \eqref{eq:subadditivity-calculation-1} by $FDU(E_i) = (\varepsilon_i)$, because it is the intersection of FDU of elements in $\mcal$, which is again a FDU. $(\varepsilon_i)$ should be interpreted as a set of subsets. We sometimes allow ourselves to write $\mu(\varepsilon_i\cap B) = \sum^\wedge \mu(E_i\cap B)$. Notice \eqref{eq:subadditivity-calculation-1} breaks the union into disjoint pieces, with the first 'piece' being $A_1\in\mcal$. And, $\cup A_{\underline{k}} = FDU_i(\varepsilon_i) + A_1$. Set $\varepsilon_1 = A_1$, which again: represents the first piece of the FDU. By \eqref{eq:subadditivity-calculation-lemma}

$$
\mu(B) = \sum^\wedge \mu(\varepsilon_i\cap B) \leq \sum^\wedge\mu(\varepsilon_i) \leq \sum \mu(A_{\underline{k}})
$$

</div>

## Convergence in measure?
Let $f_n$ be a measurable sequence of functions, we say $f_n\to f$ in measure if: for every $\varepsilon>0$ the set $\mu(\vert f_n - f\vert \geq \varepsilon)\to 0$.