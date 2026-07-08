s=input()
result=[]
def add(x, index):
    global result
    while len(result)-1<index:
        result.append(set())
    result[index].add(x)


last=0
index=0
for rs in s:
    if last==0:
        add(rs,index)
        
    elif rs ==last:
        index+=1
        add(rs,index)
    else:
        if rs in result[index]:
            while index<=len(result)-1 and rs in result[index]:
                index+=1
        else:
            index=0
        add(rs,index)
    last=rs
index=-1
answer=""
#print(result)
for rs in result:
    index+=1
    if index%2==0:
        answer+="".join(sorted(list(rs)))
    else:
        answer+="".join(sorted(list(rs),reverse=True))
print(answer)