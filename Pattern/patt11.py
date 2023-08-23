n=int(input("Enter the value of n - "))
i=1
a=65
while i<=n:
    j=1
    while j<=n:
        print(chr(a),end=" ")
        j+=1
    print()
    a+=1
    i+=1