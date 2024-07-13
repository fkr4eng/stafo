# Stafo – Statement Formalizer


<https://gitlab.hrz.tu-chemnitz.de/knoll--tu-dresden.de/stafo>

## Installation

`pip install -e .`


## Usage

- Overview:
    - `stafo --help`

- Process one snippet of the source file
    - `stafo -i data/chunk_full_source.tex data/formalized_statements0.md`
    - after running this command the user is expected to review the changes to the statement-file

- Convert formalized snippets to pyirk (still experimental):
    - `stafo -c tmp.md`


## Next Development Steps:

- deal with (many, consecutive) ignored snippets: do not waste LLM-calls on them
