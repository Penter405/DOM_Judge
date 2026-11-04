d=input().split(",")
res=[d[0]]
def dfs(n=0):
    ever=False
    if n*2+1<len(d) and d[n*2+1]!="null":
        ever=True
        res.append(d[n*2+1])
        dfs(n*2+1)
        res.pop()
    
    if n*2+2<len(d) and d[n*2+2]!="null":
        ever=True
        res.append(d[n*2+2])
        dfs(n*2+2)
        res.pop()
    if not ever:
        print("->".join(res))
        return 0
dfs()