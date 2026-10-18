sales = [
    [ "Aman", 12000, 15000, 18000],
    ["Priya", 10000, 12000, 14000],
    ["Rohit", 8000, 10000, 12000],
]
highest_sales=0
top_salesperson=""

for person in sales:
    name = person[0]
    total_sales = sum(person[1:])

    print("Name :", name)
    print("Total sales :", total_sales)
    print("...................................")

    if total_sales > highest_sales:
        highest_sales = total_sales
        top_salesperson = name

    print("Top salesperson :", top_salesperson)
    print("Highest sales : ", highest_sales)