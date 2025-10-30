You are an expert in control theory and have to critically review to formalization of a textbook into "formalized natural language".

Your task is to evaluate the given convertion of the latex source document to formalized natural language. You are only concerned about the last converted snippet. Decide wheter the content is correct or whether it needs to be improved (see Part 2).

The original text is in german. Your input data consists of several parts which are separated by `----`. Each part has a different meaning. In the formalized statements "arg1" and "arg2" are placeholders (i.e. variables) for specific values. In the abstract examples in Input Part 1 the strings "<arg1>", "<arg2>" etc. serve as such placeholders.

----

# Input Part 1: Description of allowed formalized statements

All statements are represented as a bullet list in markdown syntax. There are two general types of formalized statements: Simple Formalized Statements and Complex Formalized Statements.

## Simple Formalized Statements

Simple Formalized Statements consist of one line. They are not followed by a line with a higher indentation level. The following Simple Formalized Statements are allowed:

- // This is a comment to explain modeling decisions. It is an arbitrary single line string.
- New chapter: <arg1>.
- New section: <arg1>.
- New subsection: <arg1>.
- There is a class: <arg1>.
- There is a property: <arg1>.
- There is a relation: <arg1>.
- There is a general operator: <arg1>.
- There is a unary operator: <arg1>.
- There is a binary operator: <arg1>.
- <arg1> is applicable to <arg2>.
- <arg1> is a subproperty of <arg2>.
- <arg1> is an instance of <arg2>.
- <arg1> is a subclass of <arg2>.
- <arg1> has the associated LaTeX notation <arg2>.
- <arg1> has the alternative associated LaTeX notation <arg2>.
- <arg1> has defining formula <arg2>
- The type of argument1 of <arg1> is <arg2>.
- The type of argument2 of <arg1> is <arg2>.
- The result type of <arg1> is <arg2>.
- <arg1> has the verbal description <arg2>.
- <arg1> has the property <arg2>.
- <arg1> is associated to <arg2>.
- <arg1> has the alternative english label <arg2>.
- <arg1> has the alternative german label <arg2>.
- Concepts in this snippet:
    - <arg1>
    - <arg2>
- Definied in this snippet:
    - <arg1>
    - <arg2>

Behind the definition of new objects, such as class, property, relation, unary operator, binary operator, you specify the language the name is in by adding @en for english and @de for german.

## Complex Formalized Statements

Complex Formalized Statements consists of multiple lines which correspond to one list item of the current level followed at least one sub-list. The sub-list can consist of Simple Formalized Statements or Complex Formalized Statements. Thus, a Complex Formalized Statement contains lines with at least two indentation levels.

It might be possible that there is not enough infomation to completely generate all aspects of a Complex Fomalized Statement. Please do as best as you can and explain doubts and problems via comments.

The following Complex Formalized Statements are allowed:

- // The following starts a definition statement which can contain either one OR or one AND block. Such blocks can be nested which is represented by their indentation level. Each condition may be preceded by NOT to indicate the negation of the following condition.
- Definition of <arg1>:
    - full source code: <arg1>
    - formalized setting:
        - <expression1>
        - // the setting should define all variables that will be used in the following premise and assertion block
        - // the setting might be empty
    - formalized premise:
        - <condition1>
        - // The condition can consist of (nested) 'OR' and 'AND'-blocks.
        - // the premise might be empty
    - formalized assertion:
        - <condition2>
        - // same as for the premise: The condition can consist of (nested) 'OR' and 'AND'-blocks.

- There is a general statement:
    - full source code: <arg1>
    - formalized setting:
        - <expression1>
        - // the setting should define all variables that will be used in the following premise and assertion block
        - // the setting might be empty
    - formalized premise:
        - <condition1>
        - // The condition can consist of (nested) 'OR' and 'AND'-blocks.
        - // the premise might be empty
    - formalized assertion:
        - <condition2>
        - // same as for the premise: The condition can consist of (nested) 'OR' and 'AND'-blocks.

- There is an equivalence-statement:
    - full source code: <arg1>.
    - // the assertion is the part before "genau dann wenn"
    - source code of assertion: <arg2>.
    - // the premise is the part after "genau dann wenn"
    - source code of premise: <arg3>.
    - // the following is optional (there might be no enough information)
    - formalized setting:
        - <expression1>
        - // the setting should define all variables that will be used in the following premise and assertion block
        - // the setting might be empty
    - formalized premise:
        - <condition1>
        - // The condition can consist of (nested) 'OR' and 'AND'-blocks.
    - formalized assertion:
        - <condition2>
        - // same as for the premise: The condition can consist of (nested) 'OR' and 'AND'-blocks.

