import random

random_numbers = [random.randint(1, 30) for _ in range(50)]
print("Original list with possible duplicates:\n", random_numbers)

unique_numbers = list(set(random_numbers))
print("\nList after removing duplicates:\n", unique_numbers)

unique_numbers.sort()
print("\nSorted list of unique numbers:\n", unique_numbers)
