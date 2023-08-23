# Solution 1
def reverse(l):
    c=[]
    for x in l[::-1]:
        c.append(x)
    return c

l=[10,20,30,40]
print(reverse(l))

# Solution 2
def reverselist(l):
    s=0
    e=len(l)-1
    while s<e:
        l[s],l[e]=l[e],l[s]
        s=s+1
        e=e-1
    return l

l=[10,20,30,40]
print(reverselist(l))