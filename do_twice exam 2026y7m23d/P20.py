"""

data=input()
result=set()
back=0
front=0
count=None
while back<len(data) and front<len(data):
    if count==None 
    
"""
result=set()
data=list(map(int,input()))
for rs in range(len(data)+1):
    for pe in range(rs+1,len(data)+1):
        #print(data[rs:pe])
        if sum(data[rs:pe])%3==0:
            result.add(tuple(data[rs:pe]))
print(len(result))