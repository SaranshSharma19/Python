n = int(input("Enter the number n- "))
i=1
while i<=n:
    space = n-i
    j=1
    while space:
        print(" ",end= " ")
        space-=1
    while j<=i:
        print("*",end=" ")
        j+=1
    print()
    i+=1
