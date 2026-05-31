# Contributing to Sophon
We follow GitFlow with automated verification. All PRs must satisfy: 1) 100% test coverage 2) Valid JSON-RPC API format 3) Backward-compatible changes

## Build Requirements
- Python 3.11+
- Docker 24.0+
- nproc >= 8

## Testing
Run full suite with:

mamba create -n sophon python=3.11
poetry install --with test
pytest --cov=sophon


## Code Style
- Type hints required
- Linter: flake8 + mypy (strict)
- Docstring: Google Python format

## Security Policy
All crypto ops must use PyNaCl. No raw HTTP APIs. Mandatory TPS throttling.