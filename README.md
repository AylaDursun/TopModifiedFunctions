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

## Usage Overview

```
- uses: snadi/TopModifiedFunctions@v1.1
  with:
    # top n functions to display (default 10)
    topn:

    # The name of the branch to analyze (default `main`)
    mainbranch: ''
```

## Workflow File Example

In your `.github/workflows/workflow-name.yaml` file, use the following code:

```
name: List top modified functions

on:
  workflow_dispatch
  
jobs:
  top-modified-fns:
    runs-on: ubuntu-latest
    name: List top modified functions
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: get modified functions
        uses: snadi/TopModifiedFunctions@v1.1
        with:
          topn: 5
```

Note that the first step checks out the target github repo with all of its history (hence `fetch-depth: 0`).
This is necessary for the `TopModifiedFunctions` action to work since it relies on analyzing the history of the current repo.

Also, note that by default, this action assumes that the name of the branch to be analyzed is `main`. You can change that name
through the `mainbranch` option. You can also change your workflow to be configurable so you can analyze different branches and/or display different number of top n functions without changing your workflow file:

```
name: List top modified functions

on:
  workflow_dispatch:
    inputs:
      topn:
        description: "The number of top frequently modified functions to return"
        type: number
        default: "5"
      mainbranch:
        description: "The name of the branch to analyze"
        type: string
        default: "master"
  
jobs:
  top-modified-fns:
    runs-on: ubuntu-latest
    name: A job to list top modified functions
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: get modified functions
        uses: snadi/TopModifiedFunctions@v1.1
        with:
          topn: "${{ github.event.inputs.topn }}"
          mainbranch: "${{ github.event.inputs.mainbranch }}"
```
