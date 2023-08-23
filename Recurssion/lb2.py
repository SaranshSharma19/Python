# def partition(arr,s,e):
#     pivot = arr[s]
#     count = 0
#     for i in range(s+1,e+1):
#         if arr[i]<=pivot:
#             count+=1
#     pivotindex = count + s
#     arr[s],arr[pivotindex]=arr[pivotindex],arr[s]
#     i = s
#     j = e
#     while i<pivotindex and j>pivotindex:
#         while arr[i]<pivot:
#             i+=1
#         while arr[j]>pivot:
#             j-=1
#         if i<pivotindex and j>pivotindex:
#             arr[i],arr[j]=arr[j],arr[i]
#             i+=1
#             j-=1
#     return pivotindex

# def quickSort(arr,s,e):
#     if s>=e:
#         return
#     p = partition(arr,s,e)
#     quickSort(arr,s,p-1)
#     quickSort(arr,p+1,e)

# n= int(input())
# arr = list(map(int,input().strip().split()))[:n]
# print("Unsorted Array: ", arr)
# quickSort(arr,0,n-1)
# print("sorted Array: ", arr)

