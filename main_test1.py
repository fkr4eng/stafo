import tomllib

#! pip install google-generativeai
import google.generativeai as genai

from ipydex import IPS


# config file starts with .git_config # to prevent synchronizing it to (unencrypted) cloud
with open(".git_config.toml", "rb") as fp:
    config_dict = tomllib.load(fp)


# https://github.com/google-gemini/generative-ai-python


genai.configure(api_key=config_dict["gemeni_api_key"])

model = genai.GenerativeModel('gemini-1.5-pro-latest')

# - It would be useful if you also would generate comments to explain your "chain of thought".

prompt_part1 = r"""
Your task is to convert LaTeX source code from a mathematical text book to a sequence of highly formalized statements which can be easily post-processed. Your input data consists of several parts which are separated by `----`. Each part has a different meaning. In the formalized statements "arg1" and "arg2" are placeholders (i.e. variables) for specific values. In the abstract examples in Input Part 1 the strings "<arg1>" and "<arg2>" serve as such placeholders.

----

# Input Part 1: Description of allowed formalized statements

All statements are represented as a bullet list in markdown syntax. There are two general types of formalized statements: Simple Formalized Statements and Complex Formalized Statements.

## Simple Formalized Statements

Simple Formalized Statements consist of one line. They are not followed by a line with a higher indentation level. The following Simple Formalized Statements are allowed:

- // This is a comment to explain modeling decisions. It is an arbitrary single line string.
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
- <arg1> has the alternative label <arg2>.
- <arg1> is associate with <arg2>.
- <arg1> has the property <arg2>.


## Complex Formalized Statements

Complex Formalized Statements consists of multiple lines which correspond to one list item of the current level followed at least one sub-list. The sub-list can consist of Simple Formalized Statements or Complex Formalized Statements. Thus, a Complex Formalized Statement contains lines with at least two indentation levels. The following Complex Formalized Statements are allowed:

- There is an equivalence statement:
    - full source code: <arg1>.
    - // the assertion is the part before "if and only if"
    - source code of assertion: <arg1>.
    - // the premise is the part after "if and only if"
    - source code of premise: <arg2>.

- // The following starts a definition statement which can contain either one OR or one AND block. Such blocks can be nested which is represented by their indentation level
- <arg1> has the definition:
    - // the following starts an OR-block, i.e. a block of an arbitrary number of conditions which are linked by logical OR
    - OR
        - <condition1>
        - <condition2>
    - // the following starts an AND-block, i.e. a block of an arbitrary number of conditions which are linked by logical AND
    - AND
        - <condition1>
        - <condition2>

----

# Input Part 2: Remarks and Instructions

- In your output only generate statements which correspond to one of the statements of the above list (Input Part 1).
- If you think that a piece of information cannot be represented by one of the above statements, just generate a comment with explanations.
- In the LaTeX source code (Input Part 3 and Input Part 5) you can ignore the following:
    - `\label{...}`
    - `\index{...}`
- The LaTeX source code (Input Part 3 and Input Part 5) contains special snippet-delimiter comments like `% snippet(5)`
- In the list of resulting formalized statements we use a comment like `- // snippet(5)` to indicate the following statements are from `snippet(5)` of the LaTeX source code. Thereby `snippet(5)` is that substring of the LaTeX source code which starts with the special comment `% snippet(5)` and ends just before the next such comment `% snippet(6)`. The numbers 5 and 6 are only examples here.
- In the LaTeX source code (Input Part 3 and Input Part 5) you can ignore all other comments (i.e. substrings that start with `%` and span until the next newline)
- In the LaTeX source code (Input Part 3 and Input Part 5) some custom macros are used to abbreviate variables (`\SX`, `\SY`) and operators. The macro `\it` means italic and is used to emphasize words.
- The order of the formalized statements in Input Part 4 mainly follows the order in which the information is presented by the LaTeX source code in Input Part 3.


----
"""

prompt_part2 = """

# Input Part 3: The LaTeX source code which was already processed

```
{}
```

----

# Input Part 4: The formalized statements which where extracted from that LaTeX source code

{}
----

"""

prompt_part3 = r"""

# Input Part 5: The new LaTeX source code from which you should generate new formalized statements

```
The {\it union} of $\SX $ and $\SY$ is the set of
elements in either $\SX $ or $\SY$, which is the set
\index{union!definition}%
%
\begin{align}\SX \cup \SY \isdef\{x\mspace{-1mu}\colon\ x\in \SX \mbox{ or } x\in \SY \}=\SY \cup
\SX.\end{align}
```

----


# Input Part 6: Final Instructions

Please generate a list of formalized statements (like in Input Part 4) which represent the information from Input Part 5. Thereby, adhere to the statement types given in Input Part 1 and the given instructions.

"""


message = "\n".join([prompt_part1, prompt_part2, prompt_part3])

print(model.count_tokens(message))
config = genai.GenerationConfig(temperature=0)

if 0:
    res = model.generate_content(message, generation_config=config)
    print(res.text)



IPS()