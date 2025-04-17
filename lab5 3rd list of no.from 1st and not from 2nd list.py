list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]

unique_in_list1 = [num for num in list1 if num not in list2]

print("Numbers in first list but not in second:")
print(unique_in_list1)
