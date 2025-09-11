temp = int(input("Enter temperature (°C): "))

if temp <= 0:
    print("Freezing")
elif temp <= 10:
    print("Extremely cold")
elif temp <= 20:
    print("Cold")
elif temp <= 30:
    print("Mild")
elif temp <= 40:
    print("Warm")
elif temp <= 50:
    print("Hot")
elif temp <= 100:
    print("Very hot")
elif temp <= 1000:
    print("Dangerous")
else:
    print("Unrealistic")
