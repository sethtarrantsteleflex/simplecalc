"""Unit tests for calculator module."""

import unittest
from unittest.mock import MagicMock
from simplecalc.calculator import (
    add, subtract, multiply, divide,
    calculate, DIVISION_BY_ZERO_ERROR, INPUT_ERROR, MATH_ERROR
)


class TestCalculator(unittest.TestCase):
    """Test cases for calculator module."""

    def test_add(self):
        """Test addition of numbers."""
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(1.5, 2.5), 4.0)

    def test_calculate_add(self):
        """Test calculate function with addition operation."""
        mock_entry_num1 = MagicMock()
        mock_entry_num2 = MagicMock()
        mock_operation_var = MagicMock()
        mock_result_label = MagicMock()

        mock_entry_num1.get.return_value = '3'
        mock_entry_num2.get.return_value = '5'
        mock_operation_var.get.return_value = '+'

        calculate(
            mock_entry_num1,
            mock_entry_num2,
            mock_operation_var,
            mock_result_label
        )
        result = mock_result_label.config.call_args[1]['text']
        self.assertEqual(result, "Result: 8.0")

    def test_subtract(self):
        """Test subtraction of numbers."""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(1, 1), 0)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(10.5, 2.5), 8.0)

    def test_calculate_subtract_w_negative_result(self):
        """Test calculate function with subtraction resulting in negative number."""
        mock_entry_num1 = MagicMock()
        mock_entry_num2 = MagicMock()
        mock_operation_var = MagicMock()
        mock_result_label = MagicMock()

        mock_entry_num1.get.return_value = '30'
        mock_entry_num2.get.return_value = '53'
        mock_operation_var.get.return_value = '-'

        calculate(
            mock_entry_num1,
            mock_entry_num2,
            mock_operation_var,
            mock_result_label
        )
        result = mock_result_label.config.call_args[1]['text']
        self.assertEqual(result, "Result: -23.0")

    def test_calculate_subtract_w_positive_result(self):
        """Test calculate function with subtraction resulting in positive number."""
        mock_entry_num1 = MagicMock()
        mock_entry_num2 = MagicMock()
        mock_operation_var = MagicMock()
        mock_result_label = MagicMock()

        mock_entry_num1.get.return_value = '50'
        mock_entry_num2.get.return_value = '13'
        mock_operation_var.get.return_value = '-'

        calculate(
            mock_entry_num1,
            mock_entry_num2,
            mock_operation_var,
            mock_result_label
        )
        result = mock_result_label.config.call_args[1]['text']
        self.assertEqual(result, "Result: 37.0")

    def test_multiply(self):
        """Test multiplication of numbers."""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(1.5, 2), 3.0)

    def test_calculate_multiply(self):
        """Test calculate function with multiplication operation."""
        mock_entry_num1 = MagicMock()
        mock_entry_num2 = MagicMock()
        mock_operation_var = MagicMock()
        mock_result_label = MagicMock()

        mock_entry_num1.get.return_value = '50'
        mock_entry_num2.get.return_value = '13'
        mock_operation_var.get.return_value = '*'

        calculate(
            mock_entry_num1,
            mock_entry_num2,
            mock_operation_var,
            mock_result_label
        )
        result = mock_result_label.config.call_args[1]['text']
        self.assertEqual(result, "Result: 650.0")

    def test_divide(self):
        """Test division of numbers."""
        self.assertEqual(divide(6, 2), 3.0)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(-6, 2), -3.0)
        self.assertEqual(divide(0, 5), 0.0)
        self.assertEqual(divide(1, 0), "Error: Division by zero")

    def test_calculate_divide(self):
        """Test calculate function with division operation."""
        mock_entry_num1 = MagicMock()
        mock_entry_num2 = MagicMock()
        mock_operation_var = MagicMock()
        mock_result_label = MagicMock()

        mock_entry_num1.get.return_value = '40'
        mock_entry_num2.get.return_value = '2'
        mock_operation_var.get.return_value = '/'

        calculate(
            mock_entry_num1,
            mock_entry_num2,
            mock_operation_var,
            mock_result_label
        )
        result = mock_result_label.config.call_args[1]['text']
        self.assertEqual(result, "Result: 20.0")

    def test_calculate_divide_by_zero_error(self):
        """Test calculate function with division by zero."""
        mock_entry_num1 = MagicMock()
        mock_entry_num2 = MagicMock()
        mock_operation_var = MagicMock()
        mock_result_label = MagicMock()

        mock_entry_num1.get.return_value = '40'
        mock_entry_num2.get.return_value = '0'
        mock_operation_var.get.return_value = '/'

        calculate(
            mock_entry_num1,
            mock_entry_num2,
            mock_operation_var,
            mock_result_label
        )
        result = mock_result_label.config.call_args[1]['text']
        self.assertEqual(result, MATH_ERROR)

    def test_divide_by_zero(self):
        """Test divide function with zero divisor."""
        self.assertEqual(divide(1, 0), DIVISION_BY_ZERO_ERROR)

    def test_invalid_operation(self):
        """Test calculate function with invalid operation."""
        mock_entry_num1 = MagicMock()
        mock_entry_num2 = MagicMock()
        mock_operation_var = MagicMock()
        mock_result_label = MagicMock()

        mock_operation_var.get.return_value = '%'

        calculate(
            mock_entry_num1,
            mock_entry_num2,
            mock_operation_var,
            mock_result_label
        )
        mock_result_label.config.assert_called_with(
            text="Result: Invalid operation"
        )

    def test_invalid_input(self):
        """Test calculate function with invalid input."""
        mock_entry_num1 = MagicMock()
        mock_entry_num2 = MagicMock()
        mock_operation_var = MagicMock()
        mock_result_label = MagicMock()

        mock_entry_num1.get.return_value = 'abc'
        mock_entry_num2.get.return_value = '123'

        calculate(
            mock_entry_num1,
            mock_entry_num2,
            mock_operation_var,
            mock_result_label
        )
        mock_result_label.config.assert_called_with(text=INPUT_ERROR)

    def test_division_edge_cases(self):
        """Test division with edge cases."""
        self.assertAlmostEqual(divide(1e308, 1e308), 1.0)
        self.assertEqual(divide(0, 1e308), 0.0)


if __name__ == '__main__':
    unittest.main()
