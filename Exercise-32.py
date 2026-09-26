# Student Eligibility

students = {
    "Rahul": {"attendance": 85, "marks": 70},
    "Amit": {"attendance": 60, "marks": 80},
    "Priya": {"attendance": 90, "marks": 35},
    "Neha": {"attendance": 78, "marks": 55}
}

for name, data in students.items():

    attendance = data["attendance"]
    marks = data["marks"]

    if attendance >= 75:
       if marks >= 40:
           print(name,"=","Eligible")
    else:
        print(name,"=","Failed in Exam")
else:
    print(name,"=","Not Eligible")
           
