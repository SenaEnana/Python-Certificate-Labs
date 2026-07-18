def fibonacci(n):
    # 1. Initialize the sequence list exactly as required
    sequence = [0, 1]
    
    # 2. Handle base cases if n is already within the initialized sequence
    if n < len(sequence):
        return sequence[n]
        
    # 3. Iteratively calculate and append next Fibonacci numbers up to n
    for i in range(2, n + 1):
        # Calculate the next number using the two preceding values
        next_fib = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_fib)
        
    # 4. Return the n-th Fibonacci number
    return sequence[n]