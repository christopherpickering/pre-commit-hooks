# Pre-commit hooks

## Poetry to Pip requirements

This pre-commit hook can be used to generate a (`requirements`)[https://pip.pypa.io/en/stable/user_guide/#requirements-files] file for pip from Poetry's dependency list.

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
