def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b

def divide(a: int, b: int) -> float:
    """Return the quotient of two integers, raising a ValueError on division by zero."""
    if b == 0:
        raise ValueError("Division by zero")
