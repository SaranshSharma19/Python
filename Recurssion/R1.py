# Print Name N time using recurssion
def name(i,n):
    if i>n:
        return 
    print("Saransh")
    name(i+1,n)

n=int(input("Enter the value of n: "))
name(1,n)

# TC - O(N)
# SC - O(N)