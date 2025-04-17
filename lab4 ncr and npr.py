n = int(input("Enter n: "))
r = int(input("Enter r: "))
f = 1
for i in range(1, n+1): f *= i
fn = f
f = 1
for i in range(1, r+1): f *= i
fr = f
f = 1
for i in range(1, n-r+1): f *= i
fnr = f
print("nCr:", fn // (fr * fnr))
print("nPr:", fn // fnr)
