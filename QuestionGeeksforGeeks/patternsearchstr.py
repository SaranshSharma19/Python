txt=input("Enter the Text: ")
pat=input("Enter the pat: ")
pos=txt.find(pat)
while pos>=0:
    print(pos)
    pos=txt.find(pos,pos+1)
    break