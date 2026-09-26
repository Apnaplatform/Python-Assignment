# 1 to 100 Divisible from 3 and 5 

data = 0

for i in range(1,101):
    if (i % 3 == 0 and i % 5 == 0):
        print(i) 
