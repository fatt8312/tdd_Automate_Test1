from function_motorcycle import calculate_monthly_payment, calculate_down_Payment, validate_price
import pytest

# Test the calculate_monthly_payment function
def test_calculate_monthly_payment1():
    # Test case 1: Price 100000, down payment 20000
    assert round(calculate_monthly_payment(100000, 20000), 2) == 6848.6

def test_calculate_monthly_payment2():
    # Test case 2: Price 50000, down payment 10000
    assert round(calculate_monthly_payment(50000, 10000), 2) == 3424.3

def test_calculate_monthly_payment3():
    # Test case 3: Price 150000, down payment 30000
    assert round(calculate_monthly_payment(150000, 30000), 2) == 10272.9

# Test the calculate_down_Payment function
def test_minimum_down_input_50000():
    # Test case 4: Price 50000
    assert round(calculate_down_Payment(50000), 2) == 10000

# Test the validate_price function
def test_price_int_input_0_input():
    # Test case 5: Price 0
    assert validate_price(0) == "Invalid input. Please enter a positive number."

def test_price_negative_input():
    # Test case 6: Price -100000
    assert validate_price(-100000) == "Invalid input. Please enter a positive number."

def test_price_negative_float():
    # Test case 7: Price -1000.00
    assert validate_price(-1000.00) == "Invalid input. Please enter a positive number."

def test_price_str_input1():
    # Test case 8: Price is String
    assert validate_price("abc") == "Invalid input. Please enter a positive number."

def test_price_str_input2():
    # Test case 9: Price character
    assert validate_price("@#$%") == "Invalid input. Please enter a positive number."
    