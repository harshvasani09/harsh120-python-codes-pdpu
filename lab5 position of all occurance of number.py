import random

numbers = [random.randint(1, 50) for _ in range(20)]
print("Here's the list of 20 random numbers:")
print(numbers)

user_number = int(input("\nEnter a number to search for in the list: "))

positions = [index for index, value in enumerate(numbers) if value == user_number]

if positions:
    print(f"\nThe number {user_number} was found at the following position(s): {positions}")
else:
    print(f"\nSorry, the number {user_number} does not appear in the list.")
