import csv

with open('students.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(['Roll No', 'Name', 'Class', 'Marks'])

    writer.writerow([201, 'Neha Rajput', '12C', 91])
    writer.writerow([202, 'Arjun Tiwari', '12A', 87])
    writer.writerow([203, 'Meera Joshi', '11B', 95])
    writer.writerow([204, 'Kunal Thakur', '11C', 82])
    writer.writerow([205, 'Riya Malhotra', '12B', 89])

print("CSV file 'students.csv' has been created with updated student details.")
