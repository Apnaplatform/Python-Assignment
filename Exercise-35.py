# Student Marks + Attendance

students = {
    "Rahul": {"marks": 85, "attendance": 90},
    "Amit": {"marks": 35, "attendance": 80},
    "Priya": {"marks": 65, "attendance": 70},
    "Neha": {"marks": 45, "attendance": 85},
    "Rohit": {"marks": 90, "attendance": 60}
}

for name,data in students.items():
    marks = data["marks"]
    attendance = data["attendance"]

    if attendance < 75:
     print(name,":","Not Eligible")
    else:
      if marks >= 80:
        print(name,":", "Distinction")
      elif marks >= 60:
         print(name,":", "First Division")
      elif marks >= 40:
       print(name,":", "Pass")
else:
     print(name,":", "Fail")

