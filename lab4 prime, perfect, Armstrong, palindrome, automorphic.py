n = int(input("Enter number: "))

# Prime
p = all(n%i != 0 for i in range(2, n)) if n > 1 else False
print("Prime" if p else "Not Prime")

# Perfect
s = sum(i for i in range(1, n) if n % i == 0)
print("Perfect" if s == n else "Not Perfect")

# Armstrong
a = sum(int(d)**len(str(n)) for d in str(n))
print("Armstrong" if a == n else "Not Armstrong")

# Palindrome
print("Palindrome" if str(n) == str(n)[::-1] else "Not Palindrome")

# Automorphic
sq = n**2
print("Automorphic" if str(sq).endswith(str(n)) else "Not Automorphic")
