def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

if __name__ == "__main__":
    print("Simple calculator")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"2 * 3 = {multiply(2, 3)}")
    result = divide(6, 2)
    if result is not None:
        print(f"6 / 2 = {result}")