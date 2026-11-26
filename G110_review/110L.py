res=[]
def dfs(n):
    global res
    for child in point[n]:
        if child!=None:
            dfs(child)
    res.append(str(n))

for _ in range(int(input())):
    sizeof=int(input())#3 up
    d=list(map(int,input().split(',')))
    root=d[0]
    point=[[None,None] for _ in range(100)]
    for node in d[1:]:
        seeing=root
        while True:
            if node<seeing:
                if point[seeing][0]==None:
                    point[seeing][0]=node
                    break
                else:
                    seeing=point[seeing][0]
            else:
                if point[seeing][1]==None:
                    point[seeing][1]=node
                    break
                else:
                    seeing=point[seeing][1]
    res.clear();dfs(root)
    print(' '.join(res))