# student performance

students = {
    "Rahul": 75,
    "Amit": 32,
    "Priya": 88,
    "Neha": 39,
    "Rohit": 55
}

for name,marks in students.items():
    if (marks>=80):
        print(name ,"Excellent")
    elif (marks>=60):
        print(name ,"Good")
    elif (marks>=40):
            print(name ,"Average")
    else:
        print(name ,"Fail")