## TopModifiedFunctions

This action uses [PyDriller](https://pydriller.readthedocs.io/en/latest/) to analyze the commit history of a repository and report the most commonly modified functions. It currently analyzes source files ending in `.py`, `.js`, `.java`, and `.ts` and prints out a report in the following markdown format

```
## Top modified functions in this repo

The repo has 1 commits that modified source code files.
These commits have a total of 1 modified unique functions

Top 10 modified functions:

| Function | # commits | Date Range |
| --- | --: | --: |
| `get_freq_modified_fns.py#main` | 1 | October 18, 2023 - October 18, 2023 |

```

## How to Use this action in Your Workflow

In your `.github/workflows/workflow-name.yaml` file, use the following code:

```
on:
  workflow_dispatch
  
jobs:
  top-modified-fns:
    runs-on: ubuntu-latest
    name: A job to list top modified functions
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: get modified functions
        uses: snadi/TopModifiedFunctions@v1.0
        with:
          topn: 5
```

Note that the first step checks out the target github repo with all of its history (hence `fetch-depth: 0`).
This is necessary for the `TopModifiedFunctions` action to work since it relies on analyzing the history of the current repo.