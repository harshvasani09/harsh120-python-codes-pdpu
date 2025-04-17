number = int(input("Please enter a number to see its multiplication table: "))

print(f"\nMultiplication Table for {number}:\n" + "-" * 30)

for i in range(1, 11):
    result = number * i
    print(f"{number} × {i} = {result}")
