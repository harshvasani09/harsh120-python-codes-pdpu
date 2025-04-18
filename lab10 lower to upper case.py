with open("source.txt", "r") as src:
    content = src.read()

upper_content = content.upper()

with open("destination.txt", "w") as dest:
    dest.write(upper_content)

print("Content copied and converted to uppercase successfully!")
