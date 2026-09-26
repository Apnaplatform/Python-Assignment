# Product Stock Management

products = {
    "Laptop": 10,
    "Mouse": 3,
    "Keyboard": 0,
    "Monitor": 7,
    "Printer": 2
}

for product, stock in products.items():
    if(stock == 0):
        print(product,"=","Out of Stock")
    elif(stock <= 5):
        print(product,"=","Low Stock")
    else:
        print(product,"=","Stock Available")