
- // snippet(1i)
- // ignored content

- // manually added 1
- There is a class: 'set' @en
- 'set' has the alternative german label 'Menge'
- There is a relation: 'is subset of'
- The type of argument1 of 'is subset of' is 'set'
- The result type of 'is subset of' is 'set'
- There is a relation: 'has element'
- The type of argument1 of 'has element' is 'set'
- There is a relation: 'has element type'
- 'has element type' has the verbal description 'specifies what types of elements appear in this set'
- The type of argument1 of 'has element type' is 'set'
- There is a binary operator: 'element of sequence'
- There is a class: 'sequence'
- The type of argument1 of 'element of sequence' is 'sequence'

- // snippet(2)
- New section: "Lineare Algebra".

- // snippet(3)
- There is a class: 'real number' @en
- 'real number' has the alternative german label 'reelle Zahl'
- There is a class: 'set of real numbers' @en
- 'set of real numbers' is an instance of 'set'
- 'set of real numbers' has the associated LaTeX notation $\mathbb{R}$.
- 'set of real numbers' has the alternative german label 'Menge der reellen Zahlen'

- // manually added 2
- There is a class: 'integer number'
- 'integer number' is a subclass of 'real number'
- 'integer number' has the alternative german label 'Natürliche Zahl'

- // snippet(4)
- There is a class: 'vector space' @en
- 'vector space' has the alternative german label 'Vektorraum'
- 'vector space' is an instance of 'set'
- There is a class: 'n-dimensional real vector space' @en
- 'n-dimensional real vector space' has the associated LaTeX notation $\mathbb{R}^n$
- 'n-dimensional real vector space' has the alternative german label '$n$-dimensionaler reeller Vektorraum'
- 'n-dimensional real vector space' is an instance of 'vector space'
- There is a class: 'vector' @en
- 'vector' has the alternative german label 'Vektor'
- 'vector space' 'has element type' 'vector'
- There is a relation: 'has dimension'
- The type of argument1 of 'has dimension' is 'vector space'
- The result type of 'has dimension' is 'integer number'

- // snippet(5)
- There is a class: 'vector component' @en
- 'vector component' has the alternative german label 'Vektorkomponente'
- 'vector component' is an instance of 'real number'
- There is a relation: 'has vector component'
- The type of argument1 of 'has vector component' is 'vector'
- The result type of 'has vector component' is 'vector component'
- There is a class: 'column vector' @en
- 'column vector' has the alternative german label 'Spaltenvektor'
- 'column vector' is an instance of 'vector'
- 'column vector' has the associated LaTeX notation $\left(\begin{array}{c} x_1 \\ \vdots \\ x_n \end{array}\right)$

- // snippet(6)
- There is a class: 'row vector' @en
- 'row vector' has the alternative german label 'Zeilenvektor'
- 'row vector' is an instance of 'vector'
- 'column vector' has the alternative german label 'kontravarianter Vektor'
- 'column vector' has the alternative label 'contravariant vector'

- // snippet(7)
- There is a class: 'unit vector' @en
- 'unit vector' has the alternative german label 'Einheitsvektor'
- 'unit vector' is an instance of 'vector'
- There is a class: 'basis'
- 'basis' is an instance of 'set'
- There is a class: 'canonical basis' @en
- 'canonical basis' has the alternative german label 'kanonische Basis'
- 'canonical basis' is an instance of 'basis'
- 'canonical basis' has the associated LaTeX notation $e_1, \dots, e_n$ where $e_i$ has $i$-th component equal to 1 and all other components equal to zero.
- 'canonical basis' has the alternative german label 'Standardbasis'
- There is a general statement:
    - formalized setting:
        - 'n' is an instance of 'integer number'
        - 'Rn' is an instance of 'n-dimensional real vector space'
        - 'Rn' 'has dimension' 'n'
    - formalized assertion
        - 'b' is an instance of 'canonical basis'
        - 'b' 'is subset of' 'Rn'
        - 's' is an instance of 'set'
        - 's' 'has element type' 'unit vector'
        - 's' has the verbal description 'set of all n unit vectors'
        - There is an equation:
            - full source code: 'b' = 's'

- // snippet(8)
- There is a general statement:
    - full source code: Jeder Vektor~(\ref{eq:vektor-x}) lässt sich eindeutig als Linearkombination der Basisvektoren darstellen: $x=x_{1}e_{1}+\cdots+x_{n}e_{n}$.
    - formalized setting:
        - 'x' is an instance of 'vector'
        - 'b' is an instance of 'basis'
        - 'n' is an instance of 'integer number'
        - 'i' is an instance of 'integer number'
    - formalized assertion:
        - There is an equation:
            - full source code: $x=x_{1}e_{1}+\cdots+x_{n}e_{n}$
            - formalized left hand side: x
            - formalized right hand side: \sum_{i=1}^n 'element of sequence'(x, i) * 'element of sequence'(b, i)
- // comment: the word "eindeutig" in the german text is important. It means that the linear combination is unique. This aspect is not captured by the formalized statements yet. It might be possible to express this by adding another general statement which says that if there are two such linear combinations, then they must be equal.

- There is a general statement:
    - full source code:  If a vector x can be represented as two linear combinations of basis vectors, these linear combinations must be identical.
    - formalized setting:
        - 'x' is an instance of 'vector'
        - 'b' is an instance of 'basis'
        - 'n' is an instance of 'integer number'
        - 'i' is an instance of 'integer number'
        - 'c' is an instance of 'sequence'  // Represents coefficients
        - 'd' is an instance of 'sequence'  // Represents another set of coefficients
        - There is an equation:
            - full source code: x = \sum_{i=1}^n 'element of sequence'(c, i) * 'element of sequence'(b, i)
        - There is an equation:
            - full source code: x = \sum_{i=1}^n 'element of sequence'(d, i) * 'element of sequence'(b, i)
    - formalized assertion:
        - For all 'i' from 1 to 'n':
            - There is an equation:
                - full source code: 'element of sequence'(c, i) = 'element of sequence'(d, i)


