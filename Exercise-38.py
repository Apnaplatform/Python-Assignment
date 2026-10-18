products = [["watch",1000],["phone",20000],["laptop",50000],["tablet",15000]]

for product in products:
    if product[1] <= 20000:
        print("product name:", product[0])
        print("product price:", product[1])