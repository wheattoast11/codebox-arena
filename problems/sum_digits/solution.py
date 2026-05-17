def sum_digits(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    return sum(int(d) for d in str(n))
