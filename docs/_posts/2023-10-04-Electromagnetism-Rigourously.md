---
layout: article
title: Electromagnetism rigourously
date: 2023-10-04 10:17
category: 
author: 
tags: ['vector calculus','multivariable calculus','rigourously','geometry']
summary: 
---
# Introduction
Within the study of electromagnetism, Maxwell's equations often get reduced to computational formulas, sidestepping the mathematical depth they contain. This blog post aims to change that. We will rigorously justify his equations using techniques from analysis, distribution theory, differential and symplecetic geometry. If you are comfortable with topics like Sobolev spaces, Fourier transforms, and Riemannian manifolds, you will find this approach revealing.

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
\begin{align}
D\Phi_{\real^3,cyl} &= \begin{bmatrix} \cos(\phi) & \sin(\phi) & 0 \\
-\rho^{-1}\sin(\phi) & \rho^{-1}\cos(\phi) & 0\\
0 & 0 & 1\end{bmatrix} \label{eq:cartesian-to-cylindrical-differential}\\[2ex]
\det{(D\Phi_{\real^3,cyl})} &= \frac{1}{\rho}\label{eq:det-cartesian-to-cylindrical-differential}
\end{align}
$$


Cylindrical to Cartesian
$$
\begin{align}
D\Phi_{cyl,\real^3} &= \begin{bmatrix} 
\cos(\phi) & -\rho\sin(\phi) & 0\\ 
\sin(\phi) & \rho\cos(\phi) & 0\\
0 & 0 & 1\end{bmatrix}\label{eq:cylindrical-to-cartesian-differential} \\[2ex] 
\det{(D\Phi_{cyl,\real^3})} &= \rho \label{eq:det-cylindrical-to-cartesian-differential}
\end{align}
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
\begin{align}
(g_{ij}) &= \begin{bmatrix}1 & 0 & 0\\0 & \rho^{2} & 0\\0 & 0 & 1\end{bmatrix}\label{eq:metric-tensor-cylindrical} \\[2ex] 
\sqrt{\det(g)} &= \rho\label{eq:det-metric-tensor-cylindrical}
\end{align}
$$

</div>



<div class="note-box" markdown=1 name="Spherical Coordinates">

Cartesian to Spherical

$$
\begin{align}
D\Phi_{\real^3,sp} &= \dfrac{1}{r}\begin{bmatrix}r\sin{(\theta )} \cos{(\phi )} & r\sin(\phi )\sin(\theta ) & r\cos(\theta )\\ \cos(\phi ) \cos\theta ) & \sin(\phi ) \cos(\theta) & - \sin(\theta )\\- \sin(\phi ) \sin(\theta ) & \cos(\phi )\sin(\theta ) & 0\end{bmatrix}\label{eq:cartesian-to-spherical-differential} \\[2ex] 
\det{(D\Phi_{\real^3,sph})} &= \frac{1}{r^2\sin(\theta)} \label{eq:det-cartesian-to-spherical-differential}
\end{align}
$$

Spherical to Cartesian

$$
\begin{align}
D\Phi_{sp,\real^3} &= \begin{bmatrix}\sin{(\theta )} \cos{(\phi )} & r \cos{(\phi )} \cos{(\theta )} & - r \sin{(\phi )} \sin{(\theta )}\\\sin{(\phi )} \sin{(\theta )} & r \sin{(\phi )} \cos{(\theta )} & r \sin{(\theta )} \cos{(\phi )}\\\cos{(\theta )} & - r \sin{(\theta )} & 0\end{bmatrix}\label{eq:spherical-to-cartesian-differential} \\[2ex] 
\det{(D\Phi_{sph,\real^3})} &= r^2\sin(\theta) \label{eq:det-spherical-to-cartesian-differential}
\end{align}
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
\begin{align}
(g_{ij}) &=  \begin{bmatrix}1 & 0 & 0\\0 & r^{2} & 0\\0 & 0 & r^{2} \sin^{2}{(\theta )}\end{bmatrix}\label{eq:metric-tensor-spherical}\\[2ex] 
\sqrt{\det(g)} &= r^2\sin(\theta)\label{eq:det-metric-tensor-spherical}
\end{align}
$$

</div>

# Gradient Frame

## Calculations
Cartesian to Cylindrical
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

Cartesian to Spherical
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

## Gradient Frame Metric Product
Cylindrical gradients pairings under the Riemannian metric

$$
\begin{equation}
\begin{bmatrix}
    1 & 0 & 0 \\
    0 & \frac{1}{\rho^2} & 0 \\
    0 & 0 & 1 
