import pickle

class Employee:
    def __init__(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.doj = doj
        self.salary = salary

emp = Employee(101, "John Doe", "2023-05-12", 50000)

# Serialize
with open("employee.pkl", "wb") as file:
    pickle.dump(emp, file)

# Deserialize
with open("employee.pkl", "rb") as file:
    loaded_emp = pickle.load(file)
    print(vars(loaded_emp))
