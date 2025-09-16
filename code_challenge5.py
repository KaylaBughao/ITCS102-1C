number = eval(input("wait for talk later --> "))
factorial = 0
for t in range(number, 0, -1):
    factorial *= t
print("The factorial of ",number, " is",factorial)