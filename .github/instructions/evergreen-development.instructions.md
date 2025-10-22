---
description: "Guidelines for maintaining evergreen, sustainable, and future-proof software through continuous modernization, code quality, and best practices."
applyTo: "**/*"
---

# Evergreen Software Development Instructions

## Overview

Evergreen software development is a philosophy and set of practices designed to keep codebases current, maintainable, and future-proof. This document provides guidelines for creating and maintaining code that remains relevant, secure, and performant as technologies and requirements evolve.

## Table of Contents

- [Overview](#overview)
- [Core Principles](#core-principles)
- [Code Quality](#code-quality)
- [Documentation](#documentation)
- [Testing](#testing)
- [Dependencies Management](#dependencies-management)
- [Modernization](#modernization)
- [Performance](#performance)
- [Security](#security)
- [Continuous Integration](#continuous-integration)
- [Best Practices Checklist](#best-practices-checklist)

## Core Principles

### 1. **Future-First Mindset**

Write code with the understanding that it will need to be maintained and updated by others (or yourself) in the future.

- Assume the reader has limited context
- Use clear, self-documenting code
- Anticipate potential future changes
- Design for extensibility, not just current requirements

### 2. **Continuous Improvement**

Regularly review and update code to incorporate new best practices and language features.

- Schedule regular code review sessions
- Keep dependencies up-to-date
- Refactor when better patterns emerge
- Measure and track code quality metrics

### 3. **Consistency**

Maintain consistent coding standards across the entire codebase.

- Enforce style guides with automated linters
- Use consistent naming conventions
- Standardize project structure
- Share common utilities and patterns

### 4. **Modularity**

Design components and functions to be independent, reusable, and testable.

- Single Responsibility Principle (SRP)
- Separation of Concerns (SoC)
- DRY (Don't Repeat Yourself)
- KISS (Keep It Simple, Stupid)

## Code Quality

### Type Safety

Use type hints and static type checking to catch errors early.

**Python**:
```python
from typing import Union, Optional, List

def calculate(x: float, y: float) -> float:
    """Calculate sum of two numbers."""
    return x + y

def find_item(items: List[str], query: str) -> Optional[str]:
    """Find item in list, return None if not found."""
    return next((item for item in items if query in item), None)
```

**Best Practices**:
- Always use type hints for function parameters and return types
- Use `Optional[T]` for nullable types instead of `Union[T, None]`
- Run static type checkers (mypy for Python, etc.)

### Code Style and Formatting

Enforce consistent formatting using automated tools.

**Python**:
- **Linter**: `flake8` or `pylint`
- **Formatter**: `black` or `autopep8`
- **Style Guide**: PEP 8

**Configuration Example** (`.flake8`):
```ini
[flake8]
max-line-length = 88
ignore = E203, W503
exclude = .git,__pycache__,.venv,dist,build
```

**Pre-commit Hooks**:
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black
  - repo: https://github.com/PyCQA/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.0.1
    hooks:
      - id: mypy
        additional_dependencies: [types-all]
```

### Documentation

Document code thoroughly for future maintainers.

**Docstring Standards** (Python):
```python
def process_data(data: List[dict], filter_key: str) -> List[dict]:
    """
    Process and filter data based on specified key.
    
    Args:
        data: List of dictionaries to process
        filter_key: Key to use for filtering
        
    Returns:
        List of filtered dictionaries
        
    Raises:
        ValueError: If filter_key is empty
        TypeError: If data is not a list
        
    Example:
        >>> data = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        >>> process_data(data, 'id')
        [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
    """
    if not filter_key:
        raise ValueError("filter_key cannot be empty")
    if not isinstance(data, list):
        raise TypeError("data must be a list")
    
    return [item for item in data if filter_key in item]
```

**Documentation Structure**:
- Function/method: Purpose, parameters, return value, exceptions, examples
- Class: Purpose, attributes, methods overview
- Module: Overview, key classes/functions, usage examples
- Complex logic: Inline comments explaining why, not what

## Testing

Maintain comprehensive test coverage to ensure reliability and catch regressions.

### Test Structure

```python
import unittest
from calculator import add, subtract, divide

class TestCalculator(unittest.TestCase):
    """Test cases for calculator module."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_data = [1, 2, 3, 4, 5]
    
    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        self.assertEqual(add(2, 3), 5)
    
    def test_add_negative_numbers(self):
        """Test addition of negative numbers."""
        self.assertEqual(add(-2, -3), -5)
    
    def test_divide_by_zero_raises_error(self):
        """Test that dividing by zero raises ValueError."""
        with self.assertRaises(ValueError):
            divide(1, 0)
    
    def tearDown(self):
        """Clean up after tests."""
        self.test_data = None
```

### Coverage Requirements

- **Target**: Minimum 80% code coverage
- **Critical paths**: 100% coverage
- **Tools**: `coverage.py`, `pytest-cov`

**Configuration** (`.coveragerc`):
```ini
[run]
branch = True
source = .
omit = */tests/*

[report]
exclude_lines =
    pragma: no cover
    def __repr__
    raise AssertionError
    raise NotImplementedError
    if __name__ == .__main__.:
show_missing = True
skip_covered = False

[html]
directory = coverage_html_report
```

## Dependencies Management

Keep dependencies current and secure.

### Requirements Management

**Python** (`requirements.txt`):
```
# Format: package==version
# Core dependencies
flask==2.3.2
sqlalchemy==2.0.19
requests==2.31.0

# Development dependencies
pytest==7.4.0
black==23.3.0
flake8==6.0.0
mypy==1.0.1
```

**Lock Files** (`requirements-lock.txt`):
```
# Auto-generated lock file for reproducible builds
# Run: pip install -r requirements-lock.txt
flask==2.3.2
    click==8.1.3
    itsdangerous==2.1.2
    jinja2==3.1.2
    werkzeug==2.3.6
```

### Dependency Audit

```bash
# Check for outdated packages
pip list --outdated

# Check for security vulnerabilities
pip-audit

# Update packages safely
pip install --upgrade package-name
```

### Best Practices

- Keep dependencies up-to-date with security patches
- Review changelogs before major version updates
- Use virtual environments to isolate dependencies
- Document dependency requirements clearly
- Remove unused dependencies regularly

## Modernization

Regularly update code to leverage new language features and patterns.

### Python Version Support

- **Minimum**: Python 3.8 (end-of-life: October 2024)
- **Recommended**: Python 3.10+ (current stable)
- **Target**: Latest 2-3 versions

**Version Compatibility Check**:
```python
import sys

if sys.version_info < (3, 8):
    raise RuntimeError("Python 3.8+ required")
```

### Feature Adoption

**Use Modern Python Features**:
```python
# ✓ Good: Type hints (3.5+)
def greet(name: str) -> str:
    return f"Hello, {name}!"

# ✓ Good: Dataclasses (3.7+)
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

# ✓ Good: Pattern matching (3.10+)
match status_code:
    case 200:
        print("Success")
    case 404:
        print("Not found")
    case _:
        print("Other")

# ✗ Avoid: String formatting
result = "Hello, " + name  # Old style
result = "Hello, %s" % name  # Old style
result = f"Hello, {name}"  # ✓ Use f-strings
```

### Refactoring Schedule

- **Monthly**: Review and update documentation
- **Quarterly**: Audit dependencies and security
- **Semi-annually**: Major refactoring and modernization
- **Annually**: Architecture review and strategic updates

## Performance

Monitor and optimize application performance.

### Profiling and Benchmarking

```python
import cProfile
import pstats
from io import StringIO

def profile_function():
    """Profile a function's performance."""
    pr = cProfile.Profile()
    pr.enable()
    
    # Code to profile
    for i in range(10000):
        calculate(i, i+1)
    
    pr.disable()
    s = StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    ps.print_stats(10)  # Print top 10 functions
    print(s.getvalue())
```

### Performance Targets

- **Response time**: < 100ms for typical operations
- **Memory usage**: Monitor and keep stable
- **CPU utilization**: Avoid unnecessary processing
- **Database queries**: Minimize N+1 queries

## Security

Maintain security best practices throughout development.

### Security Checklist

- [ ] Validate all user inputs
- [ ] Use parameterized queries to prevent SQL injection
- [ ] Never hardcode secrets (use environment variables)
- [ ] Keep dependencies updated
- [ ] Use HTTPS for all network communication
- [ ] Implement proper authentication and authorization
- [ ] Log security-relevant events
- [ ] Sanitize error messages (don't leak system details)
- [ ] Use secure defaults
- [ ] Regular security audits

### Secrets Management

```python
import os
from dotenv import load_dotenv

load_dotenv()

# ✓ Good: Use environment variables
api_key = os.getenv("API_KEY")
db_password = os.getenv("DATABASE_PASSWORD")

# ✗ Bad: Hardcoded secrets
api_key = "sk_live_abc123xyz"
db_password = "password123"
```

**.env.example**:
```
API_KEY=your_api_key_here
DATABASE_PASSWORD=your_password_here
LOG_LEVEL=INFO
```

## Continuous Integration

Automate quality checks and testing.

### GitHub Actions Example

```yaml
name: Quality Checks

on: [push, pull_request]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install -r requirements-dev.txt
      
      - name: Lint with flake8
        run: flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
      
      - name: Format check with black
        run: black --check .
      
      - name: Type check with mypy
        run: mypy .
      
      - name: Run tests with coverage
        run: coverage run -m unittest discover && coverage report --fail-under=80
      
      - name: Security audit
        run: pip-audit
```

## Best Practices Checklist

### Before Committing Code

- [ ] Code follows project style guide
- [ ] All tests pass locally
- [ ] Code coverage maintained/improved
- [ ] Type hints added for all functions
- [ ] Docstrings updated
- [ ] No hardcoded secrets or credentials
- [ ] Dependencies are documented
- [ ] Error handling is comprehensive
- [ ] Performance impact considered
- [ ] Security implications reviewed

### Before Releasing

- [ ] All CI/CD checks pass
- [ ] Changelog updated
- [ ] Version number bumped appropriately (semantic versioning)
- [ ] Security vulnerabilities addressed
- [ ] Dependencies updated to latest stable
- [ ] Documentation current and accurate
- [ ] Breaking changes clearly documented
- [ ] Migration guide provided (if applicable)
- [ ] Deployment tested in staging environment
- [ ] Rollback plan prepared

### Code Review Guidelines

**Reviewer Checklist**:
- [ ] Code is readable and maintainable
- [ ] Tests cover new functionality
- [ ] No security vulnerabilities
- [ ] Performance implications considered
- [ ] Documentation is clear and complete
- [ ] Follows project conventions
- [ ] No unnecessary dependencies added
- [ ] Error handling is appropriate

## Tools and Resources

### Essential Tools

- **Linting**: `flake8`, `pylint`, `ruff`
- **Formatting**: `black`, `autopep8`
- **Type Checking**: `mypy`, `pyright`
- **Testing**: `pytest`, `unittest`
- **Coverage**: `coverage.py`
- **Security**: `bandit`, `pip-audit`
- **Git Hooks**: `pre-commit`

### Recommended Extensions (VS Code)

- Python
- Pylance
- Black Formatter
- Flake8
- PyTest Explorer
- Code Coverage Gutters

### Learning Resources

- PEP 8 Style Guide: https://pep8.org/
- Python Documentation: https://docs.python.org/3/
- Real Python: https://realpython.com/
- Test-Driven Development: https://testdriven.io/
- Security Best Practices: https://owasp.org/

## Maintenance Schedule

### Daily

- Run automated tests
- Monitor application logs
- Check for security alerts

### Weekly

- Review code quality metrics
- Update minor dependencies
- Test on supported Python versions

### Monthly

- Comprehensive dependency audit
- Performance review
- Documentation updates

### Quarterly

- Major version updates
- Architecture review
- Team training and knowledge sharing

### Annually

- Strategic architecture review
- Long-term roadmap planning
- Technology stack evaluation

---

**Last Updated**: October 22, 2025
**Version**: 1.0.0
**Maintainer**: Development Team