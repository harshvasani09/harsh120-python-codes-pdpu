students = [
    (101, "Aarav", 20),
    (102, "Diya", 21),
    (103, "Kabir", 19),
    (104, "Meera", 22),
    (105, "Rohan", 20)
]

roll_nos = []
names = []
ages = []

for roll_no, name, age in students:
    roll_nos.append(roll_no)
    names.append(name)
    ages.append(age)

print("Roll Numbers:", roll_nos)
print("Names:", names)
print("Ages:", ages)
