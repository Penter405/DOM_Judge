from collections import defaultdict
point=defaultdict(list)
king=None
for _ in range(int(input())):
    data=input().strip()
    data=data.replace(' ','')
    root,l,r=data.split(',')
    root=int(root)
    if king==None:
        king=root
    if l=='-':
        l=None
    else:
        l=int(l)
    if r=='-':
        r=None
    else:
        r=int(r)
    point[root].append(l)
    point[root].append(r)

result=-1
#postorder
def dfs(node):
    global result
    if node==None:
        return 0
    childs=[0]
    for child in point[node]:
        childs.append(dfs(child))

    result=max(result,max(childs))


    return max(childs)+1

dfs(king)
print(result)