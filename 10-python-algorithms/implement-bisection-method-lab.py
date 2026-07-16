def square_root_bisection(number, tolerance=1e-7, max_iterations=100):
    # 1. Handle negative numbers
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    
    # 2. Handle base cases 0 and 1
    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number
    