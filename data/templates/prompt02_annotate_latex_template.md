Your job is to examine the given formalized knowledge and annotate the latex snippet code.


# Input Part 1: The original latex source code:

{{context.latex_og}}

# Input Part 2: The formalized statements which where extracted from that LaTeX source code:

{{context.fnl_statements}}


# Input Part 3: The current latex snippet you are working on:

{{context.latex_current}}

# Input Part 4: The current snippet formalization:

{{context.fnl_current}}

# Input Part 5: Output format:

\setref{<original text>}{label:<formalized entity>}

# Input Part 6: Final Instructions:

Process the current snippet in latex form and in formalized form. In the current latex snippet, replace all occurances of formalized entities with the replacement given in input 5. Only annotate formal entities, that are listed under "concepts in this snippet" in input 2. Return only the new latex snippet code. dont add anything else. Do not hallucinate. Do not annotate equations or math expressions, do not annotate "\mathbb{R}". Do not make annotations inside equations.
Do not annotate equations or math expressions, do not annotate "\mathbb{R}".
Do not annotate equations or math expressions, do not annotate "\mathbb{R}".
Do not annotate equations or math expressions, do not annotate "\mathbb{R}".
Do not hallucinate.
Do not hallucinate.
Do not hallucinate.
Only annotate formal entities, that are listed under "concepts in this snippet" in input 2.
Only annotate formal entities, that are listed under "concepts in this snippet" in input 2.
