"""
i,.  i tree 0 to tree k-1 root
a,b,c
child parent_in tree 0 parent_in tree 1...(if parent==999, i am root)


"""
def get():
    node,trees,want=list(map(int,input().split(",")))
    tree=[[n for n in range(node)] for _ in range(trees) ]#inner=parent find
    for _ in range(node):
        d=list(map(int,input().split()))
        if d[1]==999:
            continue
        for rs in range(trees):
            tree[rs][d[0]]=d[rs+1]



    res=[]
    for rs in range(trees):
        now=0
        me=want
        while True:
            if tree[rs][me]==me:
                break
            me=tree[rs][me]
            now+=1
        res.append(str(now))
    return ",".join(res)
res=[]
for _ in range(int(input())):
    res.append(get())


for rs in res:
    print(rs)
"""
7,4,6
0 5 6 1 2
1 0 6 3 2
2 0 1 3 4
3 5 1 4 2
4 999 999 999
5 4 6 3 0
6 5 4 1 0
"""