# Python Project Structure - Quick Reference

## Standard Python Project Layout (src-layout)

This project now follows the recommended **src-layout** pattern for Python projects.

## Directory Structure

```txt
simplecalc/
├── src/                          # Source code directory
│   └── simplecalc/              # Package directory
│       ├── __init__.py          # Package initialization & exports
│       └── calculator.py        # Main module
├── tests/                        # Test directory
│   ├── __init__.py              # Test package initialization
│   └── test_calculator.py       # Unit tests
├── .github/                      # GitHub workflows & documentation
├── .vscode/                      # VS Code configuration
│   ├── settings.json            # Python & test settings
│   └── tasks.json               # Build & test tasks
├── pyproject.toml               # Project metadata & configuration
├── requirements-dev.txt         # Development dependencies
├── .coveragerc                  # Coverage.py configuration
├── .flake8                      # Flake8 linter configuration
├── .pre-commit-config.yaml      # Pre-commit hooks
├── .gitignore                   # Git ignore rules
├── MANIFEST.in                  # Package manifest
├── MIGRATION_GUIDE.md           # Detailed migration documentation
├── README.md                    # Project documentation
└── LICENSE                      # License file
```

## Quick Commands

### Installation

```bash
# Development mode (editable install)
pip install -e ".[dev]"

# Production install
pip install .
```

### Running the Application

```bash
# Command-line tool (after install)
simplecalc

# As Python module
python -m simplecalc.calculator
```

### Testing

```bash
# Run all tests
python -m unittest discover -s tests

# With coverage
coverage run -m unittest discover -s tests
coverage report

# Using pytest
pytest tests/ -v
```

### Code Quality

```bash
# Format code
black src/ tests/

# Lint code
flake8 src/ tests/

# Type check
mypy src/

# All pre-commit checks
pre-commit run --all-files
```

## Why src-layout?

### Benefits

1. **Import Protection**: Prevents accidental imports from the local directory
2. **Test Isolation**: Tests run against the installed package, not local files
3. **Distribution Ready**: Package is ready for PyPI distribution
4. **Standard Practice**: Follows Python packaging best practices
5. **Tool Support**: Better support from modern Python tools

### Key Principle

Tests import from the **installed package**, not from local files:

```python
# Correct
from simplecalc.calculator import add

# Not from local relative imports
```

## Configuration Files

### pyproject.toml

Modern Python project configuration:

- Package metadata
- Build system configuration
- Tool configurations (black, pytest, mypy, coverage)
- Dependencies and optional dependencies

### requirements-dev.txt

Development dependencies:

- Testing tools (pytest, coverage)
- Code quality tools (black, flake8, mypy)
- Pre-commit hooks

### .coveragerc

Coverage configuration:

- Source directory: `src`
- Omit patterns for tests
- Report settings

### .flake8

Linting configuration:

- Line length: 88 (black compatible)
- Exclusions for auto-generated files
- Per-file ignores

### .pre-commit-config.yaml

Automated checks before commit:

- Trailing whitespace removal
- End-of-file fixer
- Code formatting (black)
- Linting (flake8)
- Type checking (mypy)

## Package Structure

`src/simplecalc/__init__.py`

```python
"""Package initialization with exports."""
__version__ = "1.0.0"

from .calculator import add, subtract, multiply, divide, calculate

__all__ = ["add", "subtract", "multiply", "divide", "calculate"]
```

### Usage in Code

```python
# Import entire package
import simplecalc

# Use functions
result = simplecalc.add(1, 2)

# Or import specific functions
from simplecalc import add, subtract

result = add(1, 2)
```

## VS Code Integration

### Testing

- Tests auto-discovered from `tests/` directory
- Run/debug individual tests from the Testing sidebar
- Test explorer shows all test cases

### Python Path

```json
{
    "python.analysis.extraPaths": ["${workspaceFolder}/src"]
}
```

This ensures IntelliSense works correctly with the src-layout.

## Common Tasks

### Add a New Module

1. Create file in `src/simplecalc/new_module.py`
2. Add exports to `src/simplecalc/__init__.py` if needed
3. Create tests in `tests/test_new_module.py`
4. Run tests to verify

### Update Dependencies

```bash
# Add to pyproject.toml under [project.dependencies]
# Then reinstall
pip install -e ".[dev]"
```

### Create Distribution Package

```bash
# Build wheel and source distribution
python -m build

# Install from built package
pip install dist/simplecalc-1.0.0-py3-none-any.whl
```

## Troubleshooting

### Import Errors

**Issue**: `ModuleNotFoundError: No module named 'simplecalc'`

**Fix**:

```bash
pip install -e .
```

### Tests Not Running

**Issue**: VS Code doesn't find tests

**Fix**:

1. Check Python interpreter is from `.venv`
2. Check `.vscode/settings.json` has correct test path
3. Reload VS Code window

### Coverage Showing Wrong Files

**Issue**: Coverage reports wrong source files

**Fix**:

1. Ensure `.coveragerc` has `source = src`
2. Reinstall package: `pip install -e .`
3. Run with explicit discovery: `coverage run -m unittest discover -s tests`

## References

- [Python Packaging User Guide](https://packaging.python.org/)
- [setuptools Documentation](https://setuptools.pypa.io/)
- [PEP 517 - Pyproject.toml](https://www.python.org/dev/peps/pep-0517/)
- [pytest Documentation](https://docs.pytest.org/)
- [Project Migration Guide](MIGRATION_GUIDE.md)

## Best Practices

1. ✅ Always use `pip install -e .` for development
2. ✅ Run tests frequently during development
3. ✅ Use pre-commit hooks to maintain code quality
4. ✅ Keep `pyproject.toml` up to date with dependencies
5. ✅ Write tests in `tests/` directory, not in `src/`
6. ✅ Import from package name, not relative imports in tests
7. ✅ Use `python -m` to run modules (e.g., `python -m pytest`)

## Getting Help

For detailed information:

- See [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md) for migration details
- See [README.md](README.md) for project overview
- See `.github/instructions/` for development guidelines
