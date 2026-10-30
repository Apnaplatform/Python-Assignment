# Bank Loan Eligibility

age = int(input("enter your age :"))
if(age>=21):
    salary = int(input("enter you salary :"))
    if(salary>=25000):
        credit_score = int(input("enter your credit_score :"))
        if(credit_score>=750):
            print("Loan Apporved")
            print("intereast Rate : 8% ")
        elif(credit_score>=650):
           print("Loan approved with higher interest")
           print("intereast Rate : 10% ")
        else:
            print("Loan Rejected ")
    else:
        print("salary Low ")
else:
    print("invalid age ")