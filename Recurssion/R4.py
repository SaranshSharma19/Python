# Sum of first N numbers
def sumi(i,sum):
    if i<1:
        print(sum)
        return
    sumi(i-1,sum+i)
n=int(input("Enter The value of n: "))
sumi(n,0)


def sumi(n):
    if n==0:
        return 0
    return n + sumi(n-1)

n=int(input("Enter The value of n: "))
print(sumi(n))

def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)

n=int(input("Enter The value of n: "))
print(fact(n))