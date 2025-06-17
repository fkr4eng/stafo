- // snippet (1)
- There is a class: 'memristor stack'
- There is a class: 'stack component'

- There is a relation: 'has stack component'
- The type of argument1 of 'has stack component' is 'memristor stack'
- The result type of 'has stack component' is 'stack component'

- There is a relation: 'has position'
- The result type of 'has position' is 'integer number'
- 'has position' is a qualifier.

- There is a relation: 'is at outer position'
- 'is at outer position' is a qualifier.


- 'stack1' is an instance of 'memristor stack'
- 'stack2' is an instance of 'memristor stack'
- 'Ti' is an instance of 'stack component'
- 'stack1' 'has stack component' 'Ti' qqq 'has position' 0, 'is at outer position': True, qqq 'has position' 3,  'is at outer position': True
- 'stack2' 'has stack component' 'Ti' qqq 'has position' 0
- 'stack2' 'has stack component' 'Ti' qqq 'is at outer position' True

<!-- set the same thing again, should not produce a duplicate -->
- 'stack1' 'has stack component' 'Ti' qqq 'has position' 0, 'is at outer position': True

- There is an if-then-statement:
    - formalized setting:
        - 's' is an instance of 'memristor stack' qqq univ_quant True
        - 'k' is an instance of 'memristor stack' qqq exis_quant True
        - 'c' is an instance of 'stack component'
        - 's' 'has stack component' 'c' qqq univ_quant True
        <!-- this next statement does not make sense, it should test if the object of a qualifier relation can be a local variable -->
        - 's' 'has stack component' 'c' qqq 'is at outer position' 'c'