\end{bmatrix}=
\begin{bmatrix}
\langle \nabla \rho, \nabla \rho\rangle & \langle \nabla \rho, \nabla \phi\rangle & \langle \nabla \rho, \nabla z\rangle \\
\langle \nabla \phi, \nabla \rho\rangle & \langle \nabla \phi, \nabla \phi\rangle & \langle \nabla \phi, \nabla z\rangle \\
\langle \nabla z, \nabla \rho\rangle & \langle \nabla z, \nabla \phi\rangle & \langle \nabla z, \nabla z\rangle 
\end{bmatrix}
\label{eq:cylindrical-gradient-pairings-metric}
\end{equation}
$$


Spherical gradient pairings under Riemannian metric

$$
\begin{equation}
\begin{bmatrix}
    1 & 0 & 0 \\
    0 & \frac{1}{r^2} & 0 \\
    0 & 0 & \frac{1}{r^2\sin^2(\theta)}
\end{bmatrix}=\begin{bmatrix}
\langle \nabla r, \nabla r\rangle & \langle \nabla r, \nabla \theta\rangle & \langle \nabla r, \nabla \phi\rangle \\
\langle \nabla \theta, \nabla r\rangle & \langle \nabla \theta, \nabla \theta\rangle & \langle \nabla \theta, \nabla \phi\rangle \\
\langle \nabla \phi, \nabla r\rangle & \langle \nabla \phi, \nabla \theta\rangle & \langle \nabla \phi, \nabla \phi\rangle 
\end{bmatrix}
\label{eq:spherical-gradient-pairings-metric}
\end{equation}
$$

## Magnitudes of gradient coordinate vector fields
Cylindrical magnitudes

$$
\begin{align*}
\vert \nabla \rho\vert &= 1\\[2ex]
\vert \nabla \phi\vert &= \frac{1}{\rho}\\[2ex]
\vert \nabla z\vert &= 1
\end{align*}
$$

Spherical magnitudes

$$
\begin{align*}
\vert \nabla r\vert &= 1\\[2ex]
\vert \nabla \theta\vert &= \frac{1}{r}\\[2ex]
\vert \nabla \phi\vert &= \frac{1}{r\sin(\theta)}
\end{align*}
$$

## Gradient of a function
<div class="definition-box" markdown=1 name="Gradient of a function in coordinates">
Fix $f\in C^\infty(M)$ where $(M,g)$ is a finite dimensional $\realn$ Riemannian-manifold admitting partitions of unity. The gradient of a function $\grad{f}$ is defined as the vector field obtained by applying  musical isomoprhism $\sharp$ on the covector field $df$. In symbols

$$
\begin{equation}
\grad{f} = (df)^{\sharp} = \hat{g}^{-1}(df)
\label{eq:gradient-function-def}
\end{equation}
$$

We write $\grad{f}\lrcorner g = df$. If $X\in\mathfrak{X}(M)$ is a vector field, the $\grad{f}$ must satisfy

$$
g(\grad{f}, X) = df(X) = Xf
$$
</div>
For any vector field $X = X^j\partial_{j}$, we write $\hat{g}(X) = X\lrcorner g$ which is a covector field. If $g = g_{ij}dx^idx^j$ where $dx^idx^j$ denotes the symmetric product (not to be confused with the wedge product), then 

$$
\begin{align*}
\hat{g}(X) &= g_{ij}\biggl(dx^i(X^k\partial_k)\biggr)dx^j\\
&= g_{ij}\biggl(X^k dx^i(\partial_k)\biggr)dx^j\\
&= g_{ij}X^i dx^j
\end{align*}
$$

# Orthonormal Frames
## Calculations
We write $\unab{a} = \frac{\grad{a}}{\vert \grad{a}\vert}$ for convenience, and $\unab{a} = \widehat{\nabla a}$. We sometimes omit 'orthonormal' and refer to the cylindrical orthonormal frame as the cylindrical frame. The cylindrical gradient frame is still the one defined in \eqref{eq:cylindrical-gradient-frame} (resp. for spherical in \eqref{eq:spherical-gradient-frame}).

Cylindrical Frame

$$
\begin{align*}
\nab{\rho} &= \unab{\rho}\\[2ex]
\nab{\phi} &= \frac{\unab{\phi}}{\rho}\\[2ex]
\nab{z} &= \unab{z}
\end{align*}
$$

Spherical Frame

$$
\begin{align*}
\nab{r} &= \unab{r}\\[2ex]
\nab{\theta} &= \frac{\unab{\theta}}{r}\\[2ex]
\nab{\phi} &= \frac{\unab{\phi}}{r\sin(\theta)}
\end{align*}
$$

# Volume forms
The standard volume form on $\real^3$ is the nowhere vanishing $dV_{\real^3}$, defined by \eqref{eq:standard-vol-form}.

$$
\begin{equation}
dV_{\real^3} = dx^1\wedge dx^2\wedge dx^3
\label{eq:standard-vol-form}
\end{equation}
$$

We can compute the pullback of $dV_{\real^3}$ with respect to the gradient frame. By the pullback formula of a top-form: $$dV_{\alpha} = \Phi^*_{\alpha,\real^3}(dV_{\real^3})$$.

