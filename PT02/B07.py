from collections import defaultdict
def get_element_in_multiple(element,multiple):
    if element>=len(multiple):
        return 0
    return multiple[element]
def find_root(node):
    global find
    while True:
        if node not in find:
            return node
        node=find[node]

def bfs(root):
    global greatest, not_found
    child_long=[]
    for rs in walk[root]:
        child_long.append(bfs(rs))
    #return your height
    #greatest is not height , its top 2 child height
    child_long.sort(reverse=True)
    greatest=max(get_element_in_multiple(0,child_long)+get_element_in_multiple(1,child_long),greatest)
    try:
        not_found.remove(root)
    except:
        pass#we have already remove it,thats okay
    return get_element_in_multiple(0,child_long)+1
how_many_tree=0
greatest=0
walk=defaultdict(list)
find={}
bot=list(map(int,input().split()))
not_found=set(range(1,bot[0]+1))
for _ in range(bot[1]):
    buffer=list(map(int,input().split()))
    walk[buffer[0]].append(buffer[1])
    find[buffer[1]]=buffer[0]


while not_found:
    node=not_found.pop()
    root=find_root(node)
    how_many_tree+=1
    bfs(root)
print(how_many_tree,greatest)