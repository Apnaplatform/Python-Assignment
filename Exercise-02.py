# Student result System

python = int(input("Enter python marks : "))
if(python>=40):
    java = int(input("Enter java marks : "))
    if(java>=40):
      dbms = int(input("Enter dbms marks : "))
      if(dbms >= 40):
         totalMarks = python+java+dbms
         per=totalMarks/3
         if(per>=75):
            print("Student per is :",per)
            print("Grade A+")
         elif(per>=60):
            print("Student per is :",per)
            print("Grade A")
         elif(per>=50):
            print("Student per is :",per)
            print("Grade B")
         else:
            print("Student per is :",per)
            print("Student Pass")
      else:
         print("Student Fail in dbms")
    else:
        print("Student Fail in java")
else:
    print("Student Fail in python")
            
            
