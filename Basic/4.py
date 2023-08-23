# n = int(input())
# dp = [-1]*(n+1)
# def count(n):
#     if n==1:
#         return 0
#     if n==2:
#         return 1
#     if dp[n]!=-1:
#         return dp[n]
#     dp[n] = (n-1)*(count(n-1)+count(n-2))
#     return dp[n]
# ans  = count(n)
# print(ans)
data = "100"
n = int(data,2)
print(n)