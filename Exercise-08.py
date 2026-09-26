# Employee Bonus

experience = float(input("Enter experience in years: "))
salary = float(input("Enter salary: "))
performance = float(input("Enter performance score: "))

if experience >= 1 and salary >= 50000:

    if performance >= 90:
        bonus_percent = 20

    elif performance >= 75:
        bonus_percent = 10

    else:
        bonus_percent = 5

elif salary < 50000:

    if performance >= 90:
        bonus_percent = 15

    else:
        bonus_percent = 5

else:
    bonus_percent = 5

bonus = salary * bonus_percent / 100

print("Bonus Percentage =", bonus_percent, "%")
print("Bonus Amount = ₹", bonus)