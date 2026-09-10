n=int(input())
target=input().split(',')
result=[]
for _ in range(n):
    data=input().split(',')
    got=[]
    for rs in data:
        if rs in target:
            got.append(1)
        else:
            got.append(0)
    now=got.count(1)
    r=[0]*6
    for rs in got:
        if rs==1:
            #print(now-1)
            r[now-1]+=1
        else:
            r[now]+=1
    result.append(",".join(list(map(str,r[2:]))))
print("\n".join(result))