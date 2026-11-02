sizeof=0
from itertools import permutations
class tree:
    def __init__(self,node,tree_index,is_root=False):
        self.value=dict()#tree index:node
        if is_root:
            self.value{}
        else:
            self.value[value]=
        self.left=None
        self.right=None
res=[]
for _ in range(int(input())):
    bad_tree=0
    good_tree=0
    d=int(input())
    if d%2!=0:
        res.append(0)
        continue
    new=d//2
    sizeof=new+1
    root=tree(new+1,True)
    d=[n for n in range(1,new+1)]
    index=-1
    for nodes in (list(permutations(d))):
        index+=1
        tree_unique=0
        for node in nodes:
            see=root
            while True:
                if index not in see.value[node]:
                    see.value[node]=index
                if see.value[node][index]
        if tree_unique-bad_tree!=index:
            bad_tree+=1
        else:
            good_tree+=1
    res.append(good_tree)

for rs in res:
    print(rs)
        