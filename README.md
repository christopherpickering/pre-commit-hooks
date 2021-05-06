# Pre-commit hook Poetry to Pip requirements

This pre-commit hook can be used to generate a `requirements` file for pip from Poetry's dependency list.

## General Usage

In each of your repos, add a file called .pre-commit-config.yaml with the following contents:

```yaml
repos:
  - repo: https://github.com/christopherpickering/pre-commit-poetry-to-requirements
    rev: <VERSION> # Get the latest from: https://github.com/christopherpickering/pre-commit-poetry-to-requirements/releases
    hooks:
      - id: poetry-to-requirements
        language: system
        always_run: true
        args: [--dev,--output=subfolder/requirements.txt]

```

## Arguments

 -  --dev: include dev requirements. Default= False
 -  --output=folder/requirements.txt: output file name. Default= requirements.txt
 