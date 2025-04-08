#3.Create a nested dictionary of three employees, each with keys for name, age, and salary. Write a function to give each employee a 10% raise and print the updated dictionary.
print("3")
employees = {
    "employee1": {"name": "Abitha", "age": 24, "salary": 15000},
    "employee2": {"name": "Guru", "age": 23, "salary": 16000},
    "employee3": {"name": "Harina", "age": 24, "salary": 15500}
}

for employee in employees.values():
    employee["salary"] *= 1.10  
    
print(employees)
print("\n")
