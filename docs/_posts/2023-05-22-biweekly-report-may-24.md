---
layout: post
title: Biweekly Report
date: 2023-05-22 13:51
category: report
tags: ['research project']
---
# Week 0: Topology
Book: Folland Real Analysis Chapter 4.1-4.7
- Topological Spaces, Continuity and weak topologies, Product topology, LCH spaces, pointwise/uniform/compact convergence, exhaustion by compact sets, 
- Arzela Ascoli (I, II), compatifications.
- Tychonoff, Stone Weierstrass,
- $\ccinf$ Urysohn's Lemma

# Week 1: Topology
Book: Munkres Topology (2ed)
- Chapter 2: Topological Spaces, Basis, Order Topology, Subspace, Product, Quotient, Metric Topologies.
- Chapter 3: Connectedness, path connectedness, and their components. Compactness, local compactness.
- Chapter 4: Countability axioms, and separation axioms (T0 - T4). Urysohn's Lemma, Urysohn's Metrization Theorem, Tietze Extension Theorem
- Chapter 6: Local Finiteness, Nagata metrization theorem. paracompactness, another Smirnov metrization theorem. 
- Partitions of Unity in three flavours: $C(\xx,[0,1])$, $C^\infty(\xx,[0,1])$, and $C_c^\infty(\xx,[0,1])$

Chapter 6 contains some of the more interesting proofs in the book.

# Week 2: Manifolds
Book: Folland Advanced Calculus 
- Fretchet derivative, partials, curves, multivariate formulas, series expansion with remainder

Book: Rudin Principles of Mathematical Analysis
- Chapter 5,9: Mean value theorem for vector-valued functions, Inverse Function Theorem, Implicit Function Theorem, Rank Theorem

Book: Lee Introduction to Smooth Manifolds
- Chapter 1: Topological Manifolds, coordinate charts, manifolds with boundary, smooth manifolds, transition maps, connectedness, basis for topological manifolds
- Chapter 2: Smooth maps, test functions, partitions of unity.
- Chapter 3: Tangent spaces, derivations as a vector space, diffeomorphisms, isomorphisms, change of coordinates, differentials of smooth maps

The study of differential geometry begins with 20 pages of definitions. A significant amount of time was spent digesting the notation used in the text. For instance:

$$
dF_p\biggl(\dfrac{\partial}{\partial x^i}\biggr|_p\biggr)f = \dfrac{\partial}{\partial x^i}\biggr|_{p}(f\circ F) = \dfrac{\partial f}{\partial y^j}(F(p))\dfrac{\partial F^j}{\partial x^i}(p) = \biggl(\dfrac{\partial F^j}{\partial x^i}(p)\dfrac{\partial}{\partial y^j}\biggr|_{F(p)}\biggr)
$$

or

$$
dF_p\biggl(\dfrac{\partial}{\partial x^i}\biggr|_{p}\biggr) = dF_p\biggl(d(\phi^{-1})_{\hat{p}}\biggl(\dfrac{\partial}{\partial x^i}\biggr|_{\hat{p}}\biggr) \biggr) = d(\psi^{-1})_{\hat{F}(\hat{p})}\biggl(d\hat{F}_{\hat{p}}\biggl(\dfrac{\partial}{\partial x^i}\biggr|_{\hat{p}}\biggr)\biggr)
$$



# Week 3: Manifolds
Book: Lee Introduction to Smooth Manifolds
- Chapter 3: Tangent bundles, algebra of germs, Standard basis of tangent spaces,  velocities of curves, the differential but with curves.
- Chapter 4: Rank of a smooth map, constant rank maps, smooth immersions, smooth submersions, smooth embeddings, sections, local sections of continuous functions. Characterizations of smooth immersions and submersions. Inverse Function Theorem, Constant Rank theorem, Rank Theorem.

Book: Tu An Introduction to Manifolds
- Chapter 1: Exterior algebra: Tensors, tensor products, wedge product, covectors
- Chapter 3: Critical points, regular points. Level sets, Regular level set theorem. Category theory: covariant and contravariant functors. Smooth sections and frames. Vector fields. Vector bundles.

Book: Munkres Topology (2ed)
- Chapter 8: Blaire spaces

Book: Variational Problems in Geometry
- Chapter 1: Riemannian metrices. Curves: lengths and energies, parametrizations. Euler's equation.

Losing a bit of steam because every proof is starting to look the same. Given some property that holds for $\hat{F}\in C^\infty(\realn,\realm)$, extend it to the manifold case by composing it with coordinate functions. 