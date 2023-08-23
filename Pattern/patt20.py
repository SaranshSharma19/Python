n = int(input("Enter the number n- "))
i=1
count=1
while i<=n:
    space = n-i
    j=0
    while j<i:
        print(count+j,end=" ")
        j+=1
    start = i-1
    while start:
        print(start,end=" ")
    