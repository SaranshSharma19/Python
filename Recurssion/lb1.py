# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
# n = int(input())
# print(fact(n))




# def power(m):
#     if m==0:
#         return 1
#     return 2*power(m-1)

# m = int(input())
# print(power(m))




# def reachHome(src,dest,count):
#     count+=1
#     if src == dest:
#         print("Pahuch Gaya")
#         print(count)
#         return
#     reachHome(src+1,dest,count)
# dest = 10
# src = 1
# reachHome(src, dest,count=0)




# def fib(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     ans = fib(n-1) + fib(n-2)
#     return ans
# n = int(input())
# print(fib(n))




# def say(n,arr):
#     s=""
#     for i in str(n):
#         s+=arr[int(i)]+" "
#     return s
# arr = ["zero","one","two","three","four","five","six","seven","eight","nine"]
# n = int(input())
# print(say(n,arr))




# def issorted(arr,size,i=0):
#     if size==0 or size==1:
#         return True
#     if arr[0]>arr[1]:
#         return False
#     else:
#         i+=1
#         s = arr[i:]
#         ans = issorted(s,size-1)
#         return ans
# arr = [1,2,3,6,5]
# m = arr
# size = 5
# result = issorted(arr,size,0)
# if result:
#     print("Array Is Sorted")
# else:
#     print("Array Is Not Sorted")




# def sum_(arr):
#     if len(arr)==0:
#         return 0
#     if len(arr)==1:
#         return arr[0]
#     else:
#         return arr[0]+sum_(arr[1:])
# arr = [1,2,3,6,6]
# m = len(arr)
# print(sum_(arr))




# def found(arr, key):
#     if len(arr)==0:
#         return False
#     if len(arr)==1:
#         if arr[0]==key:
#             return True
#         else:
#             return False
#     if arr[0]==key:
#         return True
#     r = found(arr[1:],key)
#     return r
# k = int(input())
# n = int(input())
# list_ = list(map(int,input().strip().split()))[:n]
# print(list_)
# r = found(list_,k)
# if r:
#     print("Element in the list")
# else:
#     print("Element not in the list")




# def binarysearch(arr,s,e,key):
#     if s>e:
#         return False
#     mid = s + (e-s)//2
#     if arr[mid]==key:
#         return True
#     if arr[mid]<key:
#         return binarysearch(arr,mid+1,e,key)
#     else:
#         return binarysearch(arr,s,mid-1,key)

# arr = [2,4,6,10,14,18]
# key = int(input())
# res = binarysearch(arr,0,len(arr),key)
# if res:
#     print("element in the array")
# else:
#     print("element not in the array")

# def rev(s):
#     if len(s)==1:
#         return s
#     else:
#         r = rev(s[1:]) + str(s[0])
#     return r
# s = input()
# print(rev(s))



# def power(a,b):
#     if b==0:
#         return 1
#     if b==1:
#         return a
#     else:
#         ans = power(a,b//2)
#     if b%2==0:
#         return ans*ans
#     else:
#         return a*ans*ans
    
# a = int(input())
# b = int(input())
# print(power(a,b))



# def sortArray(arr,n):
#     if n==0 or n==1:
#         return arr
#     for i in range(n-1):
#         if arr[i]>arr[i+1]:
#             arr[i],arr[i+1]=arr[i+1],arr[i]
#     sortArray(arr,n-1)
#     return arr

# n = int(input())
# arr = list(map(int,input().strip().split()))[:n]
# print(sortArray(arr,n))


# Python program for implementation of MergeSort

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]


def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m
	L = [0] * (n1)
	R = [0] * (n2)
	for i in range(0, n1):
		L[i] = arr[l + i]
	for j in range(0, n2):
		R[j] = arr[m + 1 + j]
	i = 0
	j = 0
	k = l
	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1
def mergeSort(arr, l, r):
	if l < r:
		m = l+(r-l)//2
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is: ",arr)
mergeSort(arr, 0, n-1)
print("\n\nSorted array is: ",arr)