Volume form in cylindrical coordinate (co)-frame

$$
\begin{align*}
dV_{cyl} &= \Phi_{cyl,\real^3}^*(dV_{\real^3}) \\
&= \Phi_{cyl,\real^3}^*(dx^1\wedge dx^2\wedge dx^3)\\
&=\det{(D\Phi_{cyl,\real^3})}d\rho\wedge d\phi\wedge dz \\
&= \rho d\rho\wedge d\phi\wedge dz
\end{align*}
$$

Volume form in spherical coordinate (co)-frame

$$
\begin{align*}
dV_{sph} &= \Phi_{sph,\real^3}^*(dV_{\real^3}) \\
&= \Phi_{sph,\real^3}^*(dx^1\wedge dx^2\wedge dx^3)\\
&=\det{(D\Phi_{sph,\real^3})}dr\wedge d\theta\wedge d\phi \\
&= r^2\sin(\theta) dr\wedge d\theta\wedge d\phi
\end{align*}
$$

## Volume forms on regular hypersurfaces
### Cylindrical: $\rho$ level set
$S = [\rho = a]$, the unit normal to $S$ is $N=\frac{\grad{\rho}}{\vert \grad{\rho}\vert}=\nabla\rho$. Then,

$$
\begin{align*}
dV_{S} &= \iota_S^*(N\lrcorner dV_{\real^3})\\
&= \iota_S^*(N\lrcorner \rho d\rho\wedge d\phi \wedge dz)\\
&= \rho d\phi\wedge dz\\
&= a d\phi\wedge dz
\end{align*}
$$

### Cylindrical: $\phi$ level set
$S = [\phi = a]$, and $N = \frac{\grad{\phi}}{\vert \grad{\phi}\vert} = \rho\nabla\phi$. Then,

$$
\begin{align*}
dV_{S} &= \iota_S^*(N\lrcorner dV_{\real^3})\\
&= \iota_S^*(N\lrcorner \rho d\rho\wedge d\phi \wedge dz)\\
&= -\rho^2 d\rho \wedge dz\\
\end{align*}
$$

### Cylindrical: $z$ level set
$S = [z = a]$, and $N = \nabla z$.

$$
\begin{align*}
dV_{S} &= \iota_S^*(N\lrcorner dV_{\real^3})\\
&= \iota_S^*(N\lrcorner \rho d\rho\wedge d\phi \wedge dz)\\
&= \rho d\rho\wedge d\phi
\end{align*}
$$

### Spherical: $r$ level set
$S = [r=a]$, because $\vert \grad{r}\vert = 1$: $N = \nabla r$, and 

$$
\begin{align*}
dV_{S} &= \iota_S^*(N\lrcorner dV_{\real^3})\\
&= \iota_S^*(N\lrcorner r^2\sin(\theta) dr\wedge d\theta \wedge d\phi)\\
&= r^2\sin(\theta)d\theta\wedge d\phi\\
&= a^2\sin(\theta)d\theta\wedge d\phi
\end{align*}
$$

### Spherical: $\theta$ level set
$S = [\theta = a]$, where $\vert \grad{\theta}\vert = r^{-1}$, so $N = r\nabla\theta$. 

$$
\begin{align*}
dV_{S} &= \iota_S^*(N\lrcorner dV_{\real^3})\\
&= \iota_S^*(N\lrcorner r^2\sin(\theta) dr\wedge d\theta \wedge d\phi)\\
&= -r^3\sin(\theta)dr\wedge d\phi\\
&= -r^3\sin(a)dr\wedge d\phi
\end{align*}
$$

### Spherical: $\phi$ level set
$S=[\phi = a]$, and $N = r\sin(\theta)\nabla \phi$.

$$
\begin{align*}
dV_{S} &= \iota_S^*(N\lrcorner dV_{\real^3})\\
&= \iota_S^*(N\lrcorner r^2\sin(\theta) dr\wedge d\theta \wedge d\phi)\\
&= r^3\sin^2(\theta)dr\wedge d\theta
\end{align*}
$$



# Integral over hypersurfaces
Let $S$ be a compact hypersurface with or without boundary in $\real^3$. The surface integral of a vector field $X\in\mathfrak{X}(M)$ over $S$ is defined by the integral in \eqref{eq:current-density-area-integral}

$$
\begin{equation}
I = \int_{S} \langle X, N\rangle_{\real^3} dV_{s}
\label{eq:current-density-area-integral}
\end{equation}
$$

where $${dV}_{s} = \iota_S^{*}(N\lrcorner dV_g)$$ is the usual volume form on $S$ that descends from ${dV}_{\real^3}$ with the help of a smooth unit normal $N\in\mathfrak{X}(M)$.

# Current
This section is incomplete, but we list all of its equations. 

s