# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] — 2026-04-17

### Added
- Python AST parser that extracts import aliases and dotted call chains
- Runtime introspection against installed packages via `importlib` + `getattr`
- Fuzzy-matched suggestions for missing attributes via `difflib`
- CLI entry point `ghostcall` with file and stdin input
- `--md` flag to extract Python from fenced markdown code blocks
- `--json` flag for machine-readable output
- Exit codes: `0` clean, `1` hallucinations found, `2` syntax error
- Support for Python 3.9, 3.10, 3.11, 3.12, 3.13
- PyPI Trusted Publisher workflow (OIDC, no long-lived tokens)
- GitHub Actions CI across the full supported Python matrix

[Unreleased]: https://github.com/linosorice/ghostcall/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/linosorice/ghostcall/releases/tag/v0.1.0
