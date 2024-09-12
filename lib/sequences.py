def print_fibonacci(length):
    """Prints the Fibonacci sequence up to the specified length."""
    if length == 0:
        print('[]')
        return

    fib_sequence = [0]  # Start with the first Fibonacci number

    if length == 1:
        print(fib_sequence)
        return

    fib_sequence.append(1)  # Add the second Fibonacci number

    for i in range(2, length):
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)

    print(fib_sequence)