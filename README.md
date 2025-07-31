# Stafo – Statement Formalizer


<https://gitlab.hrz.tu-chemnitz.de/knoll--tu-dresden.de/stafo>

## Installation

`pip install -e .`



### Configuration

Copy `./_example_config.toml` to `./.git_config.toml` and adapt the content.


## Usage

- Overview:
    - `stafo --help`

- Process one snippet of the source file
    - `stafo -i data/chunk_full_source.tex data/formalized_statements0.md snapshots/math`
    - `stafo -i data\V0\V0_all.tex data\V0\formalized_statements_v0.md snapshots/V0`
    - `stafo -i data\nichtlinear\processed\kapitel2.tex data\nichtlinear\processed\formalized_statements_nl.md snapshots\nl`
    - after running this command the user is expected to review the changes to the statement-file

- Convert formalized snippets to pyirk (still experimental):
    - `stafo -c tmp.md`

- Auto snippet numbering
    - `stafo -asn data\nichtlinear\processed\kapitel2.tex`

## PDF creation (math document)

For manual reviewing the created snippets it is recommended to read the pdf file containing the snippet numbers. This file can be created by `pdflatex data/pdf-generation/main.tex`.


## Next Development Steps:

- deal with (many, consecutive) ignored snippets: do not waste LLM-calls on them



## Qualifiers:
### in FNL
- see example [here](./tests/testdata/statements06_qualifier.md)
- if multiple qualifiers apply together (e.g. from + to see below), they are separated by comma behind qqq
- if qualfifiers apply independant (see below), they are separated by qqq
### target format
````
d = {
    "items": {
        "bob": {
            "R1": "bob",
            "R4": {
                "object": I7435["human"],
                "q": []
            }
            "R1111": [
                {
                    "object": "Dresden",
                    "q": [
                        {
                            R1111: 2000,
                            R2222: 2002 # these two qualifiers apply together (to form a range)
                        },
                        {
                            R1111: 2002,
                            R2222: 2004
                        }, # these two qualifier dicts are independant of eachother
                    ]
                },
                {
                    "object": "Wien",
                    "q": [
                        {
                            R1111: 2005,
                            R2222: 2007
                        },
                        {
                            R1111: 2008,
                            R2222: 2010
                        },
                    ]
                }
            ]
        }
    }
}

R1111["lives_in"]
R2222["from"]
R3333["to"]
````