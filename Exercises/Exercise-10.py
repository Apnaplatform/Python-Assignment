# ATM

correct_pin = 1234

pin = int(input("Enter PIN: "))

if pin != correct_pin:
    print("Incorrect PIN")

else:
    account_active = input("Is account active? (yes/no): ").lower()

    if account_active != "yes":
        print("Account is not active")

    else:
        balance = float(input("Enter account balance: ₹"))
        amount = float(input("Enter withdrawal amount: ₹"))

        if amount <= 0:
            print("Amount must be positive")

        elif amount % 100 != 0:
            print("Amount must be a multiple of ₹100")

        elif amount > balance:
            print("Insufficient balance")

        elif balance - amount < 500:
            print("Withdrawal denied. Minimum ₹500 balance must remain")

        elif amount > 20000:
            verification = input("Extra verification required. Enter yes/no: ").lower()

            if verification == "yes":
                balance = balance - amount
                print("Withdrawal successful")
                print("Remaining Balance = ₹", balance)
            else:
                print("Extra verification failed")

        else:
            balance = balance - amount
            print("Withdrawal successful")
            print("Remaining Balance = ₹", balance)