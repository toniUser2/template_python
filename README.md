# template_python

Short description of what this project does.

## Setup

```powershell
python scripts/setup_env.py      # creates .venv and installs the project + dev tools
.\.venv\Scripts\Activate.ps1     # Linux/macOS: source .venv/bin/activate
```

Manual alternative:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
```

## Usage

```powershell
template-python                  # entry point defined in pyproject.toml
python -m template_python.main   # alternative
```

## Development

```powershell
python scripts/check.py   # run ALL checks (same as CI): lint, format, types, tests, build

pytest                 # run tests
ruff check .           # lint
ruff check . --fix     # lint + auto-fix
ruff format .          # format code
pyright                # type check (strict, same rules as Pylance)
python -m build        # build wheel + sdist into dist/
```

CI runs the same checks on every push via GitHub Actions
([.github/workflows/ci.yml](.github/workflows/ci.yml)).

Dependencies are managed in [pyproject.toml](pyproject.toml):

- runtime → `[project] dependencies`
- dev tools → `[project.optional-dependencies] dev`

After changing them, run `pip install -e ".[dev]"` again.

## Project structure

```
├── docs/                  # concept, decisions, diagrams → see docs/README.md
├── .github/workflows/     # CI pipeline
├── scripts/setup_env.py   # environment setup
├── scripts/check.py       # run all checks locally
├── src/template_python/   # source code (the package)
├── tests/                 # pytest tests
└── pyproject.toml         # metadata, dependencies, pytest + ruff config
```

## Using this template for a new project

1. Copy the folder (without `.venv/` and `.git/`) and run `git init`.
2. Rename `src/template_python/` to your package name.
3. Replace `template_python` / `template-python` in `pyproject.toml`, `tests/` and this README.
4. Run `python scripts/setup_env.py`.

## Libraries

| Library | Docs |
| ------- | ---- |
| pytest  | <https://docs.pytest.org> |
| ruff    | <https://docs.astral.sh/ruff> |
