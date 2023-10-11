---
layout: article
title: Jekyll Site Management and MathJax tips
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


# Styling

## General Styling
The CSS styling is found across `_variables.scss`, `custom.scss`. The code that is responsible for changing the *style of the codeblocks* is found within `_reset.scss`, where

```css
pre, code {
  font-family: map-get($base, font-family-code);
}

code {
  font-size: map-get($base, font-size-xs);
  line-height: map-get($base, line-height-sm);
}
```

As usual, we use three backticks to delimit code blocks. Font size adjustents are found in `_variables.scss`, where 
- the two variables 
  ```css
    font-size-root:         12px,
    font-size-root-sm:      10px,
  ```
  control the absolute size of the fonts, and the variables below are the ones I found to be most impactful. Adjust the lineheight to your liking.
  ```css
  font-size-xl:           1.0rem,
  font-size-lg:           1.0rem,
  font-size:              1.0rem,
  font-size-sm:           1.0rem,
  font-size-xs:           0.8rem,

  font-weight:            400,
  font-weight-bold:       500,

  line-height-xl:         2,
  line-height-lg:         1.4,
  line-height:            1.2,
  line-height-sm:         1.2,
  line-height-xs:         1.2,

  spacer:                 0.4rem,

  border-radius-lg:       .4rem,
  border-radius:          .2rem,
  border-radius-sm:       .1rem
  ```

  The margins of the website is adjusted in several places: the first is in `_variables.scss`.
  ```css
  $layout: (
    header-height:          5rem, // top bar
    header-height-sm:       3rem, // top bar small mode
    content-max-width:      600px, // very useful to control how wide the main content is
    sidebar-width:          150px, // so that the sidebar does not take up too much of the screen
    sidebar-header-height:  3rem,
    aside-width:            150px // the 'TOC" portion of the article
  );
  ```
  Adjusting `content-max-width` does not change the width of the homepage correspondingly. One has to change the variable `width` something, in another place I cannot recall off the top of my head. EDIT: I believe it is the third line in `_main.scss` which reads `max-width: map-get($layout, content-max-width);` but do not quote me on this.

  To change the spacing between post thumbnails: look into `_articles.scss`
  ```css
  .layout--articles {
    margin: map-get($spacers, 4) 0;
    margin-top: map-get($spacers, 5);
    @include media-breakpoint-down(md) {
      margin-top: map-get($spacers, 4);
    }
    .card__header {
      font-size: map-get($base, font-size);
    }
    .card__image {
      & > .overlay {
        &, .card__header {
          font-size: map-get($base, font-size-sm);
        }
      }
    }
  }
  ```
# MathJax setup
## Coloured boxes
To implement the boxed theorem environments, we use a html div. All of the boxes are defined within `_custom.scss`. A few more things to note: the numbering on the boxes reset on each `h2` section (so double `##` pound sign), you can adjust it 

```css
// Initialize the definition counter
body {
    counter-reset: h1counter h2counter definition lemma theorem example remark note corollary; 
}

h1 {
    counter-increment: h1counter;
}

// Reset the definition counter every time a new <h2> starts
h2 {
    counter-increment: h2counter;
    counter-reset: definition lemma theorem example remark corollary note; 
}
```

The default colours are from matplotlib's Tableau theme, we have commented out the rgb values inside `_custom.scss` for convenience. There are two skeleton styles for the boxes (proof style excluded for now),

```css
@mixin box-style {
    position: relative;
    margin: 1rem 0;
    padding: 0.5rem 1rem;
    border: 1px solid #000;
    border-radius: 0.0rem;
    align-items: center; // Align content vertically in the center

    &::before {
        margin: 0 0;
        padding: 0;
        font-weight: bold;
        color: #000;
    }

    &::after {
        white-space: pre; // Retain spaces and newlines
    }

    p {
        margin: 0; // Reset margin for the paragraph
    }
}

@mixin content-with-name($type, $color) {
    $capitalizedType: capitalize($type);
    @include box-style;
    background-color: $color;

    &::before {
        counter-increment: $type;
        content: '#{$capitalizedType} ' counter(h2counter) '.' counter($type);
    }

    &[name]:not([name=""])::before {
        content: '#{$capitalizedType} ' counter(h2counter) '.' counter($type) ':   ';
        white-space: pre;
    }
}
```

The first `box-style` controls the colouring and the amrgin of the boxes. The second one serves as a wrapper to process the latex labels and numbering options. The label changes depending on if the `"name"` field is blank. Writing 

```html
<div class="definition-box" markdown=1 name="Associated open Ellipsoid">
Let $q\in P$, it defines an open set called the **associated open ellipsoid of $q$**, denoted by $E(q)$ or $E_q$ 

$$
E(q) = \bigset{x\in\real^{2n},\: q(x)< 1} = [ q<1 ] 
$$

</div>
```

gives 

<div class="definition-box" markdown=1 name="Associated open Ellipsoid">
Let $q\in P$, it defines an open set called the **associated open ellipsoid of $q$**, denoted by $E(q)$ or $E_q$ 

$$
E(q) = \bigset{x\in\real^{2n},\: q(x)< 1} = [ q<1 ] 
$$

</div>

