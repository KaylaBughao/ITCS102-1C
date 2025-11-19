from activity23_1 import *

print("WELCOME TO MY COMPILER PROGRAM ")
name = input("Hi Vistitor, what is your name --> ")

print(f"hello  {name}, select from the option below ")
print("J - Greet name\n8 - Greet with name, age,location \n c- traingle \n e- exit ")

isCont = True

while isCont == True:
    choice = input("Select from A - E --> ").Lower()

    if choice == 'a':
       name = input("Please state your name ")
       Friendname(name)
       continue
    elif choice == 'b':
        number = eval(input("Input amy number --> "))
        print(f"Factorial of {number} is {FactorialMath (number)} ")
        continue
    elif choice == 'e':
        print("program terminated ... ")
        break
    else:
        print("invalid choice ")
        continue