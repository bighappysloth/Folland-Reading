---
layout: article
title: Electromagnetism rigourously
date: 2023-10-04 10:17
category: 
author: 
tags: []
summary: 
---
# Introduction
In the study of electromagnetism, Maxwell's equations often get reduced to computational formulas, sidestepping the mathematical depth they contain. This blog post aims to change that. We will rigorously justify Maxwell's equations using advanced mathematical techniques from analysis, distribution theory, differential geometry, and symplecetic geometry. If you are comfortable with topics like Sobolev spaces, Fourier transforms, and Riemannian manifolds, you'll find this approach revealing. Our goal is straightforward: to understand Maxwell's equations not just as physical laws, but as mathematical structures that deserve a meticulous treatment. 

## Charts
Let $M = \real^3$ equipped with its standard $C^\infty$ structure. We define the following charts on $M$. 
<div class="definition-box" markdown=1 name="Standard Chart">
The standard chart on $M$ is given by the Euclidean coordinates. It is denoted by $\Phi_{\real^3}: M\to\real^3$, where $(x_1,x_2,x_3)\mapsto (x_1,x_2,x_3)$.
</div>
Using polar coordinates, we can construct a diffeomorphism (not holomorphic) between $\mathbb{C}\setminus 0$ and $(0,+\infty)\times\real/(2\pi\mathbb{Z})$. Where if $x+iy\in\mathbb{C}$ where $x,y\in\real\setminus 0$, we have

$$
\begin{equation}
x+iy= \rho e^{i\phi}\quad\text{uniquely}
\label{eq:diffeomorphism-s1}
\end{equation}
$$

<div class="definition-box" markdown=1 name="Cylindrical Chart">
The cylindrical chart is defined on $M_{cyl} = \real^3\setminus (0,0,\real)$, $\Phi_{cyl}:M_{cyl}\to S^1\times \real$, where $S^1$ is the standard $1$-sphere. Defined by

$$
\begin{equation}
    \Phi_{cyl}(x_{\underline{3}}) = (\rho(x_{\underline{3}}), \phi(x_{\underline{3}}), z(x_{\underline{3}}))
    \label{eq:cylindrical-chart}
\end{equation}
$$

where we identify $\rho = \rho(x_1 + ix_2)$ and $\phi = \phi(x_1 + ix_2)$  as in \eqref{eq:diffeomorphism-s1}.
</div>

<div class="definition-box" markdown=1 name="Spherical Chart">
The spherical chart is similar to the cylindrical chart. It has the same domain $M_{sph} = M_{cyl}$, and $$\Phi_{sph}: M_{sph}\to (0,+\infty)\times \real/\times (0,\pi)\times (2\pi\mathbb{Z})$$, with 

$$
\begin{equation}
    \Phi_{sph}(x_{\underline{3}}) = (r(x_{\underline{3}}), \theta(x_{\underline{3}}), \phi(x_{\underline{3}}))
    \label{eq:spherical-chart}
\end{equation}
$$

with $r(x_{\underline{3}}) = \vert (x_{\underline{3}})\vert$, and $\theta\in (0,\pi)$ such that \eqref{eq:spherical-chart-theta-calculation} holds for $\rho$, $z$ as in \eqref{eq:diffeomorphism-s1}.

$$
\begin{equation}
    r e^{i\theta} = \rho + i z
    \label{eq:spherical-chart-theta-calculation}
\end{equation}
$$

</div>

## Differentials of transistion maps
Define $\Phi_{\alpha,\beta} = \Phi_{\beta}\Phi_{\alpha}^{-1}$, and we compute


<div class="note-box" markdown=1 name="Cylindrical Coordinates">

Cartesian to Cylindrical
$$
\begin{equation}
D\Phi_{\real^3,cyl} = \begin{bmatrix} \cos(\phi) & \sin(\phi) & 0 \\
-\rho^{-1}\sin(\phi) & \rho^{-1}\cos(\phi) & 0\\
0 & 0 & 1\end{bmatrix}
\label{eq:cartesian-to-cylindrical-differential}
\end{equation}
$$

Cylindrical to Cartesian
$$
\begin{equation}
D\Phi_{cyl,\real^3} = \begin{bmatrix} 
\cos(\phi) & -\rho\sin(\phi) & 0\\ 
\sin(\phi) & \rho\cos(\phi) & 0\\
0 & 0 & 1\end{bmatrix}
\label{eq:cylindrical-to-cartesian-differential}
\end{equation}
$$


Cylindrical gradient frame 

