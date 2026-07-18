def fibonacci(n):
    sequence = [0, 1]

    if n < len(sequence):
        return sequence[n]

    for i in range(2, n + 1):
        next_fib = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_fib)

    return sequence[n]