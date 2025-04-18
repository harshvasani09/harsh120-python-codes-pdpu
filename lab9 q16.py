def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)

a = int(input("Enter the base (a): "))
b = int(input("Enter the exponent (b): "))

result = power(a, b)

print(f"{a} raised to the power {b} is {result}")
