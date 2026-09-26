# Check Even/Odd Values

data = {
    "a =": 10,
    "b =": 15,
    "c =": 25,
    "d =": 30,
    "e =": 40
}

for key,value in data.items():
    if value % 2 == 0:

        if value > 20:
            print (key, value,"Large Even")
        else:
            print (key, value,"Even")
    else:
        print (key, value,"Odd")

        