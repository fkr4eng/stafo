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
Your task is to convert LaTeX source code from a mathematical text book to a sequence of highly formalized statements which can be easily postprocessed. Your input data consists of several parts which are separated by `----`. Each part has a different meaning. In the formalized statements "arg1" and "arg2" are placeholders (i.e. variables) for specific values. In the abstract examples in Input Part 1 the strings "<arg1>" and "<arg2>" serve as such placeholders.

----

# Input Part 1: The following **types** of formalized statements are allowed:

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
- <arg1> hast the alternative label <arg2>.
- There is an equivalence statement
    - full source code: <arg1>
    - source code of assertion: <arg1>
        - // the assertion is the part before "if and only if"
    - source code of premise: <arg2>
        - // the premise is the part after "if and only if"
- <arg1> is associate with <<arg2>>


----

# Input Part 2: Remarks and Instructions

- In your output only generate statements which correspond to one of the statements of the above list (Input Part 1).
- If you think that a piece of information cannot be represented by one of the above statements, just generate a comment with explanations.
- In the LaTeX source code (Input Part 3 and Input Part 5) you can ignore the following:
    - `\label{...}`
    - `\index{...}`
    - % ... (comment until the next newline)
- In the LaTeX source code (Input Part 3 and Input Part 5) some custom macros are used to abbreviate variables (`\SX`, `\SY`) and operators. The macro `\it` means italic and is used to emphasize words.
- The order of the formalized statements in Input Part 4 mainly follows the order in which the information is presented by the LaTeX source code in Input Part 3.


----
"""

prompt_part2 = r"""

# Input Part 3: The LaTeX source code which was already processed

```
\section{Sets}


A {\it set} $\{x,y,\ldots\}$ is a collection of elements.
A set can include either a finite or infinite number of elements.
The set $\SX$ is {\it finite} if it has a finite number of elements; otherwise, $\SX$ is {\it infinite}. The set $\SX$ is {\it countably infinite} if $\SX$ is infinite and its elements are in one-to-one correspondence with the positive integers.  The set $\SX$ is {\it countable} if it is either finite or countably infinite.

Let $\SX$ be a set.
Then, \begin{align}x\in \SX\end{align} means that $x$ is an {\it element}
\label{insym}%
\index{element!definition}%
of $\SX$. If $w$ is not an element of $\SX$, then we write
\begin{align}w\not\in \SX.\end{align}
\label{notinsym}

No set can be an element of itself.  Therefore, there does not exist a set that includes every set.  The set with no elements, denoted by $\varnothing\mspace{-1mu},$ is the {\it empty set}.
%
\label{varnothingsym}%
\index{empty set!definition}%
\index{nonempty set!definition}%
If $\SX\not=\varnothing\mspace{-1mu},$ then $\SX$ is {\it nonempty}.



Let $\SX$ and $\SY$ be sets. The {\it intersection}
\index{intersection!definition}%
of $\SX$ and $\SY$ is the set of common elements of $\SX$ and
$\SY$, which is given by
\begin{align}
\SX\cap \SY
%
\isdef\{x\mspace{-1mu}\colon\ x\in \SX \mbox{ and } x\in \SY \}
%
=  \{ x\in \SX \mspace{-2mu}\colon\ x\in \SY \}
%
=\{x\in \SY\mspace{-2mu}\colon\ x\in \SX \}
%
= \SY \cap \SX,\end{align}
```

----

# Input Part 4: The formalized statements which where extracted from that LaTeX source code

- There is a class: 'set'.

- There is a property: 'finite'.
- There is a property: 'infinite'.
- There is a property: 'countably infinite'.
- There is a property: 'countable'.
- There is a property: 'empty'.
- There is a property: 'nonempty'.

- 'finite' is applicable to 'set'.
- 'infinite' is applicable to 'set'.
- 'countably infinite' is applicable to 'set'.
- 'countable' is applicable to 'set'.
- 'empty' is applicable to 'set'.
- 'nonempty' is applicable to 'set'.

- 'countably infinite' is a subproperty of 'infinite'.
- 'positive integers' is an instance of 'set'.
- 'empty set' is an instance of 'set'.
- 'empty set' has the associated LaTeX notation `$\varnothing$`.
- 'empty set' has the verbal description "The set with no elements".

- There is a class: 'element'.
- There is a relation: 'is element of'.
- 'is element of' has the associated LaTeX notation `$arg1 \in arg2$`.
- There is a relation: 'is not element of'.
- 'is not element of' has the associated LaTeX notation `$arg1 \not\in arg2$`.
- There is a relation: 'is in one-to-one correspondence with'.

- There is a binary operator: 'intersection'.
- The type of argument1 of 'intersection' is 'set'.
- The type of argument2 of 'intersection' is 'set'.
- The result type of 'intersection' is 'set'.
- 'intersection' has the associated LaTeX notation `$arg1 \cap arg2$`
- 'intersection' has defining formula `$\SX\cap \SY \isdef\{x\mspace{-1mu}\colon\ x\in \SX \mbox{ and } x\in \SY \}$`.
- 'intersection' has the verbal description "The intersection of arg1 and arg2 is the set of common elements of arg1 and arg2".

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