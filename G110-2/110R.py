from collections import defaultdict,deque
n,m=list(map(int,input().split()))
point=defaultdict(list)

for _ in range(m):
    a,b=list(map(int,input().split()))
    point[a].append(b)
base,want=list(map(int,input().split()))

went=set()

def dfs(node):
    if node in went:
        return 0
    went.add(node)
    for child in point[node]:
        dfs(child)
dfs(base)

if want in went:
    print("Yes")
else:
    print("No")