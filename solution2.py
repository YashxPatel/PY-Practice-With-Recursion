# Write code for algorithm 2 below

def print_natural_numbers(n):
    if n <= 0:
        print("Invalid input. Please provide a positive number.")
        return

    for i in range(1, n + 1):
        print(i)

print_natural_numbers(3)
