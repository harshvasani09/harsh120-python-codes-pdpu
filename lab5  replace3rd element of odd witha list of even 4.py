import random
print("Let's generate some random numbers!\n")

odd_numbers = random.sample([i for i in range(1, 100, 2)], 5)
print("Original list of 5 odd integers:", odd_numbers)

even_numbers = random.sample([i for i in range(2, 101, 2)], 4)
print("List of 4 even integers:", even_numbers)
odd_numbers[2] = even_numbers
print("\nAfter replacing the 3rd element with the even number list:")
print("Nested list:", odd_numbers)

flattened_list = []
for item in odd_numbers:
    if isinstance(item, list):
        flattened_list.extend(item)  
    else:
        flattened_list.append(item)

print("\nFlattened list:", flattened_list)

sorted_list = sorted(flattened_list)
print("\nSorted list:", sorted_list)

print("\nAll done! ✅")

