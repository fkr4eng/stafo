This document describes how the LaTeX source code of the book "Matrix Mathematics" by Dennis S. Bernstein should be transformed such that it can be converted into a knowledge graph.

# Preliminaries

I chose a text based representation (collection of statements) because I think it is both easier to produce/update for me and for an LLM. It is probably also easier to understand compared to a mock up graph. A collection of formalized statements like this should be easy to convert to a RDF-based knowledge graph.

Currently I only covered a part of Section 1.1. I probably will continue soon.

We assume the following concepts to be already defined (or given as builtins): *class*, *relation*, *property*, *subproperty*, *binary operator*, *argument1*, *argument2*, *applicable*, *associated LaTeX notation*, *defining formula*.

The following types of statements are allowed:

- There is a class: arg1.
- There is a property: arg1.
- There is a relation: arg1.
- There is a unary operator: arg1.
- There is a binary operator: arg1.
- arg1 is applicable to arg2.
- arg1 is a subproperty of arg2.
- arg1 is an instance of arg2.
- arg1 is a subclass of arg2.
- arg1 has the associated LaTeX notation arg2.
- arg1 has the alternative associated LaTeX notation arg2.
- arg1 has defining formula arg2
- The type of argument1 of arg1 is arg2.
- The type of argument2 of arg1 is arg2.
- The result type of arg1 is arg2.
- arg1 has the verbal description arg2.
- arg1 hast the alternative label arg2.
- // this is a comment to explain modeling decisions (it would be suitable if the LLM also could generate comments to explain its "chain of thought")
- There is an equivalence statement
    - full source code: arg1
    - source code of assertion: arg1
        - // the assertion is the part before "if and only if"
    - source code of premise: arg2
        - // the premise is the part after "if and only if"
- arg1 is associate with arg2

# Section 1.1 represented in formalized language

- There is a class: 'set'.

- There is a property: 'finite'.
- There is a property: 'infinite'.
- There is a property: 'countably infinite'.
- There is a property: 'countable'.
- There is a property: 'empty'.
- There is a property: 'nonempty'.

- 'finite' is applicable to 'set'.
- 'infinite' is applicable to 'set'.
- 'countably infinite' is applicable to 'set'.
- 'countable' is applicable to 'set'.
- 'empty' is applicable to 'set'.
- 'nonempty' is applicable to 'set'.

- 'countably infinite' is a subproperty of 'infinite'.
- 'positive integers' is an instance of 'set'.
- 'empty set' is an instance of 'set'.
- 'empty set' has the associated LaTeX notation `$\varnothing$`.
- 'empty set' has the verbal description "The set with no elements".

- There is a class: 'element'.
- There is a relation: 'is element of'.
- 'is element of' has the associated LaTeX notation `$arg1 \in arg2$`.
- There is a relation: 'is not element of'.
- 'is not element of' has the associated LaTeX notation `$arg1 \not\in arg2$`.
- There is a relation: 'is in one-to-one correspondence with'.

- There is a binary operator: 'intersection'.
- The type of argument1 of 'intersection' is 'set'.
- The type of argument2 of 'intersection' is 'set'.
- The result type of 'intersection' is 'set'.
- 'intersection' has the associated LaTeX notation `$arg1 \cap arg2$`
- 'intersection' has defining formula `$\SX\cap \SY \isdef\{x\mspace{-1mu}\colon\ x\in \SX \mbox{ and } x\in \SY \}$`.
- 'intersection' has the verbal description "The intersection of arg1 and arg2 is the set of common elements of arg1 and arg2".

- There is a binary operator: 'union'.
- The type of argument1 of 'union' is 'set'.
- The type of argument2 of 'union' is 'set'.
- The result type of 'union' is 'set'.
- 'union' has the associated LaTeX notation `$arg1 \cup arg2$`.
- 'union' has defining formula `$\SX \cup \SY \isdef\{x\mspace{-1mu}\colon\ x\in \SX \mbox{ or } x\in \SY \}$`.
- 'union' has the verbal description "The union of arg1 and arg2 is the set of elements in either arg1 or arg2".

### Page 4 (work in progress)

- There is a binary operator: 'complement'.
- The type of argument1 of 'complement' is 'set'.
- The type of argument2 of 'complement' is 'set'.
- The result type of 'complement' is 'set'.
- 'complement' has the associated LaTeX notation `$arg1 \backslash arg2$`.
- 'complement' has defining formula `$\SY  \backslash\SX \isdef \{x \in \SY \mspace{-2mu}\colon\ x \not\in \SX \}$`.

- There is a unary operator: 'unary complement'.
- 'unary complement' has the alternative label "complement".
- The type of argument1 of 'unary complement' is 'set'.
- The result type of 'unary complement' is 'set'.
- 'unary complement' has the associated LaTeX notation `$arg1^\sim$`.
- 'unary complement' has defining formula `$\SX^\sim \isdef \SY \backslash  \SX$`.
- // the challenge here is that arg2 of 'complement' must be taken from the context. Thus it is unsiutable to model this as a simple triple. At least this statement should have a qualifier ('arg2 depends on context')

