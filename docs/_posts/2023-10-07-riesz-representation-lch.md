---
layout: article
title: Riesz Representation on LCH
date: 2023-10-07 17:08
category: math
author: 
tags: ['analysis','lch','partitions of unity']
summary: 
---
# Introduction
Will follow Follland's text closely.

## Topological preliminaries
<div class="remark-box" markdown=1 name="Neighbourhood are not necessarily open">
In our discussions hereinafter, we do not assume neighbourhoods are open sets. If $\xx$ is a topological space, and $U$ a subset of $\xx$.
- $p\oin U$ = $p\in U^o$ = $U$ is a neighbourhood of $p$.
- $A\osub U$ = $A\subseteq U^o$ = $U$ is a neighbourhood of $A$
- $U\osub \xx$ = $U$ is open in $\xx$. (not to be confused with the previous bullet point).
</div>
The space $C(\xx)$ will denote the complex-valued, continuous functions on $\xx$, and $C_c(\xx)$ is a subset of $C(\xx)$ whose elements have compact supports. Some more terminology: let $A, B, E$ be subsets of $\xx$, and $f$ a real valued function on $\xx$.
- $A$ **hides** in $B$ = $\cl{A}\subseteq B$.
- $f\precsim E$ = $f\in C(\xx,[0,1])$ and $\supp{f}\subseteq E$.
- $f\precsim_c E$ = $f\precsim E$ and $f\in C_c$.
<div class="definition-box" markdown=1 name="Locally finite">
Let $\yy$ be a topological space. A family of subsets $$\{E_{\alpha}\}$$ is **locally finite** if every point $p\in \yy$ admits a neighbourhood $V_{\beta}$ that intersects finitely many members of $E_{\alpha}$. In symbols

\begin{equation}
V_{\beta}\cap \bigcup E_{\alpha} = \bigcup^\wedge V_{\beta}\cap E_{\alpha}
\label{eq:locally-finite-subsets}
\end{equation}
</div>

Refer to [here]({{ site.baseurl }}/{% post_url 2023-05-10-munkres-chap-39-42 %}) for more on paracompactness/locally finite families.

<div class="definition-box" markdown=1 name="Partition of unity">
Let $$\{U_{\alpha}\}$$ be an open cover of $\xx$. A family of real-valued, continuous functions $$\{w_{\alpha}\}$$ is called a **partition of unity subordinate to $$\{U_{\alpha}\}$$** if all of the following hold. 

- $w_{\alpha}\in C_c(\xx,[0,1])$ for every $\alpha$.
- $\supp{w_{\alpha}}\subseteq U_{\alpha}$ for every $\alpha$.
- The family of supports of $\{w_{\alpha}\}$ is locally finite: at every $p\in \yy$, there exists a neighbourhood $V_{\beta}$ about $p$ such that 
    \begin{equation}
    V_{\beta}\cap \bigcup \supp{w_{\alpha}} = \bigcup^{\wedge} V_{\beta}\cap \supp{w_{\alpha}}
    \label{eq:locally-finite-partitions-of-unity}
    \end{equation}
- The sum over all $w_{\alpha}$ is the constant function $1$: $\sum w_{\alpha} \equiv 1$.

</div>


## Definitions
In this section, we fix $\xx$ as a LCH topological space with Borel $\sigma$-algebra $\mcal$. 

<div class="definition-box" markdown=1 name="Positive linear functional">
A **positive linear functional** on $C_c(\xx)$ is a linear functional (not necessarily continuous) such that if $f\in C_c(\xx)$ and $f\geq 0$, then $I(f)\geq 0$.
</div>



## Outermeasure proof

![]({{ site.baseurl }}{% link /images/riesz-folland-2.jpg %})
![]({{ site.baseurl }}{% link /images/riesz-folland-3.jpg %})
![]({{ site.baseurl }}{% link /images/riesz-folland-4.jpg %})
![]({{ site.baseurl }}{% link /images/riesz-folland-5.jpg %})
![]({{ site.baseurl }}{% link /images/riesz-folland-6.jpg %})