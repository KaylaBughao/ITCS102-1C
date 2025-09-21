print("ODD NUMBER ACCUMULATOR")
print("Enter 10 numbers. We'll sum only the odd ones!\n")

odd_sum = 0
for i in range(1, 11):
    number = int(input(f"Enter number {i}: "))
    if number % 2 != 0:  
        odd_sum += number
        print(f"{number} is odd, added to the sum. Current sum: {odd_sum}")
    else:
        print(f"{number} is even, not added.")

print("\nSum of all odd numbers:", odd_sum)

