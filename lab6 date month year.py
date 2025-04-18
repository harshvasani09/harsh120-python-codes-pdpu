from datetime import date

date1_tuple = (15, 4, 2023)   
date2_tuple = (18, 4, 2025)  

date1 = date(date1_tuple[2], date1_tuple[1], date1_tuple[0])
date2 = date(date2_tuple[2], date2_tuple[1], date2_tuple[0])

difference = abs((date2 - date1).days)

print(f"The number of days between {date1} and {date2} is {difference} days.")
