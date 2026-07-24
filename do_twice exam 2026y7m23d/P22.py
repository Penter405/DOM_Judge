"""
this is a tree question
so we are going to do is that initialize a set
cheak if the node ever go uped to parent
opss, its not tree
"""

right=[]
wrong_index=-1
result=0
for _ in range(int(input())):
    data=input().split()
    right.append((data[0],int(data[1])))
index=-1
for _ in range(int(input())):
    index+=1
    data=input().split()
    if wrong_index!=-1 or right[index][0]!=data[0] or right[index][1]!=int(data[1]):
        if wrong_index==-1:
            wrong_index=index+1
        
        result+=int(data[1])
print(wrong_index,result)