[![build status](https://github.com/lordwelch/flake8-no-nested-comprehensions/actions/workflows/build.yaml/badge.svg)](https://github.com/lordwelch/flake8-no-nested-comprehensions/actions/workflows/build.yaml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/lordwelch/flake8-no-nested-comprehensions/main.svg)](https://results.pre-commit.ci/latest/github/lordwelch/flake8-no-nested-comprehensions/main)

flake8-no-nested-comprehensions
================

flake8 plugin which forbids nested comprehensions

## installation

```bash
pip install flake8-no-nested-comprehensions
```

## flake8 codes

| Code   | Description                      |
|--------|----------------------------------|
| CMP100 | do not use nested comprehensions |

## rationale

I don't like them.
If you need them for performance you can put a `# noqa: CMP100` and preferrably put a comment in explaining it.

## as a pre-commit hook

See [pre-commit](https://github.com/pre-commit/pre-commit) for instructions

Sample `.pre-commit-config.yaml`:

```yaml
-   repo: https://github.com/pycqa/flake8
    rev: 3.8.1
    hooks:
    -   id: flake8
        additional_dependencies: [flake8-no-nested-comprehensions==1.0.0]
```
