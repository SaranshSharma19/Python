n=int(input())
ans=0
while n!=0:
    rem=n%10
    ans = ans*10 + rem
    n=n//10
print(ans)
