def anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    
    s1=sorted(s1)
    s2=sorted(s2)
    return(s1==s2)

s1=input("Enter The string s1: ")
s2=input("Enter The string s2: ")
print(anagram(s1,s2))

#Efficient Solution
def anagrameffecient(s1,s2):
    if len(s1)!=len(s2):
        return False
    count=[0]*256
    for i in range(len(s1)):
        count[ord(s1[i])]+=1
        count[ord(s2[i])]-=1
    for x in count:
        if x!=0:
            return False
    return True

s1=input("Enter The string s1: ")
s2=input("Enter The string s2: ")
print(anagram(s1,s2))