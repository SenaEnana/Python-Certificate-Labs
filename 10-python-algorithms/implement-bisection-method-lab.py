def square_root_bisection(number, tolerance=1e-7, max_iterations=100):
    # 1. Handle negative numbers
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    
    # 2. Handle base cases 0 and 1
    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number
    
    # 3. Initialize boundaries for the bisection method
    # For numbers less than 1 (e.g., 0.25), the square root is larger than the number itself (e.g., 0.5)
    low = 0.0
    high = max(1.0, number)
    
    for _ in range(max_iterations):
        mid = (low + high) / 2.0
        
        # Check if the interval size is within the acceptable tolerance margin
        if (high - low) <= tolerance:
            print(f"The square root of {number} is approximately {mid}")
            return mid
        
        # Update the search interval based on the midpoint
        if mid * mid < number:
            low = mid
        else:
            high = mid
            
    # 4. Handle failure to converge within the maximum iterations
    print(f"Failed to converge within {max_iterations} iterations")
    return None