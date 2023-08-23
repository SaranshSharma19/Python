# # Decimal to Binary 
n=int(input("Enter the value of n- "))
ans = 0
i = 0
while n!=0:
    bit = n & 1 # or n%2
    ans = (bit * pow(10,i)) + ans
    n = n>>1
    i+=1
print(ans)

# m=int(input("Enter the value of m- "))
# if m>0:
#     print(bin(m)[2:])
# else:
#     print(bin(m)[3:])


