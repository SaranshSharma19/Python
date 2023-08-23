# m=[1,2,3,4,5,6,7,8,9]
# n=len(m)
# start=0
# while start<=n:
#     temp=m[n-1]
#     m[n-1]=m[start]
#     m[start]=temp
#     start+=1
#     n-=1
# print(m)
# m="i.love.mummy"
# a=[]
# s=m[::-1]
# # print(s)
# for i in s.split("."):
#     m=i[::-1]
#     a.append(m)
# print(".".join(a))
# import math
# t=int(input())
# for i in range(t):
#     n=int(input())
#     l=list(map(int,input().split()))
#     g=0
#     for k in range(0,n):
#         for j in range(0,k):
#             if(math.gcd(l[j],l[k])==math.lcm(l[j],l[k])):
#                 g+=1
#     print(g)
