def apper(l):
    c=None
    for x in l:
        count=l.count(x)
        if count%2!=0:
            c=x
    return c
            
l=[10,20,20,10,40,40,50]
print(apper(l))