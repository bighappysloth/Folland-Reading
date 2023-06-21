---
layout: post
title: mathjax v3 on minima, jekyll site management
date:   2023-05-09 12:02:12 -0400
categories: website
---
in line math test $\borel_\real$
The following doesnt work for some reason.

\[\dfrac{1}{2} = x\]

while this does
$$\dfrac{1}{2} =x$$

## todo
- [improve workflow](https://www.xuningyang.com/blog/2021-01-11-katex-with-jekyll/) by using katex, and pandoc to convert latex into md.

## fixing 404
- [guide on URLs](https://mademistakes.com/mastering-jekyll/site-url-baseurl/#absolute_url-filter)

## resources for mathjax:
- [mathjax v3 configuration](https://docs.mathjax.org/en/latest/options/input/tex.html#tex-options)
- [mathjax v2 syntax for delimiters](https://scaomath.github.io/blog/welcome-to-jekyll/)

- [steps to obtain default.html back](https://stackoverflow.com/questions/50998466/how-to-use-latex-in-new-jekyll-gem-based-theme-minima)

- basically: clone minima, then copy all the required files (what is needed is default.html, and head.html)

- paste the required configuration scripts, the cdn for mathjax into the head section.

- custom-header.html does not work for some reason.
- minima 3.0 is actually called minima 2.5.1

# current head.html file
{% highlight html %}
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  {%- seo -%}
  <link rel="stylesheet" href="{{ "/assets/main.css" | relative_url }}">
  {%- feed_meta -%}
  {%- if jekyll.environment == 'production' and site.google_analytics -%}
    {%- include google-analytics.html -%}
  {%- endif -%}
  <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
  <script>
    MathJax = {
      loader: {
        load: ["input/tex", "output/chtml"]
      },
      tex: {
        inlineMath: [              // start/end delimiter pairs for in-line math
          ['\\(', '\\)'],
          ['$', '$'],
        ],
        displayMath: [             // start/end delimiter pairs for display math
          ['$$', '$$'],
          ['\\[', '\\]']
        ],
        
        processEscapes: true,
        macros: {
          real: "\\mathbb{R}",
          realn: "\\mathbb{R}^n",
          nat: "\\mathbb{N}}",
          natplus: "\\mathbb{N}^+",
          integer: "\\mathbb{Z}",
          rat: "\\mathbb{Q}",
          borel: "\\mathbb{B}",
          complex: "\\mathbb{C}",
          range: "\\operatorname{range}",
          dom: "\\operatorname{dom}",
          codom: "\\operatorname{codom}",
          image: "\\operatorname{im}",
          id: ["\\operatorname{id}_{#1}", 1],
          sgn: "\\operatorname{sgn}",
          exp: "\\operatorname{exp}",
          wt: "\\operatorname{wt}",
          least: "\\operatorname{least}",
          norm: ["\\lVert {#1} \\rVert", 1],
          bignorm: ["\\left\\lVert {#1} \\right\\rVert", 1],
          bigset: ["\\biggl \\{ {#1} \\biggr \\}", 1],
          bigbrackets: ["\\biggl ( {#1} \\biggr )", 1],
          acc: "\\operatorname{acc}",
          nb: ["\\mathcal{N}_B({#1})", 1],
          N: ["\\mathcal{N}(#1)", 1],
          Tau: "\\mathcal{T}",
          cl: ["\\overline{#1}", 1],
          clc: ["\\overline{#1}^c", 1],
          Epsilon: "\\mathcal{E}",
          diam: "\\operatorname{diam}",
          increasesto: "\\nearrow",
          decreasesto: "\\searrow",
          cond: "\\operatorname{cond}}",
          card: "\\operatorname{card}",
          szz: "\\mathcal{S}",
          cinf: "C^{\\infty}",
          ccinf: "C_c^{\\infty}",
          cnv: "\\ast",
          pmap: ["\\pi_{#1}({#2})", 2],
          pnv: ["\\pi_{#1}^{-1}({#2})", 2],
          bc: ["\\operatorname{BC}({#1})", 1],
          cc: ["\\operatorname{C}_c({#1})", 1],
          cnot: ["\\operatorname{C}_0({#1})", 1],
          supp: ["\\operatorname{supp}({#1})", 1],
          acal: "\\mathcal{A}",
          mcal: "\\mathcal{M}",
          ncal: "\\mathcal{N}",
          mustar: "\\mu^*",
          mubar: "\\cl{\\mu}",
          munot: "\\mu_0",
          muStar: "\\mu_*",
          diag: "\\operatorname{diag}",
          dim: "\\operatorname{dim}",
          defect: "\\operatorname{def}",
          rank: "\\operatorname{rank}",
          col: "\\operatorname{col}",
          row: "\\operatorname{row}",
          lin: "\\operatorname{lin}",
          spn: "\\operatorname{span}",
          tr: "\\operatorname{tr}",
          poly: "\\mathbb{P}",
          ff: "\\mathbb{F}",
          xx: "\\mathbf{X}}",
          yy: "\\mathbf{Y}}",
          ss: "\\mathbf{S}}",
          ww: "\\mathbf{W}}",
          uu: "\\mathbf{U}}",
          tt: "\\mathbf{T}}",
          xn: "\\{x_n\\}_{n\\geq 1}",
          yn: "\\{y_n\\}_{n\\geq 1}"
        }
      }
    };
  </script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js">
  </script>
</head>
{% endhighlight %}

## current folder structure
{% raw %}
./_includes:
head.html

./_layout:
base.html	default.html	home.html	page.html	post.html
{% endraw %}
copy base, default, home, page and post.html from the minima repo. copy head.html into ./_includes, then modify it. 

## interesting plugins
[pdf embedding](https://mihajlonesic.gitlab.io/projects/jekyll-pdf-embed/#result)
[algolia search](https://github.com/algolia/jekyll-algolia)(abandoned)

## how i implemented cross repo syncing

honestly i am not a computer expert i spent 3-4 hours googling how to make this wokr. my main mistake was using gpt 3.5 rather than gpt 4. gpt 4 was able to code somethign that works while i wasted hours using gpt 3.5.
[link to github workflow](https://github.com/bighappysloth/Folland-Reading/blob/main/.github/workflows/latex.yml)