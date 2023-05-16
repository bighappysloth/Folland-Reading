---
layout: post
title: notes on compactness
date: 2023-05-15 15:46
category: math
---
Compactness by itself kinda means nothing, it has to be tied to some additional structure.

In most cases you'l see compactness in Hausdorff spaces, which means a couple things:

Ordinarily, if you have a continuous function $f:\xx\to\yy$, where $\xx$ and $\yy$ are any topological spaces, one cannot deduce any topological information from $\xx$ into $\yy$.

But if $\yy$ is Hausdorff, and $\xx$ is compact, then 

$f(\xx)$ is compact, and it maps closed sets into closed sets. If $f$ is a bijection, then you a very nice homeomorphism for free essentially.

Compactness is quite abundant, closed balls in $\realn$ are compact, and in any finite dimensional vector space (see chapter on Local compactness).


That aside, 'compactness' allows you to extend 'local' properties, to 'global' properties.

Example: if $f$ is a continuous function between metric spaces $\xx$ and $\yy$, where $\xx$ is compact, then continuity (a local phenomenon) extends to a global property through compactness.