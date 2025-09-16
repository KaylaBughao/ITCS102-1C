t = 5
number = eval(input("how much --> "))
factorial = 1 
for t in range(number, 0, -1):
    factorial *= t
print("The factorial of ",number, "is",factorial)   