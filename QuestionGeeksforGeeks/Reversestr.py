# Simpe Method
s=input("Enter a string: ")
rev=""
for i in s:
    rev=i+rev
print(rev)

# Using SLicing Method
s=input("Enter the string:\n")
print(s[::-1])