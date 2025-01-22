
Your task is to convert LaTeX source code from a mathematical text book to a sequence of highly formalized statements which can be easily post-processed. The original text is in german. Your input data consists of several parts which are separated by `----`. Each part has a different meaning. In the formalized statements "arg1" and "arg2" are placeholders (i.e. variables) for specific values. In the abstract examples in Input Part 1 the strings "<arg1>", "<arg2>" etc. serve as such placeholders. The placeholders "<arg1>", "<arg2>", <condition> should be in german, the rest of your answer should be in english.

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
- <arg1> has an alternative label <arg2>.
- <arg1> has the property <arg2>.
- <arg1> is associated to <arg2>.
- <arg1> has an alternative german label <arg2>.

Behind the definition of new objects, such as class, property, relation, unary operator, binary operator, you specify the language the name is in by adding @en for english and @de for german.

## Complex Formalized Statements

Complex Formalized Statements consists of multiple lines which correspond to one list item of the current level followed at least one sub-list. The sub-list can consist of Simple Formalized Statements or Complex Formalized Statements. Thus, a Complex Formalized Statement contains lines with at least two indentation levels.

It might be possible that there is not enough infomation to completely generate all aspects of a Complex Fomalized Statement. Please do as best as you can and explain doubts and problems via comments.

The following Complex Formalized Statements are allowed:

- // The following starts a definition statement which can contain either one OR or one AND block. Such blocks can be nested which is represented by their indentation level. Each condition may be preceded by NOT to indicate the negation of the following condition.
- <arg1> has the definition:
    - // the following starts an OR-block, i.e. a block of an arbitrary number of conditions which are linked by logical OR
    - OR
        - <condition1>
        - <condition2>
    - // the following starts an AND-block, i.e. a block of an arbitrary number of conditions which are linked by logical AND
    - AND
        - <condition1>
        - <condition2>

- // This Complex Formalized Statement serves to model parts of the text which update (e.g. generalize) earlier statements
- Amend definition of <arg1>:
    - replace <arg1> by <arg2>

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

- In your output only generate statements which correspond to one of the statement types of the above list (Input Part 1).
- Please generate your output as markdown list. No heading, no delimiter.
- If you think that a piece of information cannot be represented by one of the above statements, just generate a comment with explanations.
- If you think that basic mathematical concepts like 'set' or 'integer numbers' are implied from the context but not explicitely named, try to generate statements as described in Input Part 1 but add a comment saying 'infered knowlege'.
- If you think you need to introduce a new relation that is not explicitely described, please do so.
- In the LaTeX source code (Input Part 3 and Input Part 5) you can ignore the following:
    - `\label{...}`
    - `\index{...}`
- The LaTeX source code (Input Part 3 and Input Part 5) contains special snippet-delimiter macros like `\snippet{5}`
- In the list of resulting formalized statements we use a comment like `- // snippet(5)` to indicate the following statements are from `snippet 5` of the LaTeX source code. Thereby `snippet 5` is that substring of the LaTeX source code which starts with special macro `\snippet{5}` and ends just before the next such macro `\snippet{6}`. The numbers 5 and 6 are only examples here.
- The argument of some of these macros ends with 'i', for example: `\snippet{2i}`. This indicates that this snippet should be ignored.
- In the LaTeX source code (Input Part 3 and Input Part 5) you can ignore all LaTeX comments (i.e. substrings that start with `%` and span until the next newline)
- In the LaTeX source code (Input Part 3 and Input Part 5) some custom macros are used to abbreviate variables (`\SX`, `\SY`) and operators. The macro `\it` means italic and is used to emphasize words.
- The order of the formalized statements in Input Part 4 mainly follows the order in which the information is presented by the LaTeX source code in Input Part 3.

----

# Input Part 3: The LaTeX source code which was already processed

```
{{context.processed_latex_source}}
```

----

# Input Part 4: The formalized statements which where extracted from that LaTeX source code

{{context.resulting_statements}}

{% if context.continue_mode %}
## Instructive Remark
Note that the last of theses formalized statement-snippets is incomplete. You are expected to continue the this snippet based on the LaTeX source in Input Part 5
{% endif %}
----


# Input Part 5: The new LaTeX source code from which you should generate new formalized statements

```
{{context.new_latex_source}}
```

{% if context.continue_mode %}
## Instructive Remark
Note that part of this LaTeX snippet already has been formalized. You are expected to continue the last snippet of Input Part 4
{% endif %}

----


# Input Part 6: LaTeX source code which follows the previous snippet

You are not supposed to convert this LaTeX code to formalized statements. However, it might give you some additional context which helps to formalize the source code from Input Part 5.

```
{{context.look_ahead_latex_source}}
```



# Input Part 7: Final Instructions

Please generate a list of formalized statements (like in Input Part 4) which represent the information from Input Part 5. Thereby, adhere to the statement types given in Input Part 1 and the given instructions.
"""
