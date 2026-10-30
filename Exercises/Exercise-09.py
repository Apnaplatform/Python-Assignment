# Driving License

age = int(input("Enter age: "))

learner_license = input(
    "Do you have a learner license? (yes/no): "
).lower()

test_score = int(input("Enter driving test score: "))

if age >= 18 and learner_license == "yes" and test_score >= 60:
    print("Driving License Approved")
else:
    print("Driving License Not Approved")