"""Utility functions for the calculator project."""


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference between two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return a divided by b, rejecting division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def absolute_value(value: float) -> float:
    """Return the non-negative magnitude of a number."""
    return abs(value)


def remainder(a: int, b: int) -> int:
    """Return the remainder of a divided by b, rejecting zero divisors."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a % b


def power(base: float, exponent: float) -> float:
    """Return base raised to the supplied exponent."""
    return base**exponent
