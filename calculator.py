import tkinter as tk
from tkinter import messagebox


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y


def calculate():
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
            if result == "Error: Division by zero":
                messagebox.showerror("Math Error", "Division by zero is not allowed.")
                result_label.config(text="Result: ")
                return
        else:
            result = "Invalid operation"

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")


# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Input fields and labels
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="First Number:").grid(row=0, column=0, padx=10, pady=10)

tk.Label(root, text="Second Number:").grid(row=1, column=0, padx=10, pady=10)

# Operation buttons
operation_var = tk.StringVar(value='+')
operations = ['+', '-', '*', '/']

for i, op in enumerate(operations):
    tk.Radiobutton(root, text=op, variable=operation_var, value=op).grid(
        row=i, column=2, padx=10, pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=4, column=0, columnspan=3, pady=10)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=5, column=0, columnspan=3, pady=10)

# Run the application
root.mainloop()
