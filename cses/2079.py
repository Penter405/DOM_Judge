from collections import defaultdict
nodes=int(input())#1 indexed
point=defaultdict(list)
went=[True]+[False]*(nodes)
my_value=[0]*(nodes+1)
good=None
def go_down(n):
    if went[n]:
        return 0
    went[n]=True

    value=1
    for child in point[n]:
        value+=go_down(child)

    my_value[n]=value
    return value
went2=[True]+[False]*(nodes)
def dfs(n):
    global good
    if went2[n]:
        return 0
    went2[n]=True

    for child in point[n]:
        if my_value[child]>=good and not went2[child]:
            return dfs(child)
    return n




for _ in range(nodes-1):
    a,b=list(map(int,input().split()))
    point[a].append(b)
    point[b].append(a)
    
good=go_down(1)/2
print(dfs(1))