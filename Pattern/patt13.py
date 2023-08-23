n=int(input("Enter the value of n - "))
i=1
a=65
while i<=n:
    j=1
    while j<=n:
        print(chr(a),end=" ")
        j+=1
        a+=1
    print()
    i+=1