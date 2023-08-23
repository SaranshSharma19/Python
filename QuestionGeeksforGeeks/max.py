# n=int(input())
# sum=0
# while n!=0:
#     sum=sum+n
#     n=n-1
# print(sum)
# from binascii import b2a_hqx


# def func(i):
#     sum=0
#     while i!=0:
#         sum = sum + i
#         i=i-1
#     return sum       #O(n)

# n=int(input())
# print(func(n))

# def func(n):
#     return n*(n+1)/2
# i=int(input())
# print(func(i))      #O(1)


# def func(n):
#     sum=0
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             sum=sum+1
#     return sum
# i=int(input())
# print(func(i))      #O(n^2)

def avg(n):
    sum=0
    for x in n:
        sum=sum+x
    c=len(n)
    return sum/c
l=[10,20,30,40]
print(avg(l))

def avg(n):
    sum=0
    for x in n:
        sum=sum+x
    c=len(n)
    return sum/c
l=[10,20,30,60]
print(avg(l))

def evenandodd(l):
    even=[]
    odd=[]
    for x in l:
        if x%2==0:
            even.append(x)     
        elif x%2!=0:
            odd.append(x)
    return even,odd
l=[10,20,35,43,50]
even,odd=evenandodd(l)
print(even)
print(odd)

def smaller(n):
    s=[]
    d=10
    for x in n:
        if x<d:
            s.append(x)
    return s
l=[8,100,20,40,3,7]
s=smaller(l)
print(s)

def smaller(n):
    s=[]
    d=60
    for x in n:
        if x<d:
            s.append(x)
    return s
l=[100,20,40,60,80,200]
s=smaller(l)
print(s)

# Slicing 
# l=[Start:Stop:Step]   stop not included , first element is always start and we increment by step 
l=[10,20,30,40,50,60,70]
print(l[0:6:1])

# If we copy a list into another list then they both are different but in case of tuple and string they are same


# Comprehensions
# It provide a short cut to make a list from iterable(ie. Range )
li=[x for x in range(11) if x%2==0]
print(li)
l2=[x for x in range(11) if x%2!=0]
print(l2)

l=[100,20,40,60,80,200]
d=60
a=[x for x in l if x<d]
print(a)

l=[8,100,20,40,3,7]
a=[x for x in l if x%2==0]
b=[x for x in l if x%2!=0]
print(a)
print(b)

s="GeeksForGeeks"
l=[x for x in s if x in "aeiou"]
print(l)

l=["geeks","For","geeks","best","for","DSA"]
a=[x.upper() for x in l if x.startswith('g')]
print(a)

l=[1,2,3,4,5]
d1={x:x**3 for x in l}
print(d1)

d1={x:f"ID{x}" for x in range(5)}
print(d1)

l1=[1,2,3]
l2=["geeks","for","geeks"]
d2={l1[i]:l2[i] for i in range(len(l2)) }
print(d2)

# A Better way to create a dictionary item is zip function
l1=[1,2,3]
l2=["geeks","for","geeks"]
d3=dict(zip(l1,l2))
print(d3)

# Solution 1
l1=[1,2,3]
print(max(l1))

# Solution 2
def amx(n):
        if not l:
            return None
        else:
            a=l[0]
            for i in range(1,len(l)):
                if l[i]>a:
                    a=l[i]
            return a
l=[1,2,30,77,89,12]
print(amx(l))

