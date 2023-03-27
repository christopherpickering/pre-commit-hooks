# Pre-commit hooks

[![codecov](https://codecov.io/gh/christopherpickering/pre-commit-hooks/branch/master/graph/badge.svg?token=TY1AWZZ2JB)](https://codecov.io/gh/christopherpickering/pre-commit-hooks)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/christopherpickering/pre-commit-hooks/master.svg)](https://results.pre-commit.ci/latest/github/christopherpickering/pre-commit-hooks/master)
[![test](https://github.com/christopherpickering/pre-commit-hooks/actions/workflows/test.yaml/badge.svg)](https://github.com/christopherpickering/pre-commit-hooks/actions/workflows/test.yaml)
![PyPI - Downloads](https://img.shields.io/pypi/dm/poetry-to-requirements)
![PyPI](https://img.shields.io/pypi/v/poetry-to-requirements)

## Poetry to Pip requirements

This pre-commit hook can be used to generate a [requirements](https://pip.pypa.io/en/stable/user_guide/#requirements-files) file for pip from Poetry's dependency list.

### General Usage

In each of your repos, add a file called .pre-commit-config.yaml with the following contents:

```yaml
repos:
  - repo: https://github.com/christopherpickering/pre-commit-hooks
    rev: <VERSION> # Get the latest from: https://github.com/christopherpickering/pre-commit-hooks/releases
    hooks:
      - id: poetry-to-requirements
        args: [--dev,--output=subfolder/requirements.txt]

```

### Arguments

 -  --dev: include dev requirements. Default= False
 -  --output=folder/requirements.txt: output file name. Default= requirements.txt. This path should be relative to the --input path.
 -  (optional) --input=path/to/project_root: path to the project root. Default= .
