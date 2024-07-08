- // snippet(1)
- New capter: 'Sets, Logic, Numbers, Relations, Orderings, Graphs, and Functions'.

- // snippet(2i)
- // ignored content

- // snippet(3)
- New section: 'Sets'.

- // snippet(4)
- There is a class: 'set'.
- There is a property: 'finite'.
- 'finite' is applicable to 'set'.
- There is a property: 'infinite'.
- 'infinite' is applicable to 'set'.

- // snippet(5)
- There is a property: 'countably infinite'.
- 'countably infinite' is applicable to 'set'.
- 'countably infinite' is a subproperty of 'infinite'.
- There is a relation: 'is in one-to-one correspondence with'.
- // The following statement is not directly given in the LaTeX source of this snippet but instead added from common mathematical knowledge because it makes sense to define the set of positive integers here (where it is used)
- 'positive integers' is an instance of 'set'.
- There is a property: 'countable'.
- 'countable' is applicable to 'set'.
- 'countable' has the definition:
    - OR
        - arg1 has the property 'finite'
        - arg1 has the property 'countably infinite'


- // snippet(6)
- There is a class: 'element'.
- There is a relation: 'is element of'.
- 'is element of' has the associated LaTeX notation `$arg1 \in arg2$`.
- There is a relation: 'is not element of'.
- 'is not element of' has the associated LaTeX notation `$arg1 \not\in arg2$`.

- There is a property: 'empty'.
- 'empty' is applicable to 'set'.
- There is a property: 'nonempty'.
- 'nonempty' is applicable to 'set'.

- // snippet(7)
- 'empty set' is an instance of 'set'.
- 'empty set' has the associated LaTeX notation `$\varnothing$`.
- 'empty set' has the verbal description "The set with no elements".

- // snippet(8)
- There is a binary operator: 'intersection'.
- The type of argument1 of 'intersection' is 'set'.
- The type of argument2 of 'intersection' is 'set'.
- The result type of 'intersection' is 'set'.
- 'intersection' has the associated LaTeX notation `$arg1 \cap arg2$`
- 'intersection' has defining formula `$\SX\cap \SY \isdef\{x\mspace{-1mu}\colon\ x\in \SX \mbox{ and } x\in \SY \}$`.
- 'intersection' has the verbal description "The intersection of arg1 and arg2 is the set of common elements of arg1 and arg2".

- // snippet(9)
- There is a binary operator: 'union'.
- The type of argument1 of 'union' is 'set'.
- The type of argument2 of 'union' is 'set'.
- The result type of 'union' is 'set'.
- 'union' has the associated LaTeX notation `$arg1 \cup arg2$`.
- 'union' has defining formula `$\SX \cup \SY \isdef\{x\mspace{-1mu}\colon\ x\in \SX \mbox{ or } x\in \SY \}$`.
- 'union' has the verbal description "The union of arg1 and arg2 is the set of elements in either arg1 or arg2".


- // snippet(10)
- There is a binary operator: 'binary complement'.
- // explanation: In the LaTeX source this is only called 'complement' but we use the label 'binary complement' to prevent confusion with 'unary complement' (see next snippet)
- 'binary complement' has the alternative label "complement".
- The type of argument1 of 'binary complement' is 'set'.
- The type of argument2 of 'binary complement' is 'set'.
- The result type of 'binary complement' is 'set'.
- 'binary complement' has the associated LaTeX notation `$arg1 \backslash arg2$`.
- 'binary complement' has defining formula `$\SY  \backslash\SX \isdef \{x \in \SY \mspace{-2mu}\colon\ x \not\in \SX \}$`.

- // snippet(11)
- There is a unary operator: 'unary complement'.
- 'unary complement' has the alternative label "complement".
- The type of argument1 of 'unary complement' is 'set'.
- The result type of 'unary complement' is 'set'.
- 'unary complement' has the associated LaTeX notation `$arg1^\sim$`.
- 'unary complement' has defining formula `$\SX^\sim \isdef \SY \backslash  \SX$`.
- // the challenge here is that arg2 of 'complement' must be taken from the context. Thus it is unsiutable to model this as a simple triple. At least this statement should have a qualifier ('arg2 depends on context')

