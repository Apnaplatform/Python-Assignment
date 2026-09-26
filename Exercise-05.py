# Login System

userName = input("Enter your name :")

if userName == "admin":
    password = input("Enter your password :")
    
    if password == "12345":
        role = input("Enter your role :")
        
        if role == "admin":
            print("Full access")
        elif role == "teacher": 
            print("Teacher dashboard")
        elif role == "student":
            print("Student dashboard")
        else:
            print("Invalid role")
            
    else:
        print("Wrong password") 
        
else:
    print("Invalid Username")  
