# Migration Guide: Restructuring to Standard Python Project Layout

## Overview

This guide documents the migration from a flat project structure to the recommended Python project structure following best practices.

## What Changed

### Old Structure

```txt
simplecalc/
├── calculator.py
├── test_calculator.py
├── .coveragerc
├── README.md
└── LICENSE
```

### New Structure

```txt
simplecalc/
├── src/
│   └── simplecalc/
│       ├── __init__.py
│       └── calculator.py
├── tests/
│   ├── __init__.py
│   └── test_calculator.py
├── .coveragerc
├── .flake8
├── .pre-commit-config.yaml
├── pyproject.toml
├── requirements-dev.txt
├── MANIFEST.in
├── README.md
└── LICENSE
```

## Key Changes

### 1. Source Code Organization

**Before:**

- Source code at root level
- No package structure

**After:**

- Source code in `src/simplecalc/` package
- Proper `__init__.py` with package exports
- Better namespace isolation

### 2. Test Organization

**Before:**

- Tests at root level
- Import directly from `calculator`

**After:**

- Tests in dedicated `tests/` directory
- Import from installed package: `from simplecalc.calculator import ...`
- Tests run against installed package

### 3. Package Configuration

**Before:**

- No formal package configuration
- No dependency management

**After:**

- `pyproject.toml` with full configuration
- Development dependencies in `requirements-dev.txt`
- Setuptools configuration for package building

### 4. Development Tools

**New additions:**

- `.flake8`: Linting configuration
- `.pre-commit-config.yaml`: Pre-commit hooks
- Updated `.coveragerc`: Coverage for src layout
- Updated VS Code settings and tasks

## Installation Instructions

### For Development

```bash
# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Install in editable mode with dev dependencies
pip install -e ".[dev]"

# Or install just dev dependencies
pip install -r requirements-dev.txt
pip install -e .
```

### For End Users

```bash
pip install .
```

## Running the Application

### Old Method (deprecated)

```bash
python calculator.py
```

### New Methods

**As a command-line tool:**

```bash
simplecalc
```

**As a Python module:**

```bash
python -m simplecalc.calculator
```

## Running Tests

### Old Method

```bash
python -m unittest test_calculator.py
```

### New Methods

**Using unittest:**

```bash
python -m unittest discover -s tests
```

**Using pytest:**

```bash
pytest tests/
```

**With coverage:**

```bash
coverage run -m unittest discover -s tests
coverage report
```

**Using VS Code:**

- Tests will automatically discover from `tests/` directory
- Use the Testing sidebar to run/debug tests

## Import Changes

### Old Imports (in tests)

```python
from calculator import add, subtract, multiply, divide
```

### New Imports

```python
from simplecalc.calculator import add, subtract, multiply, divide
# Or
from simplecalc import add, subtract, multiply, divide
```

## Configuration Updates

### .coveragerc

```ini
[run]
source = src  # Changed from "."
omit = 
    */tests/*
```

### .vscode/settings.json

```json
{
    "python.testing.unittestArgs": ["-v", "-s", "tests", "-p", "test_*.py"],
    "python.analysis.extraPaths": ["${workspaceFolder}/src"]
}
```

## Benefits of New Structure

### 1. **Better Separation**

- Clear distinction between source code, tests, and configuration
- Prevents accidental imports from test modules

### 2. **Standard Layout**

- Follows Python packaging best practices
- Compatible with modern Python packaging tools (pip, setuptools, build)
- Easier for contributors to understand

### 3. **Improved Testing**

- Tests run against installed package, not local files
- Catches import issues early
- Better isolation between test and source code

### 4. **Professional Setup**

- Ready for PyPI distribution
- Proper dependency management
- Development tool integration

### 5. **VS Code Integration**

- Better IntelliSense and code navigation
- Proper test discovery
- Linting and formatting tools integrated

## Development Workflow

### Setup New Environment

```bash
# Clone repository
git clone <repo-url>
cd simplecalc

# Setup virtual environment
python -m venv .venv
.venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Install pre-commit hooks (optional)
pre-commit install
```

### Daily Development

```bash
# Run tests
pytest tests/ -v

# Run with coverage
coverage run -m pytest tests/
coverage report
coverage html  # Generate HTML report

# Format code
black src/ tests/

# Lint code
flake8 src/ tests/

# Type check
mypy src/
```

### Before Commit

```bash
# Run all checks (if using pre-commit)
pre-commit run --all-files

# Or manually
black src/ tests/
flake8 src/ tests/
mypy src/
pytest tests/
```

## Troubleshooting

### Import Errors

**Problem:** `ModuleNotFoundError: No module named 'simplecalc'`

**Solution:**

```bash
# Reinstall in editable mode
pip install -e .
```

### Tests Not Found

**Problem:** VS Code doesn't discover tests

**Solution:**

1. Check `.vscode/settings.json` has correct test path
2. Reload VS Code window
3. Check Python interpreter is from the virtual environment

### Coverage Not Working

**Problem:** Coverage shows 0% or wrong files

**Solution:**

1. Check `.coveragerc` has `source = src`
2. Run with discovery: `coverage run -m unittest discover -s tests`
3. Make sure package is installed: `pip install -e .`

## Migration Checklist

- [x] Create `src/simplecalc/` directory
- [x] Move `calculator.py` to `src/simplecalc/`
- [x] Create `src/simplecalc/__init__.py`
- [x] Create `tests/` directory
- [x] Move `test_calculator.py` to `tests/`
- [x] Update imports in test files
- [x] Create `pyproject.toml`
- [x] Create `requirements-dev.txt`
- [x] Create `.flake8` configuration
- [x] Create `.pre-commit-config.yaml`
- [x] Update `.coveragerc`
- [x] Update `.vscode/settings.json`
- [x] Update `.vscode/tasks.json`
- [x] Update `README.md`
- [x] Install package in editable mode
- [x] Run tests to verify
- [x] Update documentation

## Backward Compatibility

### Old Files

The old `calculator.py` and `test_calculator.py` at root level can be:

- Kept temporarily with deprecation warnings
- Removed once confirmed working
- Updated to import and delegate to new location

### Maintaining Old Structure (Not Recommended)

If you must keep the old structure temporarily:

```python
# calculator.py (at root) - Deprecated wrapper
from simplecalc.calculator import *

if __name__ == '__main__':
    from simplecalc.calculator import main
    main()
```

## References

- [Python Packaging Guide](https://packaging.python.org/)
- [setuptools Documentation](https://setuptools.pypa.io/)
- [pytest Documentation](https://docs.pytest.org/)
- [PEP 517/518: pyproject.toml](https://www.python.org/dev/peps/pep-0517/)

## Questions?

For questions about this migration, see:

- Project README.md
- `.github/instructions/python.instructions.md`
- `.github/instructions/evergreen-development.instructions.md`
