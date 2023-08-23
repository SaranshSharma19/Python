# Using Slicing
l=[10,20,30,40]
l=l[1:]+l[0:1]
print(l)

# Using Append and Pop operation
l=[10,20,30,50]
l.append(l.pop(0))
print(l)

# Using Function
def rleft(l):
    n=len(l)
    x=l[0]
    for i in range(1,n):
        l[i-1]=l[i]
    l[n-1]=x

l=[10,20,30,60]
rleft(l)
print(l)