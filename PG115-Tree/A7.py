
from collections import defaultdict
datas=input().strip().replace(" ","").split(';')
point=defaultdict(list)
for data in datas:
    node,l,r=data.split(',')
    if l!='-':
        point[node].append(l)
        point[l].append(node)
    if r!='-':
        point[node].append(r)
        point[r].append(node)

want,me=input().split(',')
result=0
went=set()
def dfs(node,leng=0):
    global result,want,went
    if result!=0:
        return 0
    if node==None or node == '-':
        return 0
    if node in went:
        return 0
    went.add(node)
    if node ==want:
        result=leng

    for neighbor in point[node]:
        dfs(neighbor,leng+1)
    return 0

dfs(me)

print(result)