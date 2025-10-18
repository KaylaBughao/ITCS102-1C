import random

print("Guess a Number")
print("---------------------")

random_value = random.randint(1,50)
even = 0
odd = True


name = input("What's your name?-->")
while odd == True:
    number = eval(input("Guess a number from:"))
    even += 1

    if number == random_value:
        print("You Win")
        break
    else:
        print("Please Guess again.")
        continue

print(f"Hi {name},Congratulations, your odd is correct!, Number of even {even}")