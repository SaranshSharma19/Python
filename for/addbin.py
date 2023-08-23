a="1010"
b="1011"
ans=0
i=0
an=0
j=0
m=int(a)
n=int(b)
while m!=0:
    digit = m%10
    if digit == 1:
        ans += pow(2,i)
        m=m//10
        i+=1
while n!=0:
    digit = n%10
    if digit == 1:
        an += pow(2,j)
        n=n//10
        j+=1
ans+= an
print(bin(ans)[2:])