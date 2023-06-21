---
layout: post
title: useful latex resources
date: 2023-05-11 02:50
category: latex
tags: ['latex','workflow']
---
[This page](https://en.wikibooks.org/wiki/LaTeX/Advanced_Mathematics#Vertically_aligning_displayed_mathematics) describes the use of `underbrace/overbrace`, `gather`, `align`, `cases` and `dcases`

[This page](https://pbelmans.ncag.info/blog/2010/12/06/the-power-of-mathclap-and-substack/) explains how to use `\mathclap` and `\substack` properly to sequeeze the indices of operators.

## Packages
- [physics](https://ctan.org/pkg/physics): Automatic delimter sizing, 'evaluated at bar' for derivatives, spacing for differentials 
- [physics2](https://ctan.org/pkg/physics2)
- [amsmath documentation](https://mirror.quantum5.ca/CTAN/macros/latex/required/amsmath/amsldoc.pdf)


# Matrices
[This page](https://en.wikibooks.org/wiki/LaTeX/Advanced_Mathematics#Limits) discusses spacing for and matrices.
$$
    Mz = \Biggl[_{\substack{\\[2ex] {a+c\text{ rows}}}}\overbrace{\begin{bmatrix}
        \begin{array}{c|c}
            A & B \\
            \hline
            C & D \\
        \end{array}
    \end{bmatrix}}^{a+b \text{ columns}}z = \begin{bmatrix}
        \begin{array}{c|c}
            A & B \\
            \hline
            C & D \\
        \end{array}
    \end{bmatrix}\begin{bmatrix}
        x\\ y
    \end{bmatrix}  
$$

{% highlight latex %}
    \[
        Mz = \Biggl[_{\mathclap{\substack{\\[2ex] {a+c\text{ rows}}}}}\overbracket{\begin{bmatrix}
            \begin{array}{c|c}
                A & B \\
                \hline
                C & D \\
            \end{array}
        \end{bmatrix}}^{a+b \text{ columns}}z = \begin{bmatrix}
            \begin{array}{c|c}
                A & B \\
                \hline
                C & D \\
            \end{array}
        \end{bmatrix}\begin{bmatrix}
            x\\ y
        \end{bmatrix}
    \]
{% endhighlight %}

# Multi-part proofs

{% highlight latex %}
\begin{wts}[Properties of Groups (Hungerford: Theorem 1.2)]\label{hungerford-chp1:theorem-1.2}
    Let $G$ be a group with identity $e$, which is unique by \cref{hungerford-chp1:monoid-unique-identity}. Then
    \begin{enumroman}
        \item $c\in G$ and $cc=c$ implies $c=e$. 
        
        \item Left/Right cancellation: 
        \[
            \begin{cases}
                ab=ac\implies b=c\\
                ba=ca\implies b=c
            \end{cases}
        \]
        
        \item If $a\in G$, its two-sided inverse is unique. 
        
        \item Let $a\in G$, then the inverse of its two-sided inverse (uniqueness guaranteed by iii), is $a$ itself; or $(a^{-1})^{-1}=a$.
        
        \item If $a,b\in G$, then the following equations in $x,y$ admit unique solutions
        \[
            \begin{cases}
                ax=b\\
                ya=b
            \end{cases}
        \]
    \end{enumroman}
\end{wts}
\begin{proof}[Proof of \Cref{hungerford-chp1:theorem-1.2}]
    \begin{enumerate}[label={Proof of Part (\roman*): },leftmargin=*]
        \item[]
        \item \[cc=c\implies (cc)c^{-1}=cc^{-1}\implies c(cc^{-1})=e\implies ce=c=e\]
        \item First claim:
            \begin{multline*}
                ab=ac\implies a^{-1}(ab)=a^{-1}(ac)\\
                \implies (a^{-1}a)b=(a^{-1}a)c\implies eb=ec\implies b=c
            \end{multline*}
            Second claim is the same, just cancel from the right using $aa^{-1}=e$ and associativity.
        \item Suppose $b$ and $c$ are two-sided inverse for $a$, it follows from Part ii that 
        \[
            ab=ac\implies b=c=a^{-1}
        \]
        \item From Part iii, the two-sided inverses of group elements exist and are unique, and $a^{-1}a=aa^{-1}$ so $a$ is an inverse for $a^{-1}$, and it is the only inverse.
        \item First equation: write $ax=b=a(a^{-1}b)$, left-cancelling reads $x=a^{-1}b$, uniqueness follows from Part ii. Second equation is similar.
    \end{enumerate}
\end{proof}
{% endhighlight %}