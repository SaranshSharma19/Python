def pivot(nums):
    i=0
    j=len(nums)-1
    mid=i+(j-i)//2
    while i<j:
        if nums[mid]>=nums[0]:
            i=mid+1
        else:
            j=mid
        mid=i+(j-i)//2
    return i
nums=[3,8,10,17,1]
m=pivot(nums)
print(m)
