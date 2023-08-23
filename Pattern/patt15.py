n=int(input("Enter the value of n - "))
i=1
a=65
while i<=n:
    j=1
    while j<=i:
        print(chr(a),end=" ")
        a+=1
        j+=1
    print()
    i+=1