- // snippet(12)
- There is a binary operator: 'symmetric difference'.
- The type of argument1 of 'symmetric difference' is 'set'.
- The type of argument2 of 'symmetric difference' is 'set'.
- The result type of 'symmetric difference' is 'set'.
- 'symmetric difference' has the associated LaTeX notation `$arg1 \ominus arg2$`.
- 'symmetric difference' has defining formula `$\SX\ominus \SY \isdef (\SX \cup \SY)\backslash(\SX \cap \SY)$`.
- 'symmetric difference' has the verbal description "The symmetric difference of X and Y is the set of elements that are in either X or Y but not both".

- // snippet(13)
- There is a relation: 'is subset of'.
- The type of argument1 of 'subset' is 'set'.
- The type of argument2 of 'subset' is 'set'.
- 'is subset of' has the associated LaTeX notation `$arg1 \subseteq arg2$`.
- 'is subset of' has the alternative associated LaTeX notation `$arg2 \supseteq arg1$`.
- // for 'subset' no defining formula is given
- 'is subset of' has the verbal description "If $x \in X$ implies that $x \in Y$, then $X$ is a subset of $Y$".
- 'is subset of' has the alternative verbal description "$Y$ contains $X$".

- // snippet(14)
- There is an equivalence-statement
    - full source code: "Note that $\SX \subseteq\SY$ if and only if $\SX\backslash\SY=\varnothing.$"
    - // from the context can be taken that X and Y are sets
    - source code of assertion: "$\SX \subseteq\SY$"
    - source code of premise: "$\SX\backslash\SY=\varnothing.$"
    - formalized premise:
        - There is an equation:
            - formalized left hand side
                - 'binary complement'(\SX, \SY)
            - formalized right hand side:
                - 'empty set'
    - formalized assertion:
        - $\SX$ 'is subset of' $\SY$

- // snippet(15)
- There is an equivalence-statement
    - full source code: "Furthermore, $\SX =\SY$ if and only if $\SX \subseteq \SY $ and $\SY \subseteq \SX $."
    - // from the context can be taken that X and Y are sets
    - source code of assertion: "$\SX =\SY$"
    - source code of premise: "$\SX \subseteq \SY $ and $\SY \subseteq \SX$"
    - // in a later processing stage we can determine that the premise consists of two conditions

- // snippet(16)
- There is a binary operator: 'proper subset'.
- The type of argument1 of 'proper subset' is 'set'.
- The type of argument2 of 'proper subset' is 'set'.
- The result type of 'proper subset' is 'set'.
- 'proper subset' has the associated LaTeX notation `$arg1 \subset arg2$`.
- 'proper subset' has the verbal description "If $\SX \subseteq \SY $ and $\SX \not= \SY $, then $\SX$ is a {\it proper subset} of $\SY$ and we write $\SX \subset \SY $".

- // snippet(17)
- There is a relation: 'is disjont to'.
- The type of argument1 of 'is disjont to' is 'set'.
- The type of argument2 of 'is disjont to' is 'set'.
- 'is disjoint to' has the verbal description "The sets $\SX$ and $\SY$ are {\it disjoint} if $\SX \cap \SY =\varnothing\mspace{-1mu}.$".

- // snippet(18)
- There is a class: 'partition'.
- 'partition' is a subclass of 'set'.
- 'partition' has the verbal description "A partition of X is a set of pairwise-disjoint and nonempty subsets of X whose union is equal to X".
- // the following association statements are a supplement for not having a semantical definition yet
- 'partition' is associated with 'is disjont to'.
- 'partition' is associated with 'nonempty'.
- 'partition' is associated with 'subset'.
- 'partition' is associated with 'union'.

- // snippet(19)
- 'nonnegative integers' is an instance of 'set'.
- 'nonnegative integers' has the associated LaTeX notation `$\BBN$`.
- 'positive integers' is an instance of 'set'.
- 'positive integers' has the associated LaTeX notation `$\BBP$`.
- 'integers' is an instance of 'set'.
- 'integers' has the associated LaTeX notation `$\BBZ$`.
- 'rational numbers' is an instance of 'set'.
- 'rational numbers' has the associated LaTeX notation `$\BBQ$`.
- 'real numbers' is an instance of 'set'.
- 'real numbers' has the associated LaTeX notation `$\BBR$`.

