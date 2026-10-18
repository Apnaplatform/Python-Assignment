# Student Result System

def studentResult(name, *marks, **details):
    print("Student Name:", name)
    print("Marks:", marks)

    if len(details) > 0:
        print("No subject details provided.")
        
    total = sum(marks)
    average = total/len(marks)

    print("Total Marks:",total)
    print("Average Marks:",average)

    print("===========Additional Information===========")
    for key, value in details.items():
        print(key, ":", value)

studentResult("Rahul", 85, 90, 78, RollNo=101, Class="10th", Section="A")