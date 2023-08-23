n=int(input("Enter the value of n - "))
i=1
a=65
while i<=n:
    j=0
    while j<i:
        print(chr(a+j),end=" ")
        j+=1
    print()
    a+=1
    i+=1