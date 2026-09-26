# Nested Dictionary – Employee Experience

employees = {
    "Rahul": {"salary": 60000, "experience": 6},
    "Amit": {"salary": 55000, "experience": 3},
    "Priya": {"salary": 45000, "experience": 4},
    "Neha": {"salary": 30000, "experience": 1}
}

for name,data in employees.items():
    salary = data["salary"]
    experience = data["experience"]

    if salary >= 50000:
        if experience >= 5:
            print(name,":","Senior")
        else:
            print(name,":","Mid-Level")
    else:
        if (experience >= 3):
            print(name,":","Experienced Junior")
        else:
            print(name,":","Fresher/Junior")