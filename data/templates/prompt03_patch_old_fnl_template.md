Your task is to extract the formalized concepts and list them.

# Input 1: The previously formalized statements.

````
{{context.fnl_statements}}
````

# Input 2: The current snippet you are working on.

````
{{context.current_snippet}}
````

# Input 3: The output format.

````
- Concepts in this snippet:
    - '<arg1>'
    - '<arg2>'
- Defined in this snippet:
    - '<arg1>'
````

# Input 4: Final instructions.
Extract all concepts (classes, relations, properties, etc.) given in the current snippet and return them formatted as in input 3.
Distinguish between concepts, that were defined in this snippet (usually indicatd by "There is a class:" or similar), those should be listed under "Defined in this snippet", and all concepts that occur in this snippet, those should be listed under "Concepts in this snippet". Keep in mind that the second category includes concepts that were defined in the snippet and also concepts, that occur inside nested statements.
Only use the formalized names, no language alternatives. Dont use equations.
Dont add any `` to indicate code. set all concepts in tick marks ('')

