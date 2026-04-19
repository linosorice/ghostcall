# Contributing

Thanks for considering a contribution. ghostcall is a small, focused CLI — issues and PRs are welcome, and so are clear no-votes on features that would expand scope.

## Bug reports

Open a [bug report](https://github.com/linosorice/ghostcall/issues/new?template=bug_report.yml). Include the input that triggered the issue, the ghostcall output, and the Python version.

## Feature ideas

Open a [feature request](https://github.com/linosorice/ghostcall/issues/new?template=feature_request.yml) or start a thread in Discussions. Before proposing a feature, check the [Limitations section of the README](./README.md#limitations) — some scope choices are deliberate.

## Running the test suite

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
ruff check src tests
```

All PRs must pass `pytest` and `ruff check` on Python 3.9–3.13 (GitHub Actions enforces this).

## Scope

ghostcall does one thing: detect missing attributes in LLM-generated Python code against your installed packages. PRs that multiply that scope (other languages, type checking, auto-fix, network calls, config files) will be politely declined with an explanation.
