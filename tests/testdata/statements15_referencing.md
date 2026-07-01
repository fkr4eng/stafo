- There is a class: 'real number'
- There is a relation: 'has proof'
- There is a property: 'prop'

- There is an equivalence-statement (test theorem):
    - formalized setting:
        - 'a' is an instance of 'real number'.
        - 'b' is an instance of 'real number'.
    - formalized premise:
        - There is an equation:
            - full source code: 'a' == 2 * 'b'
    - formalized assertion:
        - There is an equation:
            - full source code: 2 * 'a' == 4 * 'b'

- There is an if-then-statement (Proof => of test theorem):
    - formalized setting:
        - 'a' is an instance of 'real number'.
        - 'b' is an instance of 'real number'.
    - formalized premise:
        - There is an equation:
            - full source code: 'a' == 2 * 'b'
    - formalized assertion:
        - There is an equation:
            - full source code: 2 * 'a' == 4 * 'b'

- There is an if-then-statement (Proof <= of test theorem):
    - formalized setting:
        - 'a' is an instance of 'real number'.
        - 'b' is an instance of 'real number'.
    - formalized premise:
        - There is an equation:
            - full source code: 2 * 'a' == 4 * 'b'
    - formalized assertion:
        - There is an equation:
            - full source code: 'a' == 2 * 'b'

- 'test theorem' 'has proof' 'Proof => of test theorem'
- 'test theorem' 'has proof' 'Proof <= of test theorem'

- There is a general statement ('stm2'):
    - formalized setting:
        - 'a' is an instance of 'real number'.
        - 'b' is an instance of 'real number'.
    - formalized premise:
        - There is an equation ('double'):
            - full source code: 'a' == 2 * 'b'
    - formalized assertion:
        - 'double' 'has the property' 'prop'