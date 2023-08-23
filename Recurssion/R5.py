def rev(l,r,arr):
    if l>=r:
        return
    arr[l],arr[r]=arr[r],arr[l]
    rev(l+1,r-1,arr)
def main(): 
    r=int(input("Enter The value of r: "))
    arr=list(map(int,input().strip().split()))[:r]
    rev(0,r-1,arr)
    print(arr)
main()