s = input("Enter a string: ")
res = ''
for ch in s:
    if 'A' <= ch <= 'Z':
        res += chr(ord(ch) + 32)
    else:
        res += ch
print("Lowercase:", res)


s = input("Enter a string: ")
res = ''
for ch in s:
    if 'a' <= ch <= 'z':
        res += chr(ord(ch) - 32)
    else:
        res += ch
print("Uppercase:", res)


s = input("Enter a string: ")
res = ''
for ch in s:
    if 'a' <= ch <= 'z':
        res += chr(ord(ch) - 32)
    elif 'A' <= ch <= 'Z':
        res += chr(ord(ch) + 32)
    else:
        res += ch
print("Toggled:", res)
