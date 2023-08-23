from itertools import count


def apper(l):
    c=None
    for x in l:
        count=l.count(x)
        if count%2!=0:
            c=x
    return c
            
l=[10,20,20,10,40,40,50]
print(apper(l))

def appear(l):
    res =0              
    for x in l:
        res = res ^ x     # XOR Operation
    return res            # x^x = 0 and x^0=x  
l=[10,20,20,10,40,40,50]
print(appear(l))


