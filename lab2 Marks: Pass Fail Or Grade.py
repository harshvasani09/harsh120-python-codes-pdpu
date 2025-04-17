def check_results(marks):
    grades = [(0, 39, 'F'), (40, 44, 'P'), (45, 49, 'C'), (50, 54, 'B'), (55, 59, 'B+'),
              (60, 69, 'A'), (70, 79, 'A+'), (80, 100, 'O')]
    
    for i, m in enumerate(marks):
        if m == -1:
            print(f"Subject {i+1}: Absent - Grade: NA")
        else:
            for low, high, g in grades:
                if low <= m <= high:
                    print(f"Subject {i+1}: Grade: {g}")
                    break
    if any(m <= 39 for m in marks if m != -1):
        print("Result: Fail")
    else:
        print("Result: Pass")
    print("Total:", sum(marks), "Average:", sum(marks)/len(marks))
