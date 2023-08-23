# Using direct method
from collections import deque


l=[10,20,30,40,50]
d=2
l=l[d:]+l[:d]
print(l)

# From deque container
from collections import deque
l=[10,20,30,40,50]
d=3
dq=deque(l)
dq.rotate(-d) # For left rotate we use - for right rotate we don't need to put - sign
l=list(dq)
print(l)

# using function + append and pop operation
def left(l,d):
    for i in range(0,d):
        l.append(l.pop(0))

l=[10,20,30,40,50]
d=3
left(l,d)
print(l)

