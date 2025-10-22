# simplecalc

Simple calculator repo for testing and evaluating possibilities.

## Overview

This project is a Python-based calculator GUI application with comprehensive unit tests and code coverage analysis. It demonstrates modern Python development practices including type hints, error handling, and test-driven development.

## Features

- **Basic Operations**: Addition, subtraction, multiplication, and division
- **Error Handling**: Graceful handling of division by zero and invalid inputs
- **Type Hints**: Full type annotations for improved code quality
- **Comprehensive Tests**: 16 unit tests with coverage tracking
- **GUI Interface**: Built with tkinter

## Installation

### For Development

```bash
# Install in editable mode with dev dependencies
pip install -e ".[dev]"
```

### For Use

```bash
pip install .
```

## Running program

```bash
# After installation
simplecalc

# Or directly from source
python -m simplecalc.calculator
```

## Running tests

### Via unittest

```bash
python -m unittest -v test_calculator.py
```

### Via coverage

```bash
coverage run -m unittest discover && coverage report
```

### Via VSCode

Use the VSCode Test functionality to run and debug tests directly in the editor.

## Architecture Diagrams

### Class Diagram

```mermaid
classDiagram
    class Calculator {
        +add(x: float, y: float) float
        +subtract(x: float, y: float) float
        +multiply(x: float, y: float) float
        +divide(x: float, y: float) Union[float, str]
        +calculate(entry_num1, entry_num2, operation_var, result_label) None
    }
    
    class Constants {
        DIVISION_BY_ZERO_ERROR
        INPUT_ERROR
        MATH_ERROR
    }
    
    class GUI {
        -entry_num1: tk.Entry
        -entry_num2: tk.Entry
        -operation_var: tk.StringVar
        -result_label: tk.Label
        -calculate_button: tk.Button
    }
    
    Calculator --> Constants
    GUI --> Calculator
```

### Sequence Flow Diagram

```mermaid
sequenceDiagram
    actor User
    participant GUI as GUI Interface
    participant Calc as Calculator
    participant Result as Result Label
    
    User->>GUI: Enter numbers and select operation
    User->>GUI: Click Calculate button
    GUI->>Calc: calculate(entry_num1, entry_num2, operation_var, result_label)
    
    alt Valid Input & Valid Operation
        Calc->>Calc: Parse numbers & get operation
        Calc->>Calc: Execute operation (add/subtract/multiply/divide)
        Calc->>Result: Update label with result
        Result-->>GUI: Display result to user
    else Invalid Input
        Calc->>Result: Display INPUT_ERROR message
        Result-->>GUI: Show error to user
    else Division by Zero
        Calc->>Result: Display MATH_ERROR message
        Result-->>GUI: Show error to user
    else Invalid Operation
        Calc->>Result: Display "Invalid operation"
        Result-->>GUI: Show error to user
    end
```

### Data Flow Diagram

```mermaid
graph LR
    A[User Input<br/>num1, num2] -->|Entry widgets| B[Calculate Function]
    C[Operation Selection<br/>+, -, *, /] -->|StringVar| B
    B -->|Parse & Validate| D{Valid Input?}
    D -->|No| E[Error Handler]
    D -->|Yes| F{Valid Operation?}
    F -->|No| E
    F -->|Yes| G[Execute Operation]
    G -->|add/subtract/multiply/divide| H[Result Computation]
    H -->|format result| I[Update GUI Label]
    E -->|format error| I
    I -->|Display| J[User Output]
```

### Code Coverage Map

```mermaid
graph TD
    A[test_calculator.py]
    B[calculator.py]
    
    A --> A1["test_add<br/>✓ 100%"]
    A --> A2["test_subtract<br/>✓ 100%"]
    A --> A3["test_multiply<br/>✓ 100%"]
    A --> A4["test_divide<br/>✓ 100%"]
    A --> A5["test_divide_by_zero<br/>✓ 100%"]
    A --> A6["test_invalid_operation<br/>✓ 100%"]
    A --> A7["test_invalid_input<br/>✓ 100%"]
    A --> A8["test_division_edge_cases<br/>✓ 100%"]
    
    A1 --> B1["add()"]
    A2 --> B2["subtract()"]
    A3 --> B3["multiply()"]
    A4 --> B4["divide()"]
    A5 --> B5["divide() edge case"]
    A6 --> B6["calculate() - invalid op"]
    A7 --> B7["calculate() - invalid input"]
    A8 --> B8["divide() - edge cases"]
    
    B1 & B2 & B3 & B4 & B5 & B6 & B7 & B8 --> B
    
    style B1 fill:#90EE90
    style B2 fill:#90EE90
    style B3 fill:#90EE90
    style B4 fill:#90EE90
    style B5 fill:#90EE90
    style B6 fill:#90EE90
    style B7 fill:#90EE90
    style B8 fill:#90EE90
```

## Test Coverage

Current test coverage: **100%** of core calculator functions.

- ✓ All arithmetic operations (add, subtract, multiply, divide)
- ✓ Error handling (division by zero, invalid input)
- ✓ Edge cases (large numbers, floating-point precision)
- ✓ GUI integration (calculate function with mocked components)

## Configuration

The project uses `.coveragerc` for coverage configuration:

- **Branch coverage**: Enabled
- **Source**: Current directory
- **Report**: Shows missing lines and skips covered lines
- **HTML output**: Generated in `coverage_html_report/` directory

## Project Structure

```text
simplecalc/
├── src/
│   └── simplecalc/
│       ├── __init__.py           # Package initialization
│       └── calculator.py         # Main calculator module with GUI
├── tests/
│   ├── __init__.py               # Test package initialization
│   └── test_calculator.py        # Unit tests
├── .github/                      # GitHub configuration and documentation
├── .coveragerc                   # Coverage configuration
├── .flake8                       # Flake8 linter configuration
├── .pre-commit-config.yaml       # Pre-commit hooks configuration
├── pyproject.toml                # Project configuration and dependencies
├── requirements-dev.txt          # Development dependencies
├── README.md                     # This file
└── LICENSE                       # Project license
```

This structure follows Python best practices:

- **src/simplecalc/**: Source code in a package directory
- **tests/**: All tests in a dedicated directory
- **pyproject.toml**: Modern Python project configuration
- **Configuration files**: Linting, formatting, and coverage configs at root

## Documentation

- **[Project Structure Guide](.github/PROJECT_STRUCTURE.md)**: Quick reference for the project layout
- **[Migration Guide](.github/MIGRATION_GUIDE.md)**: Detailed migration from old to new structure
- **[Python Instructions](.github/instructions/python.instructions.md)**: Python-specific guidelines
- **[Evergreen Development](.github/instructions/evergreen-development.instructions.md)**: Best practices

## Future Enhancements

- [ ] Support for additional operations (power, modulo, square root)
- [ ] History of calculations
- [ ] Scientific calculator mode
- [ ] Dark theme support
- [ ] Keyboard input support
- [ ] Configuration file for customization
- [ ] Web interface using Flask/FastAPI
- [ ] REST API for calculator operations
