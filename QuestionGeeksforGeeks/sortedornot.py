from tkinter.messagebox import YES

# Solution 1
def sorted(l):
    a=l[0]
    for i in l[1:]:
        if a<=i:
            return True
        else:
            return False

l=[1,2,3]
print(sorted(l))


def insorted(l):
    i=1
    while i<len(l):
        if l[i]<l[i-1]:
            return False
        i=i+1
    return True

l=[100,20,30]
print(insorted(l))

