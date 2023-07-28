---
layout: post
title: compact fattenings and translations
date: 2023-07-28 19:16
tags: ['math']
summary: 
---
The following is a sequence of results obtained by reading Folland's Real Analysis, Proposition 9.3. We wish to show if $\phi\in C_c^\infty$ is a test function, and $U$ is an open set, then the set 

$$
V = \bigset{x\in\realn,\: \forall y\in\supp{\phi}\: x-y\in U}
$$

is open. 

# Fattening of Compact Sets
Let $K$ be compact and $U$ be an open neighbourhood of $K$ in the metric space $(X, d)$. Then, there exists $\varepsilon>0$ such that

$$
B_\varepsilon(K)=\bigcup_{x\in K} B_\varepsilon(x)\subseteq U
$$

*Proof:* By contradiction, let $n^{-1}>0$ induce $x_n\in K$ with $B_{n^{-1}}(x_n)\setminus U\neq\varnothing$, set $y_n\in B_{n^{-1}}\cap U^c$. After relabelling, we assume $x_n$ converges in $K$ to some $x\in K$ by sequential compactness. If $\varepsilon>0$, then pick a $n$ so large that $n^{-1}<\varepsilon 2^{-1}$, and $x_n\in B_{\varepsilon 2^{-1}}(x)$. 

We see that $y_n\in B_{n^{-1}}(x_n)\subseteq B_{\varepsilon 2^{-1}}(x_n)$, and $x_n\in B_{\varepsilon 2^{-1}}(x)$ implies $y\in B_\varepsilon(x)$ by the Triangle Inequality. Since $y\notin U$, and $\varepsilon>0$ was arbitrary, this means $x\in \partial U$ and the proof is complete.

*Corollary:* There is no smallest fattening of $K$. If $B_\varepsilon(K)\subseteq U$ is a fattening, then so is $B_{\varepsilon 2^{-1}}(K)\subseteq B_{\varepsilon}(K)\subseteq U$.

# Notes on the translation of balls
Let $B_r(x) = \{y\in X,\: d(x,y)< r\}$, then the following hold

- $B_r(x) + a = B_r(x+a)$
- $(-1)B_r(-x) = B_r(-x)$
- $x-B_r(y) = B_r(x-y)$

# Translation Lemma 1
Let $K$ be a set and $U$ be open, and suppose $x$ is a point such that the fattening $B_\varepsilon(x-K)\subseteq U$. Then $x$ admits a neighbourhood about which all points $z\in B_{\varepsilon 2^{-1}}(x)$ have fattenings $B_{\varepsilon 2^{-1}}(z-K)\subseteq U$. 

*Proof:* Suppose $z\in B_{\varepsilon 2^{-1}}(x)$, and let $y\in K$ be arbitrary. We claim $B_{\varepsilon 2^{-1}}(z-y)\subseteq U$. Indeed, if $w\in B_{\varepsilon 2^{-1}}(z-y)$, by translation invariance: $d(w,z-y) = d(w+y,z)<\varepsilon 2^{-1}$. Using the triangle inequality with $d(x,z)<\varepsilon 2^{-1}$, we see that 

$$
d(w+y, x)= d(w,x-y)<\varepsilon\implies w\in B_{\varepsilon}(x-y)\subseteq U
$$

This holds for every $w$, so $B_{\varepsilon 2^{-1}}(z-y)\subseteq B_{\varepsilon}(x-y)\subseteq U$, and since $y$ was arbitrary, $B_{\varepsilon 2^{-1}}(z-K)\subseteq U$. 

# Translation Lemma 2
Let $V = \bigset{x,\: x-y\in U,\: \forall y\in K}$ where $K$ is compact and $U$ is open. Then $V$ is open.

*Proof:* Let $x\in V$, then $x-K$ is again a compact set, since addition and scalar multiplication is continuous. So $x-K$ admits a $2\varepsilon$-fattening by the fattening lemma. And for every $z\in B_\varepsilon(x)$, Translation Lemma 1 reads 

$$
B_\varepsilon(z-K)\subseteq U\implies z-K\subseteq U
$$

and $B_{\varepsilon}(x)\subseteq V$. Therefore $V$ is open.