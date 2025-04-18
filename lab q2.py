def compute(n):
    n_str = str(n)
    result = int(n_str) + int(n_str * 2) + int(n_str * 3) + int(n_str * 4)
    return result

for digit in range(4, 8):
    result = compute(digit)
    print(f"Result for {digit}: {result}")
