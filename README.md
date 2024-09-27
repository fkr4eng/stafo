# Stafo – Statement Formalizer


<https://gitlab.hrz.tu-chemnitz.de/knoll--tu-dresden.de/stafo>

## Installation

`pip install -e .`


## Usage

- Overview:
    - `stafo --help`

- Process one snippet of the source file
    - `stafo -i data/chunk_full_source.tex data/formalized_statements0.md snapshots/math`
    - `stafo -i data\V0\V0_all.tex data\V0\formalized_statements_v0.md snapshots/V0`
    - after running this command the user is expected to review the changes to the statement-file

- Convert formalized snippets to pyirk (still experimental):
    - `stafo -c tmp.md`


## PDF creation (math document)

For manual reviewing the created snippets it is recommended to read the pdf file containing the snippet numbers. This file can be created by `pdflatex data/pdf-generation/main.tex`.


## Next Development Steps:

- deal with (many, consecutive) ignored snippets: do not waste LLM-calls on them