- // snippet(20)
- There is an equation:
    - full source code: '$\{x,x\}=\{x\}.$'
    - left hand side: '$\{x,x\}$'
    - right hand side: '$\{x\}$'
    - // explanation: From the context can be taken that `\{x,x\}` and \{x\} are instances of 'set'. This statement expresses that a set with twice the element x is equal to the set with element x. This implicitly expresses that a set cannot have repeated elements. However, this information is not given explicitly.

- // snippet(21)
- There is a class: 'multiset'.
- 'multiset' has the verbal description "A multiset is a finite collection of elements that allows for repetition.".
- 'multiset' has the associated LaTeX notation `$\{arg1\}_{\rmms}`.
- // explanation: `arg1` represents the elements of the multiset.

- // snippet(22i)
- // ignored content

- // snippet(23)
- // This statement expresses that the operators 'intersection', 'union', 'binary complement', 'symmetric difference', 'Cartesian product' and the relations 'proper subset' and 'subset' can also be applied to the class 'multiset'. To model this we have to amend (generalize) the defining statements for those
- There is a class: 'generalized set'.
- 'multiset' is a subclass of 'generalized set'
- 'set' is a subclass of 'multiset'
- Amend definition of 'intersection':
    - replace 'set' by 'generalized set'
// please continue

- Amend definition of 'union':
    - replace 'set' by 'generalized set'
- Amend definition of 'binary complement':
    - replace 'set' by 'generalized set'
- Amend definition of 'symmetric difference':
    - replace 'set' by 'generalized set'
- Amend definition of 'subset':
    - replace 'set' by 'generalized set'
- Amend definition of 'proper subset':
    - replace 'set' by 'generalized set'
- // snippet(24)
- There is an equation:
    - // this is used as example
    - full source code: '$\{x,x\}_{\rmms}\cup\{x\}_{\rmms} =\{x,x,x\}_{\rmms}$'
    - left hand side: '$\{x,x\}_{\rmms}\cup\{x\}_{\rmms}$'
    - right hand side: '$\{x,x,x\}_{\rmms}$'
    - // explanation: From the context can be taken that '$\{x,x\}_{\rmms}$', '$\{x\}_{\rmms}$' and '$\{x,x,x\}_{\rmms}$' are instances of 'multiset'. This statement illustrates the application of the operator 'union' to instances of 'multiset'.

- // snippet(25)
- // The first sentence expresses that there is a mapping from the class 'multiset' to the class 'set'. However, this mapping is not defined explicitly.
- // The second sentence expresses that there is a mapping from the class 'set' to the class 'multiset'. However, this mapping is not defined explicitly.
- 'set' is a subclass of 'multiset'.
- // explanation: This statement was already given in snippet(23). However, here it is given again from a different perspective.

- // snippet(26)
- There is a binary operator: 'Cartesian product'.
- 'Cartesian product' has the associated LaTeX notation `$arg1 \times arg2$`.
- 'Cartesian product' has the alternative associated LaTeX notation `$\varprod_{i=1}^n arg1$`.
- // explanation: `arg1` represents a sequence of sets.
- The type of argument1 of 'Cartesian product' is 'generalized set'.
- The type of argument2 of 'Cartesian product' is 'generalized set'.
- The result type of 'Cartesian product' is 'generalized set'.
- 'Cartesian product' has the verbal description "The Cartesian product  X_1 ×⋯× X_n  of sets  X_1,…,X_n  is the set consisting of tuples of the form  (x_1,…,x_n) , where, for all  i∈{1,…,n},  x_i∈X_i.".
- There is a class: 'tuple'.
- 'tuple' has the associated LaTeX notation `$(arg1)$`.
- // explanation: `arg1` represents the components of the tuple.
- 'tuple' has the alternative label "n-tuple".
- 'tuple' has the verbal description "A tuple with n components is an n-tuple".

