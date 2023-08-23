# Queue using dequeue
from collections import deque
q = deque()
print(type(q))

# Insert Element to right
q.append(10)
q.append(20)
q.append(30)
print(q)

# deleting ELement from left
print(q.popleft())
print(q.popleft())
print(q.popleft())

# Size
print(len(q))

# Is Empty
print(len(q)==0)


# Insert Element to left
q.appendleft(10)
q.appendleft(20)
q.appendleft(30)
print(q)

# deleting ELement from right
print(q.pop())
print(q.pop())
print(q.pop())

# Size
print(len(q))

# Is Empty
print(len(q)==0)