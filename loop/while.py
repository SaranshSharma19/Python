i=1
while i<10:
    print(i)
    i+=1

"""
The break Statement
With the break statement we can stop the loop even 
if the while condition is true:

"""
j=1
while j<6:
    print(j)
    if j==3:
        break
    j=j+1

m=0
while m<6:
    m=m+1
    if m==3:
        continue
    print(m)

s=1
while s<6:
    print(s)
    s+=1
else:
    print("s is no longer less than 6")