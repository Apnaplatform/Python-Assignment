# Employee details

def employee_details(**deatails):
    

    for key, value in deatails.items():
        print(key, ":", value)

employee_details(Name="Satyam",
Department="IT",
Salary=50000,
City="Bangalore",
Experience=5)