- // snippet(27)
- // The first sentence expresses that there is a mapping from the class 'tuple' to the class 'multiset'. However, this mapping is not defined explicitly.
- 'tuple' is a subclass of 'multiset'.
- There is a property: 'ordered'.
- 'ordered' is applicable to 'multiset'.
- // express that every tuple is ordered (this is implictly stated)
- There is an if-then-statement:
    - formalized premise:
        - $T$ 'is instance of' 'tuple'.
    - formalized assertion:
        - $T$ has the property 'ordered'

- // snippet(28)
- There is an equation:
    - reference: 'ref_eq1'
    - full source code: `$(x_1,\ldots, x_n)\in{\textstyle\varprod_{i=1}^n} \SX_i \isdef \SX_1\mspace{-2mu} \times\cdots \times \SX_n.`
    - // explanation: This statement defines that a tuple is an element of the Cartesian product of sets.
- 'ref_eq1' is associated to 'Cartesian product'
- 'Cartesian product' has the alternative associated LaTeX notation `${\textstyle\varprod_{i=1}^n} arg1$`.
- There is an equation:
    - reference: 'ref_eq2'
    - full source code: `$\SX^n$ denotes $\varprod_{i=1}^n \SX.$`
    - left hand side: `$\SX^n$`
    - right hand side: `$\varprod_{i=1}^n \SX.$`
    - // explanation: This statement defines a shorthand notation for the Cartesian product if all sets are equal.
- 'ref_eq2' is associated to 'Cartesian product'
- 'Cartesian product' has the alternative associated LaTeX notation `$arg1^n$`.
- // explanation: `arg1` represents a set.

- // snippet(29)
- There is a class: 'sequence'.
- 'sequence' has the associated LaTeX notation `$(arg1)^{\infty}_{i=1}$`.
- // explanation: `arg1` represents the components of the tuple.
- 'sequence' has the alternative associated LaTeX notation `$(arg1, arg2, \ldots)$`.
- // explanation: `arg1` and `arg2` represent the first two components of the tuple.
- 'sequence' has the verbal description "A sequence (x1,x2,…) is a tuple with a countably infinite number of components.".
- 'sequence' is a subclass of 'tuple'.
- There is a class: 'subsequence'.
- 'subsequence' is a subclass of 'sequence'.
- 'subsequence' has the verbal description "A subsequence $A$ of a sequence $B$ contains a subset of its elements.".

- // snippet(30i)
- // ignored content
- // Informal summary: This snippet explains the notion of 'subset' and 'proper subset' for sequences. However, this is already clear since 'sequence' is a subclass of 'multiset' (via the class 'tuple')

- // snippet(31)
- There is a binary operator: 'sequence addition'.
- 'sequence addition' has the associated LaTeX notation '$arg1 + arg2$'.
- 'sequence addition' has defining formula '$X + Y\isdef (x_i + y_i)_{i=1}^\infty$'.
- // explanation: It is not explicitly stated that X and Y are sequences. However, this can be taken from the context.
- // explanation: It is not explicitly stated that '+' on the right hand side of the defining formula means component-wise addition. However, this can be taken from the context.
- There is a binary operator: 'sequence component-wise multiplication'.
- 'sequence component-wise multiplication' has the associated LaTeX notation '$arg1 \odot arg2$'.
- 'sequence component-wise multiplication' has defining formula '$X\odot Y\isdef (x_i\odot y_i)_{i=1}^\infty$'.
- // explanation: Same remarks as for 'sequence addition'
- There is a binary operator: 'sequence scalar multiplication'.
- 'sequence scalar multiplication' has the associated LaTeX notation '$arg1 arg2$'.
- 'sequence scalar multiplication' has defining formula '$XY\isdef (x_i y_i)_{i=1}^\infty$'.
- // explanation: Same remarks as for 'sequence addition'

- // snippet(32i)
- // ignored content

- // snippet(33)
- New section: 'Logic'.

- // snippet(34)
- There is a class: 'statement'.
- 'statement' has the verbal description "Every statement is either true or false, and no statement is both true and false."
