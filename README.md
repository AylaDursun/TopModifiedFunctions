## TopModifiedFunctions

This action uses [PyDriller](https://pydriller.readthedocs.io/en/latest/) to analyze the commit history of a repository and report the most commonly modified functions. It currently analyzes source files ending in `.py`, `.js`, `.java`, and `.ts` and prints out a report in the following markdown format

```
## Top modified functions in this repo

The repo has 1 commits and a total of 1 modified functions

Top 10 modified functions:

| Function | # commits | Date Range |
| --- | --: | --: |
| `get_freq_modified_fns.py#main` | 1 | October 18, 2023 - October 18, 2023 |

```