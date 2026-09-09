from collections import defaultdict,deque
point=defaultdict(list)
king=None
for _ in range(int(input())):
    data=input().strip()
    data=data.replace(' ','')
    root,l,r=data.split(',')
    if king==None:
        king=root
    if l=='-':
        l=None
    if r=='-':
        r=None
    point[root].append(r)
    point[root].append(l)

result=[]
queue=deque()
queue.append(king)
#postorder
def bfs():
    global result,queue
    while queue:
        node=queue.popleft()
        if node==None:
            continue
        result.append(node)
        for child in point[node]:
            queue.append(child)
bfs()
print(','.join(result))

"""
7
1,2,5
2,3  ,   4
3,-,-
4      ,7,-
5,6,-
6, -,-
7,-,-

"""