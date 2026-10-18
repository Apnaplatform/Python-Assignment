courses = {
    "Java": {"instructor": "Rahul", "duration": 40},
    "Python": {"instructor": "Priya", "duration": 50},
    "JavaScript": {"instructor": "Aman", "duration": 60 },
    "C++": {"instructor": "Rohit", "duration": 65}
}

for course, details in courses.items():
    if course == "Python":
      print("instructor:", details["instructor"])
      print("duration:", details["duration"],"hrs")