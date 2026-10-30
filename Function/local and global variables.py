# local variable
def show():
    x=20
    print("local variable : ",x)
show()

# global variable
x = 20
def show():
    global x
    x=20
    print("global variable : ",x)
show()
print("global variable : ",x)


def display():
    global x
print("global variable :",x)
display()

balance= 2000
def show():
    global balance
    deposit=1000
    print("deposit :",deposit)
    balance=balance+deposit
show()
print("balance :",balance)

