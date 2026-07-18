def fibonacci(n):
    # 1. Initialize the sequence list exactly as required
    sequence = [0, 1]
    
    # 2. Handle base cases if n is already within the initialized sequence
    if n < len(sequence):
        return sequence[n]
        
    # 3. 
    for i in range(2, n + 1):
        pass