# Queue Using List
q = []
print(type(q))

# Add Element to right
q.append(10)
q.append(20)
q.append(30)
print(q)

# Pop Element from left
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))

# Size
print(len(q))

# is Empty
print(len(q)==0)

# Add Element to left
q.insert(0,10)
q.insert(0,20)
q.insert(0,30)
print(q)

# Pop Element from right
print(q.pop())
print(q.pop())
print(q.pop())

# Size
print(len(q))

# is Empty
print(len(q)==0)

