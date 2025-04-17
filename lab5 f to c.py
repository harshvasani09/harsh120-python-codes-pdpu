fahrenheit_temps = [32, 68, 77, 95, 104]

print("Original temperatures in Fahrenheit:")
print(fahrenheit_temps)

celsius_temps = [(temp - 32) * 5 / 9 for temp in fahrenheit_temps]

print("\nConverted temperatures in Celsius:")
print([round(temp, 2) for temp in celsius_temps]) 
