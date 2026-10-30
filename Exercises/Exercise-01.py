# ATM Withdrawal
balance = 50000
pin=input("Enter your PIN: ")
if pin=="1234":
    amount = int(input("Enter withdrawal amount: "))
    if (amount % 100 == 0):
        if (amount <= balance):
            balance = balance - amount
            print("Withdrawal Successful")
            print("Withdrawn Amount:", amount)
            print("Remaining Balance:", balance)
        else:
            print("Insufficient Balance")
    else:
        print("Amount must be a multiple of 100")
else:
    print("Invalid PIN")