# Workflow considerations (minimum viable product)


- The LaTeX source contains special snippet-delimiter comments like `% snippet(5)`
- A LaTeX source code snippet starts with such a comment and ends just before the next such comment.
- In the list of resulting formalized statements we use a comment like `- // snippet(5)` to indicate the following statements are from snippet(5) of the LaTeX source code