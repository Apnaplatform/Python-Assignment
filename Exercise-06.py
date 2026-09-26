# Movies ticket system
seats_available = int(input("Enter your seat No. :"))
if (seats_available > 0):
 age = int(input("Enter your age: "))
 if(age < 5):
  print("Free")
 elif(5<=age<=12):
  print("50% discount")
 elif(age>60):
  print("30% discount")
 else:
  print("Full price")
else:
 print("Full house")
