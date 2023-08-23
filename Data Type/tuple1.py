# Unpacking a Tuple
fruits=("apple","banana","kiwi")
(red , yellow , green)=fruits
print(red , yellow , green)

fruits=("apple","banana","kiwi","Watermelon","mango")
(red , yellow , *green)=fruits
print(red , yellow , green)
#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

fruits=("apple","banana","kiwi")
for x in fruits:
    print(x)

i=0
while i<len(fruits):
    print(fruits[i])
    i=i+1

for i in range(len(fruits)):
    print(fruits[i])

tuple1=("a","b","c")
tuple2=(1,2,3)
tuple3=tuple1+tuple2
print(tuple3)

fruits=tuple1*2
print(fruits)
