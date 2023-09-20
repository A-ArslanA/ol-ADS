def calculate_factorial(n):
    if n == 1 or n == 0:
        return 1
    if n < 0:
        return None
    return calculate_factorial(n - 1) * n