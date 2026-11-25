from sys import stdin
d=stdin.read().split('\n')
for line in d:
    if line=='':
        continue
    pre, ino=line.split()
    lr={
        k:v for v,k in enumerate(ino)
    }
    point={}
    root=None
    for node in pre:
        if root==None:
            root=node
            point[root]=[None,None]
            continue
        seeing=root
        point[node]=[None,None]
        while True:
            if lr[node]<lr[seeing]:
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
    res=[]
    def dfs(n):
        for child in point[n]:
            if child:
                dfs(child)

        res.append(n)
    dfs(root)
    print(''.join(res))