$$
\begin{equation}
X_{cyl} = (\nabla \rho, \nabla \phi, \nabla z)
\label{eq:cylindrical-gradient-frame}
\end{equation}
$$

Metric tensor with respect to \eqref{eq:cylindrical-gradient-frame}.

$$
\begin{equation}
(g_{ij}) = \begin{bmatrix}1 & 0 & 0\\0 & \rho^{2} & 0\\0 & 0 & 1\end{bmatrix}\quad\text{and}\quad \sqrt{\det(g)} = \rho
\label{eq:metric-tensor-cylindrical}
\end{equation}
$$

</div>



<div class="note-box" markdown=1 name="Spherical Coordinates">

Cartesian to Spherical

$$
\begin{equation}
D\Phi_{\real^3,sp}=\dfrac{1}{r}\begin{bmatrix}r\sin{(\theta )} \cos{(\phi )} & r\sin(\phi )\sin(\theta ) & r\cos(\theta )\\ \cos(\phi ) \cos\theta ) & \sin(\phi ) \cos(\theta) & - \sin(\theta )\\- \sin(\phi ) \sin(\theta ) & \cos(\phi )\sin(\theta ) & 0\end{bmatrix}
\label{eq:cartesian-to-spherical-differential}
\end{equation}
$$

Spherical to Cartesian

$$
\begin{equation}
D\Phi_{sp,\real^3}= \begin{bmatrix}\sin{(\theta )} \cos{(\phi )} & r \cos{(\phi )} \cos{(\theta )} & - r \sin{(\phi )} \sin{(\theta )}\\\sin{(\phi )} \sin{(\theta )} & r \sin{(\phi )} \cos{(\theta )} & r \sin{(\theta )} \cos{(\phi )}\\\cos{(\theta )} & - r \sin{(\theta )} & 0\end{bmatrix}
\label{eq:spherical-to-cartesian-differential}
\end{equation}
$$

Spherical gradient frame 

$$
\begin{equation}
X_{sph} = (\nabla r, \nabla \theta, \nabla \phi)
\label{eq:spherical-gradient-frame}
\end{equation}
$$

Metric Tensor with respect to \eqref{eq:spherical-gradient-frame}

$$
\begin{equation}
(g_{ij}) =  \begin{bmatrix}1 & 0 & 0\\0 & r^{2} & 0\\0 & 0 & r^{2} \sin^{2}{(\theta )}\end{bmatrix}\quad\text{and}\quad \sqrt{\det(g)}=r^2\sin(\theta)
\label{eq:metric-tensor-spherical}
\end{equation}
$$

</div>

The standard volume form on $\real^3$ is the nowhere vanishing $dV_{\real^3}$, defined by \eqref{eq:standard-vol-form}.

$$
\begin{equation}
dV_{\real^3} = dx^1\wedge dx^2\wedge dx^3
\label{eq:standard-vol-form}
\end{equation}
$$

We can compute the pullback of $dV_{\real^3}$ with respect to the gradient frame. To be explicit:

$$
\begin{equation}
    \begin{bmatrix}
    \nabla \rho\\\nabla \phi\\\nabla z
    \end{bmatrix} = 
    \begin{bmatrix} 
    \cos(\phi) & \sin(\phi) & 0 \\
    -\rho^{-1}\sin(\phi) & \rho^{-1}\cos(\phi) & 0\\
    0 & 0 & 1
    \end{bmatrix}
    \begin{bmatrix}
    \nabla x^{1}\\\nabla x^{2}\\\nabla x^{3}
    \end{bmatrix}
    \label{eq:cylindrical-gradient-frame-coordinate-transformations}
\end{equation}
$$

$$
\begin{equation}
    \begin{bmatrix}
    \nabla r\\\nabla \theta\\\nabla \phi
    \end{bmatrix} = 
    \dfrac{1}{r}
    \begin{bmatrix}
    r\sin{(\theta )} \cos{(\phi )} & r\sin(\phi )\sin(\theta ) & r\cos(\theta )\\ 
    \cos(\phi ) \cos\theta ) & \sin(\phi ) \cos(\theta) & - \sin(\theta )\\
    - \sin(\phi ) \sin(\theta ) & \cos(\phi )\sin(\theta ) & 0
    \end{bmatrix}
    \begin{bmatrix}
    \nabla x^{1}\\\nabla x^{2}\\\nabla x^{3}
    \end{bmatrix}
    \label{eq:spherical-gradient-frame-coordinate-transformations}
\end{equation}
$$