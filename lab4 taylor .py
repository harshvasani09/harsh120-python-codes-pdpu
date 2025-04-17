import math

angle_degrees = float(input("Enter an angle in degrees: "))


x = angle_degrees * math.pi / 180

sin_approx = x  
sign = -1       

for i in range(3, 15, 2): 
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j 
    
    term = (x ** i) / factorial
    sin_approx += sign * term  
    sign *= -1  

print(f"\nApproximate value of sin({angle_degrees}°): {sin_approx:.6f}")
