#programing
#three types of loop , for loop ,while looop and do while loop
#while and for loop
#for loop if you have a definite stopping point
#while loop if your stopping point is conditional
#boolean stopping point
#implement keywords while , break, continue

isDirty = True #boolean stopping point 

while isDirty == True:
    wash_again = input("Continue washing the cloths (yes / no)--> ").lower()

    if wash_again == "yes":
        print("Washing the clothes again ...")
        continue
    else:
        print("Washing stops now...")
        break

