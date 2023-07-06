# Write code for algorithm 3 below

def fibonacci_sequence(n):
    if n <= 0:
        print("Invalid input. Please provide a positive integer.")
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        prev_1 = 0
        prev_2 = 1
        for _ in range(3, n + 1):
            current = prev_1 + prev_2
            prev_1, prev_2 = prev_2, current
        return prev_2

number = int(4)
result = fibonacci_sequence(number)
print(f"{number} in the Fibonacci Sequence is:", result)
