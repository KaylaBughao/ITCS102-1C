

def Friendname(name):
    print(f"HI {name}, do  you have a crush?")

def GreetFriend(name, loc, age):
    print(f"Hi {name} from {loc} , {age} yr\'s old")

def FuntionMath(number):
    print(f"This calculates the summation from 1 to {number}")
    add = 0
    for a in range(1, number + 1, 1):
        add += a
    return add

def FactorialMath(number):
    print(f"This calculates the factorial from 1 to {number}")
    edd += 1
    for a in range(number, 0,-1):
        edd *= a
    return edd

def Triangle():
    print("\t\t *",end=" ")
for s in range(1,11,1):
    for g in range(10,s,-1):
        print(" ", end=" ")
    for h in range(1,s,1):
        print("*", end=" ")
    for j in range(1,s,1):
        print("*", end=" ")
    print()