- There is an if-then-statement:
    - full source code: <arg1>.
    - // the assertion is the part before "wenn"
    - // the premise is the part after "wenn"
    - formalized setting:
        - <expression1>
        - // the setting should define all variables that will be used in the following premise and assertion block
        - // the setting might be empty
    - source code of premise: <arg1>.
    - source code of assertion: <arg1>.
    - // the following is optional (there might be no enough information)
    - formalized premise:
        - <condition1>
        - // The condition can consist of (nested) 'OR' and 'AND'-blocks.
    - formalized assertion:
        - <condition2>
        - // same as for the premise: The condition can consist of (nested) 'OR' and 'AND'-blocks.

- // The following equation statement can only be used as part of a formalized setting, premise or assertion of one of the previous statements.
- There is an equation:
    - full source code: <arg1>.
    - source code of left hand side: <arg2>.
    - source code of right hand side: <arg3>.
    - formalized left hand side: <expression1>
    - formalized right hand side: <expression2>.
    - // for the formalized expression, the following symbols are allowed: + (addition), - (subtraction), * (multiplication), / (division), ** (power)

- // The following equation statement can only be used as part of a formalized setting, premise or assertion of one of the previous statements.
- There is a system of equations:
    - There is an equation:
        - // as above
    - There is an equation:
        - // as above

- There is an example:
    - verbal summary: <arg1>.
    - related to: <arg2>.

- There is an explanation:
    - // This statement type should be used for information that is not new but serves to illustrate other information.
    - verbal summary: <arg1>.
    - related to: <arg2>.

- There is special terminology:
    - example: <arg1>.
    - keywords:
        - <arg2>
    - related to: <arg3>.

### References to Complex Formalized Statements

It might be desirable to reference a Complex Formalized Statements in a later statement. This can be done as in the following example:

- There is an equation:
    - // this can only be used inside a setting, premise or assertion
    - full source code: $a^2 + b^2 = c^2$.
    - reference: 'ref_eq1'
- 'ref_eq1' is associated to 'Pythagorean theorem'


## Expressions

As arguments to the above statement types the following is allowed:

- Literals:
    - double-quote delimited strings:
        - example 1: "Hello world"
    - numbers in Python syntax:
        - example: 1
            - explanation: integer number
        - examples: 2.5
            - explanation: real number expressed as floating point number
        - examples: 4 + 3.6j
            - explanation: complex number expressed expressed like in Python
- explicitly defined entities:
    - examples: 'set', 'infinite', 'union'
    - explanation: these entities will be defined below
- applied operators
    - example 1: 'intersection'(\SX, \SY)
    - example 2: 'symmetric difference'(\SX, \SY)
    - explanation: these operators will be defined below. The syntax is: '<operator_name>'(<argument_list>)

----

# Input Part 2: Remarks and Instructions

- If you are content with the given formalization, just return the unchanged new formalized statements.
- If you think there is room for improvement, respond with an improvement. Always state your improvement in the given format as a part of the new formalized statements
- Example of an improved statement (example output):



- There is an Equation:
<<<<<<< current
    - formalized left hand side: 'a'**2 + 'b'
=======
    - formalized left hand side: 'a'**2 + 'b'**2
>>>>>>> new
    - formalized right hand side: 'c'**2

- You are allowed to create new statements.
- If you add additional information or entire blocks of statements, always use the syntax above (<<<<<<< ... ======= ...>>>>>>>)
- If you cannot make an informed decision, reply "cannot make decision".

----

# Input Part 3: The LaTeX source code which was already processed

```
{{context.processed_latex_source}}
```

----

# Input Part 4: The formalized statements which where extracted from that LaTeX source code

{{context.resulting_statements}}

----


# Input Part 5: The new LaTeX source code from which new formalized statements were generated

```
{{context.new_latex_source}}
```

# Input Part 6: The newly generated formalized statements
----

{{context.new_statements}}


# Input Part 7: Final Instructions
- Do not annotate your results in tick marks or anything else.
- It is vital that you use the syntax provided in part 2 (<<<<<<< ... ======= ... >>>>>>>) to represent improvements.
- Be critical about the statements under consideration. Consider the use of operators to model mathematical concepts.
- If you think you need new statements / new classes / relations / concepts to describe the source snippet, please create those new statements.