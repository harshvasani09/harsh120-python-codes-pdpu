import openpyxl
workbook = openpyxl.load_workbook('students.xlsx')
sheet = workbook.active
students_data = {}
for row in sheet.iter_rows(min_row=2, values_only=True):
    roll_no = row[0]
    name = row[1]
    subject1 = row[2]
    subject2 = row[3]
    subject3 = row[4]
    
    total = subject1 + subject2 + subject3
  
    students_data[roll_no] = {
        'Name': name,
        'Subject1': subject1,
        'Subject2': subject2,
        'Subject3': subject3,
        'Total': total
    }
  print("\nStudent Records with Total Marks:\n")
for roll, info in students_data.items():
    print(f"Roll No: {roll}")
    for key, value in info.items():
        print(f"  {key}: {value}")
    print("-" * 30)
