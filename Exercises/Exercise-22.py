data =[22, 55, 12, 89, 34, 67]

gretest = data[0]

for i in data:
    if i > gretest:
        gretest = i
print("gretest number =", gretest)