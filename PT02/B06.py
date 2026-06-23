from collections import defaultdict
walk=defaultdict(list)
find={}
for _ in range(int(input())-1):
    bot=list(map(int,input().split()))
    walk[bot[0]].append(bot[1])
    find[bot[1]]=bot[0]
def get_root(node):
    while True:
        if node not in find:
            return node
        node=find[node]
root=get_root(1)
greatest=0


def get_element_in_multiple(element,multiple):
    if element>=len(multiple):
        return 0
    return multiple[element]


#from a nodes left count to its right 
def bfs(root):
    global greatest
    child_long=[]
    for rs in walk[root]:
        child_long.append(bfs(rs))
    #return your height
    #greatest is not height , its top 2 child height
    child_long.sort(reverse=True)
    greatest=max(get_element_in_multiple(0,child_long)+get_element_in_multiple(1,child_long),greatest)
    return get_element_in_multiple(0,child_long)+1
bfs(root)
print(greatest)