Example of these boxes can be found [here]({{ site.baseurl }}/{% post_url 2023-08-01-part-4-functional-analytic-setting %}). Including the styling implementation for the boxes for convenience:

```css
.definition-box {
    @include content-with-name(definition, rgba(231, 201, 95, 0.1));

    .definition-label {
        font-weight: bold;
    }
}

.theorem-box {
    @include content-with-name(theorem, rgba(86, 120, 163, 0.1));
}

.lemma-box {
    @include content-with-name(lemma, rgba(133, 182, 177, 0.1));
}

.corollary-box {
    @include content-with-name(corollary, rgba(86, 120, 163, 0.1));
}

.note-box {
    @include content-with-name(note, rgba(227, 147, 68, 0.05));
}

.remark-box {
    @include content-with-name(remark, rgba(86, 120, 163, 0.05));
}
```



## Custom startup script
We modified `head.html` to include a special startup script (along with the script that launches MathJax). The startup section is to fix the div labels within the theorem boxes. Those labels are rendered after the main page, so we (chatgpt and me) used a javascript promise `MathJax.typesetPromise([element])` to delay rendering all the math until the entire html has been loaded, shown below. The custom startup script also loops through each of the coloured boxes (definition, theorem, remark, lemma, corollary, note) and replaces the labels, and renders the labels in latex.

Things that do not work:
- MathJax plugins: I could not get the latex extensions to work for some resaon. My macros would not work with any of the plugins, and upon removing all my macros even then the plugins do not load consistently.
- The delimiters `\[` and `\]` do not trigger math mode for some reason. However, writing 

```latex
\begin{equation}
\dfrac{1}{2} 
\end{equation}
```

renders 

\begin{equation}
\dfrac{1}{2}
\end{equation}



Cutom startup script
{% highlight html %}
<head>
  <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
  <script>
    window.MathJax = {
      startup: {
        ready: () => {
          MathJax.startup.defaultReady();
          // Your custom code after MathJax is ready
          MathJax.startup.promise.then(() => {
            MathJax.typesetClear();
            // List of classes to process
            const classes = ['definition-box', 'theorem-box', 'remark-box', 'lemma-box', 'corollary-box', 'note-box'];

            classes.forEach(className => {
              // Grab elements of the current class
              const elements = document.querySelectorAll('.' + className);

              elements.forEach(element => {
                const nameValue = element.getAttribute('name');
                if (nameValue) {  // Check if "name" attribute exists and is not empty
                  const strongElement = document.createElement('strong');  // Create a new <strong> element
                  strongElement.textContent = nameValue;  // Set its text content
                  element.insertBefore(strongElement, element.firstChild);  // Insert it as the first child of the element

                  // Update MathJax to typeset the changed content
                  MathJax.typesetPromise([element]).catch((err) => console.error(err.message));
                }
              });
            });
          }).catch((err) => console.error(err.message));
        }
      },
      // loader: {
      //   load: ['[tex]/textmacros','[tex]/physics']
      // },
      tex: {
        tags: 'ams',
        inlineMath: [              // start/end delimiter pairs for in-line math
          ['\\(', '\\)'],
          ['$', '$'],
        ],
        displayMath: [             // start/end delimiter pairs for display math
          ['$$', '$$'],
          ['\\[', '\\]']
        ],
        // packages: {'[+]': ['textmacros']},
        processEscapes: true,
        processEnvironments: true,
        macros: {
          induces: "{\\: \\looparrowright \\:}",
          // other macros omitted
          Isomor: ["\\overset{\\:\\mathcal{#1}\\:}{\\rightleftharpoons}", 1],
          oin: "\\: \\mathring{\\in} \\:",
        },
        formatError: (jax, err) => jax.formatError(err)
      }
    };
  </script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js">
  </script>

</head>
{% endhighlight %}

## Additional resources for MathJax:
- [mathjax v3 configuration](https://docs.mathjax.org/en/latest/options/input/tex.html#tex-options)
- [mathjax v2 syntax for delimiters](https://scaomath.github.io/blog/welcome-to-jekyll/)
- [steps to obtain default.html back](https://stackoverflow.com/questions/50998466/how-to-use-latex-in-new-jekyll-gem-based-theme-minima)
- basically: clone minima, then copy all the required files (what is needed is default.html, and head.html)
- paste the required configuration scripts, the cdn for mathjax into the head section.
- custom-header.html does not work for some reason.
- minima 3.0 is actually called minima 2.5.1

## current folder structure
{% raw %}
./_includes:
head.html

./_layout:
base.html	default.html	home.html	page.html	post.html
{% endraw %}
copy base, default, home, page and post.html from the minima repo. copy head.html into ./_includes, then modify it. 

## interesting plugins
In my experience none of the plugins work and they break everything 
[pdf embedding](https://mihajlonesic.gitlab.io/projects/jekyll-pdf-embed/#result)
[algolia search](https://github.com/algolia/jekyll-algolia)(abandoned)

## Cross Repo Syncing, how does it work?

honestly i am not a computer expert i spent 3-4 hours googling how to make this wokr. my main mistake was using gpt 3.5 rather than gpt 4. gpt 4 was able to code somethign that works while i wasted hours using gpt 3.5.
[link to github workflow](https://github.com/bighappysloth/Folland-Reading/blob/main/.github/workflows/latex.yml)

Update later.