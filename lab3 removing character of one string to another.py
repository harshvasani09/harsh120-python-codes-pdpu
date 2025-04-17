main = input("Enter main string: ")
remove = input("Enter characters to remove: ")
result = ''
for ch in main:
    if ch not in remove:
        result += ch
print("Final string:", result)
