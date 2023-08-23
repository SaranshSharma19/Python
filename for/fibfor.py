from pyrsistent import b


n=int(input("Enter the value of n- "))
i=0
j=1
print(i,end=" ")
print(j,end=" ")
for a in range(1,n+1):
    nextnum=i+j
    print(nextnum,end=' ')
    i=j
    j=nextnum
