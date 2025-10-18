n = 8
for a in range(1, n+1):
    print("  " * (n - a), end="")  
    
    for j in range(a, 1, -1):
        print(j, end=" ")
    print("1", end=" ")
    
    for k in range(2, a+1):
        print(k, end=" ")
    print()
    
for a in range(n-1,0,-1):
    print("  " * (n - a), end="")  
    
    for j in range(a, 1, -1):
        print(j, end=" ")
    print("1", end=" ")
    
    for k in range(2, a+1):
        print(k, end=" ")
    print()