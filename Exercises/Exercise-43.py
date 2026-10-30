# Student Average Marks Calculator

def calculate_average(marks):
    
  if len(marks) > 0:
    print("Error: No Marks provided.")

    for key, value in marks.items():
        print(key, ":", value)

calculate_average(Marks={"maths": 85, "Science": 90, "English": 78, "History": 88})