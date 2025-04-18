lst = [("harsh",), "khushi", ("Shyam",), "shreya"]
boys = girls = 0
for x in lst:
    if isinstance(x, tuple):
        boys += 1
    else:
        girls += 1
print("Boys:", boys, "Girls:", girls)
