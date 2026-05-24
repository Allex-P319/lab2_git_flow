def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """
    Return division of a by b.
    If b is zero, print error and return None.
    """
    if b == 0:
        print("Error: division by zero")
        return None
    return a / b


if __name__ == "__main__":
    print("=== SIMPLE CALCULATOR ===")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"2 * 3 = {multiply(2, 3)}")
    result = divide(6, 2)
    if result is not None:
        print(f"6 / 2 = {result}")
