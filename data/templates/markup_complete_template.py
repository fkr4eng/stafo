<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Formalized Knowledge</title>
<style>
    body {
        font-family: Arial, sans-serif;
        padding: 20px;
    }
    .toggle-container {
        display: flex;
        align-items: flex-start;
        margin-bottom: 20px;
    }
    .content-box {
        padding: 10px;
        border: 2px solid #333;
        min-width: 150px;
        flex: 1;
    }
    .toggle-btn {
        padding: 8px 16px;
        margin-left: 10px; /* space between content and button */
        font-size: 14px;
        cursor: pointer;
        height: fit-content; /* so button isn't stretched vertically */
    }
    .state {
        display: none; /* hidden templates */
    }

    .tooltip {
        position: relative;
        cursor: pointer;
        color: blue;
    }

    .tooltip .tooltiptext {
        visibility: hidden;
        width: 800px;
        height: 600px;
        background-color: #fff;
        color: #333;
        text-align: left;
        border-radius: 6px;
        border: 1px solid #ccc;
        padding: 10px;
        position: absolute;
        z-index: 1;
        top: 1.5em;
        left: 0;
        box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
        transition: opacity 0.5s ease, visibility 0.5s ease;
        opacity: 0;
        transform-origin: top left;
    }

    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }

    .tooltiptext iframe {
        width: 100%;
        height: 100%;
        border: none;
        zoom: 0.5;
        pointer-events: none; /* disable interaction */
    }
    .markdown-output {
        border: 1px solid #ccc;
        padding: 15px;
        background: #f9f9f9;
        margin-bottom: 20px;
        white-space: pre-wrap;
    }
    .markdown-source {
        display: none; /* hide raw markdown */
    }
    .markdown-output ul {
        margin-top: -10px;
        margin-bottom: -10px;
        padding-left: 20px;
    }
    .markdown-output ul li {
        margin-top: -10px;
        margin-bottom: -10px; /* smaller gap between bullets */
        padding: 0;
    }

</style>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/atom-one-dark.min.css">

<!-- Highlight.js library -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
<!-- Load Python syntax support -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/python.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<script>
    // Automatically highlight all code blocks
    hljs.highlightAll();
</script>

<link rel="stylesheet" type="text/css" href="nl_latex_copy.css" />
<script>window.MathJax = {
  tex: { tags: "ams" },
  options: {
    processHtmlClass: "state",  // only process elements with this class
  },
  startup: {
    typeset: true  // disable automatic typesetting on startup
  }
};</script>
<script type="text/javascript" async="async" id="MathJax-script" src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml-full.js"></script>

</head>
<body>

{% for snippet in context.snippets %}
<b>Snippet {{snippet.snippet}}</b>
<div class="toggle-container">
    <div class="content-box"></div>
    <button class="toggle-btn">Show FNL</button>

    <div class="state" data-button="Show FNL">
{{snippet.tex}}
    </div>
    <div class="state" data-button="Show PyIRK">
        <div class="markdown-block">
            <textarea class="markdown-source">
{{snippet.fnl}}
            </textarea>
            <div class="markdown-output"></div>
        </div>

    </div>
    <div class="state" data-button="Show TeX">
        <pre><code class="language-python">
{{snippet.pyirk}}
        </code></pre>
    </div>
</div>

{% endfor %}


<script>
document.querySelectorAll(".toggle-container").forEach(container => {
    const states = Array.from(container.querySelectorAll(".state"));
    let index = 0;

    const box = container.querySelector(".content-box");
    const button = container.querySelector(".toggle-btn");

    function showState(i) {
        box.innerHTML = states[i].innerHTML;
        const btnLabel = states[i].dataset.button;
        if (btnLabel) {
            button.textContent = btnLabel;
        }
    }

    showState(index);

    button.addEventListener("click", () => {
        index = (index + 1) % states.length;
        showState(index);
    });
    MathJax.typesetPromise().catch(err => console.error(err.message));
});
</script>
<script>
  // For each markdown block, render the markdown inside the output div
  document.querySelectorAll('.markdown-block').forEach(block => {
    const source = block.querySelector('.markdown-source').value;
    const output = block.querySelector('.markdown-output');
    output.innerHTML = marked.parse(source);
  });
</script>
</body>
</html>
