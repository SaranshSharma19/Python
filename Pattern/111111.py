# importing "heapq" to implement heap queue
import heapq

# initializing list 1
li1 = [5, 6, 9, 7, 3]

# initializing list 2
li2 = [5, 7, 9, 4, 6]

# using heapify() to convert list into heap
heapq.heapify(li1)
heapq.heapify(li2)

print(li1)
# using heappushpop() to push and pop items simultaneously
# pops 2
print("The popped item using heappushpop() is : ", end="")
print(heapq.heappushpop(li1, 4))
print(li1)

# using heapreplace() to push and pop items simultaneously
# pops 3
print(li2)
print("The popped item using heapreplace() is : ", end="")
print(heapq.heapreplace(li2, 2))
print(li2)
