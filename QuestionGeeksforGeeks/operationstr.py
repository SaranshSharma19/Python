s1="geeksforgeeks"
s2="geeks"
print(s2 in s1)
print(s2 not in s1)

# Cocatination
s1="geeks"
s2="forgeeks"
s3=s1+s2
s4="Welcome to " + s1+s2
print(s3)
print(s4)

# Index Method
s1="geeksforgeeks"
s2="geeks"
print(s1.index(s2)) # It will give first index value
print(s1.rindex(s2)) # It will give last index value 
print(s1.index(s2,0,13))
print(s1.index(s2,1,13))

# Part 2 String Operation
s="geeks"
print(len(s))
s1=s.upper()
print(s1)
s2=s.lower()
print(s2)
print(s1.islower())
print(s1.isupper())
print(s2.islower())
print(s2.isupper())

a="geeksforgeeks Python Course"
print(a.startswith("geeks"))
print(a.endswith("geeks"))
print(a.startswith("Python"))
print(a.endswith("Course"))
print(a.startswith("geeks",8,len(a)))

# To create a list of a string
print(a.split())
a="geeksfor,geeks,Python,Course"
print(a.split(","))

l=['geeksfor', 'geeks', 'Python', 'Course']
print(' '.join(l))
print(", ".join(l))

# Strip function
s="--geeksforgeeks--"
print(s.strip("-"))
print(s.lstrip("-"))
print(s.rstrip("-"))

# Find Function
s1="geeksforgeeks"
s2="geeks"
print(s1.find(s2))
print(s1.find("gfg"))
print(s1.find(s2,1,len(s1)))