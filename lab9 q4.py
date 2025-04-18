def sum_avg(m1, m2, m3, m4, m5):
    total = m1 + m2 + m3 + m4 + m5
    average = total / 5
    
    return total, average

marks = [80, 75, 90, 85, 88] 
total, average = sum_avg(*marks) 

print(f"Total marks: {total}")
print(f"Average marks: {average:.2f}")
