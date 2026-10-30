# Employee Salary and Department

employees = {
    "Rahul": {"salary": 60000, "department": "IT"},
    "Amit": {"salary": 40000, "department": "HR"},
    "Priya": {"salary": 70000, "department": "IT"},
    "Neha": {"salary": 45000, "department": "Finance"}
}

for name,data in employees.items():
    salary = data["salary"]
    department = data["department"]

    if salary >= 50000:
        if department == "IT":
            print (name,":","Senior IT Employee")
        elif department == "HR":
                    print (name,":","Senior HR Employee")
        else:
              print(name,":", "Senior Employee")
    else:
        print(name, ":", "Junior Employee")
    
          
        

