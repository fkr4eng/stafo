- There is a binary operator: 'element of sequence'
- There is a class: 'sequence'
- The type of argument1 of 'element of sequence' is 'sequence'
- The type of argument2 of 'element of sequence' is 'integer number'
- There is a relation: 'is element of'
- Applying 'element of sequence' creates relation: result 'is element of' argument1

- There is a class: 'linear map'
- There is a unary operator: 'kernel op'
- The type of argument1 of 'kernel op' is 'linear map'
- Applying 'kernel op' creates relation: result 'is secondary instance of' 'vector space'

- There is a general statement:
    - formalized setting:
        - 'f' is an instance of 'sequence'
        - 'i' is an instance of 'integer number'
        - 'y' is an instance of 'integer number'
    - formalized assertion:
        - There is an equation:
            - formalized left hand side: 'y'
            - formalized right hand side: 'element of sequence'('f', 'i')

- There is a general statement:
    - formalized setting:
        - 'A' is an instance of 'linear map'
        - 'K' is an instance of 'vector space'
    - formalized assertion:
        - There is an equation:
            - formalized left hand side: 'K'
            - formalized right hand side: 'kernel op'('A')
