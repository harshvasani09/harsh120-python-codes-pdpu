import random

numbers = [random.randint(-50, 50) for i in range(30)]
print("Here is a list of 30 randomly generated numbers (can include positive, negative, and zero):")
print(numbers)

positive_numbers = [num for num in numbers if num > 0]

negative_numbers = [num for num in numbers if num < 0]

print("\nList of positive numbers from the original list:")
print(positive_numbers)

print("\nList of negative numbers from the original list:")
print(negative_numbers)

zero_count = numbers.count(0)
if zero_count > 0:
    print("\nNote: There", "is" if zero_count == 1 else "are", zero_count, "zero" + ("" if zero_count == 1 else "s"), "in the original list.")
