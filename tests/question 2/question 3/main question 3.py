def main():
    num = 50  # Initial value of num
    
    # Call the function with num
    use_local_variable(num)
    
    # Display the value of num after calling the function
    print(f"The value of num in main after calling the function: {num}")  # Expected: 50

if __name__ == "__main__":
    main()

def use_local_variable(num):
    # Local variable num inside the function
    num = 10
    # The function does not return anything, num inside the function is local and doesn't affect the global num

def test_use_local_variable():
    num = 100  # Variable outside the function
    use_local_variable(num)  # Call the function with num as the argument
    
    # Show that the value of num outside the function remains unchanged
    print(f"The value of num after calling the function: {num}")  # Expected: 100

def main():
    num = 50  # Initial value of num
    
    # Call the function with num
    use_local_variable(num)
    
    # Display the value of num after calling the function
    print(f"The value of num in main after calling the function: {num}")  # Expected: 50

if __name__ == "__main__":
    # Run the test case
    test_use_local_variable()
    
    # Run the main program
    main()
