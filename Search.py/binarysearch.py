# def found(n,key):
#     start=0
#     end=len(n)-1
#     mid = (start+end)//2   # optimized s + (e-s)//2
#     while start<=end:
#         if n[mid]==key:
#             return mid
#         elif n[mid]<key:
#             start=mid+1
#         else:
#             end=mid-1
#         mid=(start+end)//2  # optimized s + (e-s)//2
#     return -1

# n=[1,2,3,4,5,6,7,8,9,10]
# key=int(input("Enter The Value Of Key - "))
# print(found(n,key))
# cook your dish here

# t=int(input())
# for i in range(t):
#     n=int(input())
#     l=list(map(int,input().split()))
# print(l)
t=int(input())
for i in range(t):
    n=int(input())
    for j in range(n):
        s=input().split()
print(s)
