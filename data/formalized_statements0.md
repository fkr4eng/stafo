- // snippet(1i)
- // snippet(1)
- test2
- // snippet(1)
- There is a class: 'set'.
- There is a property: 'finite'.
- 'finite' is applicable to 'set'.
- There is a property: 'infinite'.
- 'infinite' is applicable to 'set'.

- // snippet(2)
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


- // snippet(3)
- There is a class: 'element'.
- There is a relation: 'is element of'.
- 'is element of' has the associated LaTeX notation `$arg1 \in arg2$`.
- There is a relation: 'is not element of'.
- 'is not element of' has the associated LaTeX notation `$arg1 \not\in arg2$`.

- There is a property: 'empty'.
- 'empty' is applicable to 'set'.
- There is a property: 'nonempty'.
- 'nonempty' is applicable to 'set'.

- // snippet(4)
- 'empty set' is an instance of 'set'.
- 'empty set' has the associated LaTeX notation `$\varnothing$`.
- 'empty set' has the verbal description "The set with no elements".

- // snippet(5)
- There is a binary operator: 'intersection'.
- The type of argument1 of 'intersection' is 'set'.
- The type of argument2 of 'intersection' is 'set'.
- The result type of 'intersection' is 'set'.
- 'intersection' has the associated LaTeX notation `$arg1 \cap arg2$`
- 'intersection' has defining formula `$\SX\cap \SY \isdef\{x\mspace{-1mu}\colon\ x\in \SX \mbox{ and } x\in \SY \}$`.
- 'intersection' has the verbal description "The intersection of arg1 and arg2 is the set of common elements of arg1 and arg2".
