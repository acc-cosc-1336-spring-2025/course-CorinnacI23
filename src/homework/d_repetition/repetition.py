# repetition.py

# Function to get the factorial of a number using a for range loop
def get_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

# Function to sum odd numbers up to a given number using a while loop
def sum_odd_numbers(num):
    total = 0
    i = 1
    while i <= num:
        if i % 2 != 0:
            total += i
        i += 1
    return total
