print("\t\t *",end=" ")
for s in range(1,10,1):
    for g in range(10,s,-1):
        print(" ", end=" ")
    for h in range(1,s,1):
        print("*", end=" ")
    for j in range(1,s,1):
        print("*", end=" ")
    print()
    

for s in range(1,10,1):
    for g in range(1,s,1):
        print(" ", end=" ")
    for h in range(10,s,-1):
        print("*", end=" ")
    for j in range(10,s,-1):
        print("*", end=" ")
    print()
print("\t\t *",end=" ")