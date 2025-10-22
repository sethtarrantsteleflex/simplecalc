import tkinter as tk
from typing import Union

# Constants
DIVISION_BY_ZERO_ERROR = "Error: Division by zero"
INPUT_ERROR = "INPUT ERROR! Please enter valid numbers."
MATH_ERROR = "MATH ERROR! Division by zero is not allowed."


def add(x: float, y: float) -> float:
    """Add two numbers."""
    return x + y


def subtract(x: float, y: float) -> float:
    """Subtract the second number from the first."""
    return x - y


def multiply(x: float, y: float) -> float:
    """Multiply two numbers."""
    return x * y


def divide(x: float, y: float) -> Union[float, str]:
    """
    Divide the first number by the second.
    Return an error message if dividing by zero.
    """
    if y == 0:
        return DIVISION_BY_ZERO_ERROR
    return x / y


def calculate(
    entry_num1: tk.Entry,
    entry_num2: tk.Entry,
    operation_var: tk.StringVar,
    result_label: tk.Label
) -> None:
    """Perform the selected operation and display the result."""
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
            if result == DIVISION_BY_ZERO_ERROR:
                result_label.config(text=MATH_ERROR)
                return
        else:
            result = "Invalid operation"

        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text=INPUT_ERROR)


# Create the main window
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Simple Calculator")

    # Input fields and labels
    entry_num1 = tk.Entry(root)
    entry_num1.grid(row=0, column=1, padx=10, pady=10)

    entry_num2 = tk.Entry(root)
    entry_num2.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(root, text="First Number:") \
        .grid(row=0, column=0, padx=10, pady=10)

    tk.Label(root, text="Second Number:") \
        .grid(row=1, column=0, padx=10, pady=10)

    # Operation buttons
    operation_var = tk.StringVar(value='+')
    operations = ['+', '-', '*', '/']

    for i, op in enumerate(operations):
        tk.Radiobutton(root, text=op, variable=operation_var, value=op).grid(
            row=i, column=2, padx=10, pady=5)

    # Calculate button
    calculate_button = tk.Button(
        root,
        text="Calculate",
        command=lambda: calculate(
            entry_num1, entry_num2, operation_var, result_label
        )
    )
    calculate_button.grid(row=4, column=0, columnspan=3, pady=10)

    # Result label
    result_label = tk.Label(root, text="Result: ")
    result_label.grid(row=5, column=0, columnspan=3, pady=10)

    # Run the application
    root.mainloop()
