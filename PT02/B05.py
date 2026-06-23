from collections import defaultdict
walk=defaultdict(list)
result={}
for _ in range(int(input())):
    bot=input().split()
    walk[bot[0]].append(bot[1])

def bfs(root):
    my_child=0
    for rs in walk[root]:
        my_child+=bfs(rs)
    result[root]=my_child
    return my_child+1
bfs("A")
for rs in sorted(result):
    print(rs,result[rs])
