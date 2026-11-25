sizeof=int(input())
point=[[] for _ in range(sizeof+1)]
for _ in range(sizeof-1):
    a,b=list(map(int,input().split()))
    point[a].append(b)
    point[b].append(a)

def dfs(n,depth=0):
    global went, res
    went[n]=True
    res=max(res,depth)
    for child in point[n]:
        if not went[child]:
            dfs(child,depth+1)
result=[]
for me in range(sizeof):
    me+=1
    res=0
    went=[True]+[False]*sizeof
    
    dfs(me)
    result.append(str(res))
print(' '.join(result))
