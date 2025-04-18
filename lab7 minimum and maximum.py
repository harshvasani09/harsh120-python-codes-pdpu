salaries = {
    "Teaching": [30000, 32000, 31000],
    "Admin": [25000, 27000],
    "Support Staff": [18000, 19000, 17500]
}

for department in salaries:
    min_salary = min(salaries[department])
    max_salary = max(salaries[department])
  
    print(f"{department} - Min Salary: ₹{min_salary}, Max Salary: ₹{max_salary}")
