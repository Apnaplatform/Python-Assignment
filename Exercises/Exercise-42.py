# Argument Unpacking in Shopping System

def display_prices(*prices):
    print("Product Prices: ")

    for price in prices:
        print("$", price)

def display_product_details(**details):
    print("Product Details:")

    for key, value in details.items():
        print(key, ":", value)

def display_customer(**customer):
    print("Customer Details:")

    for key, value in customer.items():
        print(key, ":", value)


display_prices(100, 50, 20, 15)
display_product_details(Name="Laptop", Brand="Dell", RAM="16GB", Storage="512GB")
display_customer(Name="Satyansh", Email="satyansh@gmail.com", Phone="8976768678", Address="Bareilly")

