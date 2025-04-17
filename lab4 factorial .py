number = int(input("Please enter a non-negative integer: "))

if number < 0:
    print("Sorry, factorial is not defined for negative numbers.")
else:
    factorial = 1 
    for i in range(1, number + 1):
        factorial *= i 
    print(f"The factorial of {number} is: {factorial}")
