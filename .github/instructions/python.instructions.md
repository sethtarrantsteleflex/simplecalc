# Instructions for the Simple Calculator Project

## Overview
This project is a simple calculator application built using Python. It includes both a graphical user interface (GUI) built with `tkinter` and a set of mathematical operations (addition, subtraction, multiplication, and division). The project also includes unit tests to ensure the correctness of the mathematical operations.

---

## Technologies Used

### 1. Python
- **Version**: Ensure Python 3.10 or higher is installed.
- **Modules**: The project uses the built-in `tkinter` module for the GUI and `unittest` for testing.

### 2. tkinter
- Used for creating the graphical user interface (GUI).
- Provides input fields, buttons, and labels for user interaction.

### 3. unittest
- Python's built-in testing framework.
- Used to test the mathematical operations in the `calculator.py` file.

---

## Setup Instructions

### 1. Install Python
- Download and install Python from [python.org](https://www.python.org/).
- Ensure Python is added to your system's PATH.

### 2. Clone the Repository
```bash
# Clone the repository to your local machine
git clone https://github.com/sethtarrantsteleflex/simplecalc.git
cd simplecalc
```

### 3. Set Up a Virtual Environment (Optional but Recommended)
```bash
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

---

## Running the Application

### 1. Run the Calculator GUI
```bash
python calculator.py
```
This will launch the graphical user interface for the calculator.

---

## Running Tests

### 1. Run All Tests
```bash
python -m unittest -v test_calculator.py
```

### 2. Run Tests in VS Code
- Open the project in VS Code.
- Ensure the Python extension is installed.
- Go to the Testing tab and click "Run All Tests."

---

## Project Structure
```
.
├── calculator.py        # Main application file with GUI and math functions
├── test_calculator.py   # Unit tests for the math functions
├── README.md            # Project documentation
├── LICENSE              # License file
└── __pycache__/         # Compiled Python files (auto-generated)
```

---

## Additional Notes
- Ensure you have the necessary permissions to run Python scripts on your system.
- If you encounter issues, check the Python version and ensure all dependencies are installed.