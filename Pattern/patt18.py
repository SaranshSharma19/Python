n = int(input("Enter the number n- "))
i=1
while i<=n:
    space = n-i
    j=1
    while j<=n-i+1:
        print("*",end=" ")
        j+=1
    print()
    i+=1