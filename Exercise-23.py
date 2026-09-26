# Find the smallest number in a list

data =[22, 55, 12, 89, 34, 67]

smallest = data[0]

for i in data:
    if i < smallest:
        smallest = i
print("smallest number =", smallest)