- There is a binary operator: 'symmetric difference'.
- The type of argument1 of 'symmetric difference' is 'set'.
- The type of argument2 of 'symmetric difference' is 'set'.
- The result type of 'symmetric difference' is 'set'.
- 'symmetric difference' has the associated LaTeX notation `$arg1 \ominus arg2$`.
- 'symmetric difference' has defining formula `$\SX\ominus \SY \isdef (\SX \cup \SY)\backslash(\SX \cap \SY)$`.
- 'symmetric difference' has the verbal description "The symmetric difference of X and Y is the set of elements that are in either X or Y but not both".

- There is a binary operator: 'subset'.
- The type of argument1 of 'subset' is 'set'.
- The type of argument2 of 'subset' is 'set'.
- The result type of 'subset' is 'set'.
- 'subset' has the associated LaTeX notation `$arg1 \subseteq arg2$`.
- 'subset' has the alternative associated LaTeX notation `$arg2 \supseteq arg1$`.
- // for 'subset' no defining formula is given
- 'subset' has the verbal description "If $x \in X$ implies that $x \in Y$, then $X$ is a subset of $Y$".
- 'subset' has the alternative verbal description "$Y$ contains $X$".

- There is an equivalence-statement
    - full source code: "Note that $\SX \subseteq\SY$ if and only if $\SX\backslash\SY=\varnothing.$"
    - // from the context can be taken that X and Y are sets
    - source code of assertion: "$\SX \subseteq\SY$"
    - source code of premise: "$\SX\backslash\SY=\varnothing.$"
    - // in a later processing stage we can determine that this statement relates the items 'subset', 'complement' and 'empty set'
    - formalized setting:
        - SX is instance of set
        - SY is instance of set
    - formalized premise:
        - There is an equation:
            - formalized left hand side: 'binary complement'(\SX, \SY)
            - formalized right hand side: 'empty set'
    - formalized assertion:
        - $\SX$ 'is subset of' $\SY$

- There is an equivalence-statement
    - full source code: "Furthermore, $\SX =\SY$ if and only if $\SX \subseteq \SY $ and $\SY \subseteq \SX $."
    - // from the context can be taken that X and Y are sets
    - source code of assertion: "$\SX =\SY$"
    - source code of premise: "$\SX \subseteq \SY $ and $\SY \subseteq \SX$"
    - formalized setting:
        - SX is instance of set
        - SY is instance of set
    - formalized premise:
        - AND:
            - SX 'is subset of' SY
            - SY 'is subset of' SX
    - formalized assertion:
        - There is an equation:
            - formalized left hand side: SX
            - formalized right hand side: SY

- There is a binary operator: 'proper subset'.
- The type of argument1 of 'proper subset' is 'set'.
- The type of argument2 of 'proper subset' is 'set'.
- The result type of 'proper subset' is 'set'.
- 'proper subset' has the associated LaTeX notation `$arg1 \subset arg2$`.
- 'proper subset' has the verbal description "If $\SX \subseteq \SY $ and $\SX \not= \SY $, then $\SX$ is a {\it proper subset} of $\SY$ and we write $\SX \subset \SY $".

- There is a relation: 'is disjont to'.
- The type of argument1 of 'is disjont to' is 'set'.
- The type of argument2 of 'is disjont to' is 'set'.
- 'is disjoint to' has the verbal description "The sets $\SX$ and $\SY$ are {\it disjoint} if $\SX \cap \SY =\varnothing\mspace{-1mu}.$".

- There is a class: 'partition'.
- 'partition' is a subclass of 'set'.
- 'partition' has the verbal description "A partition of X is a set of pairwise-disjoint and nonempty subsets of X whose union is equal to X".
- // the following association statements are a supplement for not having a semantical definition yet
- 'partition' is associated with 'is disjont to'.
- 'partition' is associated with 'nonempty'.
- 'partition' is associated with 'subset'.
- 'partition' is associated with 'union'.


---

For simplicity some information is not represented by the above statements:

- property 'countable': finite or countably infinite
- Assertion: No set can be an element of itself
- Implicit Assertion as triple: ('empty set', 'has number of elements', 0)

---

## General Modelling Questions

- how to model examples?
- how to model repetitions of already established knowledge (but phrased in different words). Examples:
- how to model equations with multiple equality signs? E.g. which demonstrate stepwise simplification?
    - Therefore, $A$ and $B$ are equivalent if and only if either both $A$ and $B$
are true or both $A$ and $B$ are false.
- how to model prose explanations? Example:
    - In order to visualize logic operations on predicates, it is helpful to replace statements with sets and logic operations by set operations; the truth of a statement can then be visualized in terms of Venn diagrams.

## Mathematical (Modelling) Questions

Is there just *one* empty set? In other words: Are all empty sets identical or just equivalent?
Are {3, 2} = {2, 3} the same set? Because: "a tuple can be viewed as an ordered multiset"
