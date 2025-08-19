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

\eqnote{<original math code>}{concepts:<list of formalized entities in equation>}{statement:<formalized math code>}

# Input Part 6: Example

# previous latex input:
Zu zwei Vektoren $x,y\in{\mathbb{R}}^{n}$ definiert man durch
\begin{equation}
(x,y):=\sum_{i=1}^{n}x_{i}y_{i}\label{eq:skalarprodukt}
\end{equation}
das (\textbf{\em kanonische}) \textbf{\em Skalarprodukt}.

# previous formalized statements:
- There is a binary operator: 'canonical scalar product' @en.
- 'canonical scalar product' has the alternative german label 'kanonisches Skalarprodukt'.
- 'canonical scalar product' has the alternative german label 'Skalarprodukt'.
- 'canonical scalar product' has the alternative label 'scalar product' @en.
- 'canonical scalar product' has the associated LaTeX notation $(x,y)$.
- The type of argument1 of 'canonical scalar product' is 'vector'.
- The type of argument2 of 'canonical scalar product' is 'vector'.

# current latex snippet
Die Vektoren~$x$ und~$y$ sind zueinander \textbf{\em orthogonal} (bzw.
stehen \textbf{\em senkrecht aufeinander}), falls
\[
(x,y)=0.
\]

# current formalized statements
- There is a class 'orthogonality' @en.
- 'orthogonality' has the alternative german label 'Orthogonalität'.
- 'orthogonality' has the verbal description 'concept of orthogonality, perpendicular vectors.' // todo better description
- There is a relation 'is orthogonal to'
- The type of argument1 of 'is orthogonal to' is 'vector'
- The result type of 'is orthogonal to' is 'vector'
- 'is orthogonal to' has the alternative german label 'ist senkrecht zu'
- 'is orthogonal to' 'is used to model' 'orthogonality'
- 'is orthogonal to' 'is symmetrical' 'True'.
- There is an equivalence-statement:
    - full source code: Die Vektoren~$x$ und~$y$ sind zueinander \textbf{\em orthogonal} (bzw. stehen \textbf{\em senkrecht aufeinander}), falls \[ (x,y)=0. \]
    - formalized setting:
        - 'x' is an instance of 'vector'.
        - 'y' is an instance of 'vector'.
        - 'n' is an instance of 'integer number'.
        - 'Rn' is an instance of 'n-dimensional real vector space'.
        - 'Rn' 'has dimension' 'n'.
        - 'x' is element of 'Rn'.
        - 'y' is element of 'Rn'.
    - formalized premise:
        - There is an equation:
            - full source code: 'canonical scalar product'(x, y) == 0
    - formalized assertion:
        - 'x' 'is orthogonal to' 'y'.


- Concepts in this snippet:
    - 'orthogonality'
    - 'is orthogonal to'
    - 'vector'
    - 'integer number'
    - 'n-dimensional real vector space'
    - 'has dimension'
    - 'is element of'
    - 'canonical scalar product'
- Defined in this snippet:
    - 'orthogonality'
    - 'is orthogonal to'

# expected output:
Die Vektoren~$x$ und~$y$ sind zueinander \textbf{\em orthogonal} (bzw.
stehen \textbf{\em senkrecht aufeinander}), falls
\eqnote{\[
(x,y)=0.
\]}{concepts:'vector', 'canonical scalar product'}{statement:'canonical scalar product'('vector', 'vector')=0}


# Input Part 7: Final Instructions:

Process the current snippet in latex form and in formalized form. Look for mathematical expressions in the current snippet and annotate them as given in input 5. The first argument of the \eqnote command is the original math expression, dont change it. the second argument is a comma separated list of all formalized concepts that appear in this expression. only list concepts, that were officially formalized in the formalized statements in input 2 and 4. Do not hallucinate. In the third argument, try to represent the math statement in its structure with formalized concepts only. Do not hallucinate. if you think the third representation is not possible, leave the brakets empty. See also the example in input 6.
Do not use latex code in the third argument!
Do not use latex code in the third argument!
If the third argument cannot be given by formalized objects only, leave it empty.
If the third argument cannot be given by formalized objects only, leave it empty.

With the first argument, always encapsulate the entire math part, like this:
\eqnote{
    \begin{equation}
        ...
    \end{equation}
}{concepts:...}{statement:...}
or
\eqnote{$...$}{concepts:...}{statement:...}

