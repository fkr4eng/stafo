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
- The result type of 'is at outer position' is 'bool'
- 'is at outer position' is a qualifier.


- 'stack1' is an instance of 'memristor stack'
- 'stack2' is an instance of 'memristor stack'
- 'Ti' is an instance of 'stack component'
- 'stack1' 'has stack component' 'Ti' qq: 'has position' 0, 'is at outer position': True, qq: 'has position' 3,  'is at outer position': True
- 'stack2' 'has stack component' 'Ti' qq: 'has position' 0
- 'stack2' 'has stack component' 'Ti' qq: 'is at outer position' True

<!-- set the same thing again, should not produce a duplicate -->
- 'stack1' 'has stack component' 'Ti' qq: 'has position' 0, 'is at outer position': True