# Shopping Cart Classification

products = {
    "Mobile": 15000,
    "Mouse": 500,
    "Laptop": 60000,
    "Keyboard": 1200
}

for products, price in products.items():
    if price >= 5000:
        print(products,"Premium Product")
    elif price >= 1000:
        print(products,"Expancive Product")
    else:
       print(products,"Affordable Product") 