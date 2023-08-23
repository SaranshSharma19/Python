# Solution 1
def amx(n):
        if not l:
            return None
        else:
            a=l[0]
            for i in range(1,len(l)):
                if l[i]>a:
                    a=l[i]
            return a
l=[1,2,30,770,89,12]
print(amx(l))

def getsecmax(l):
    if len(l)<=1:
        return None
    lar=amx(l)
    slar=None
    for x in l:
        if x!=lar:
            if slar==None:
                slar=x
            else:
                slar=max(slar,x)
    return slar
print(getsecmax(l))

# Solution 2
def getseclar(l):
    if len(l)<=1:
        return None
    lar=l[0]
    secl=None
    for i in l[1:]:
        if i>lar:
            secl=lar
            lar=i
            
        elif i!=lar:
            if secl==None or secl<i:
                secl=i
    return secl

l=[1,2,10]
print(getseclar(l))