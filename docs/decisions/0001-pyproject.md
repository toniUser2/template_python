# 0001 – pyproject.toml instead of setup.py and requirements.txt

**Status:** accepted

## Context

The template used `setup.py`, `requirements.txt` and `tests/pytest.ini` side by side.
Tests needed a `sys.path` hack to import the code.

## Decision

All configuration lives in `pyproject.toml` (metadata, dependencies, pytest, ruff).
Code uses the `src/<package>/` layout and is installed with `pip install -e ".[dev]"`.

## Consequences

- One place for dependencies and tool configuration.
- Tests import the package directly; no `sys.path` manipulation.
- The environment must be set up via `pip install -e` (done by `scripts/setup_env.py`).
