# user input 
name = input("Hi, what is your name? -->")
sum = 0
odd = ""
print("\n++++++++++++++++++++++++++++++++++++")
print("\nODD NUMBER SELECTOR,press 0 to stop the loop.")

number = True

while number == True:
    random = eval(input("\nInput a random number-->"))

    if random % 2 == 1:
        print("Odd number detected")
        sum += random
        odd += str(random) + " "
        continue
    elif random == 0:
        print("Loop Terminated.")
        break
    else: 
        if random % 2 == 0:
            print("Even number detected")
        else:
            print("Ivalid input, please try again.")
            continue
print("Hi",name,"the summation of all the odd numbers is",sum)
print("The Odd numbers are the ff", odd)