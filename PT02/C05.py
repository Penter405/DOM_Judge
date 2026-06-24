"""
question gives us preorder and inorder traval
we can know A might be B child by preorder,
and knowing A might be in B's left or right by inorder.
"""
"""
from collections import defaultdict
preorder_traval, inorder_traval=list(map(str,input().split()))
inorder_index=dict()
for rs in range(0,len(inorder_traval)):
    inorder_index[inorder_traval[rs]]=rs
may_have_right=[]
result=defaultdict(list)
removed_height=0
find=dict()
for rs in preorder_traval:
    if len(may_have_right)==0 or inorder_index[may_have_right[-1]]>inorder_index[rs]:
        #inorder_index[may_have_right[-1]]>inorder_index[rs] means last node we see have child on its left, so its inorder_index more than child
        may_have_right.append(rs)
        result[len(may_have_right)-1+removed_height].append(rs)
    #cheak whose right child here
    elif len(may_have_right)==1:
        #inorder_index[may_have_right[-1]]<inorder_index[rs]
        may_have_right[0]=rs
        removed_height+=1
        result[len(may_have_right)-1+removed_height].append(rs)
    else:
        #at least two may_have_right


    #only 1 in may_have_right or many in


#output
"""
def add_element_to_result_with_index(element:str,index:int):
    if len(result[-1])<=index:
        result[-1].append([])
    result[-1][index].append(element)


def binary_create_tree(parent:str,node:str,deep=1):
    if parent not in walk:
        walk[parent]=[""]*2
    if inorder_index[node]<inorder_index[parent]:
        if parent[0]=="":
            walk[parent][0]=node
            return deep
        else:
            return binary_create_tree(walk[parent][0],deep+1)
    elif inorder_index[node]<inorder_index[parent]:
        if parent[1]=="":
            walk[parent][1]=node
            return deep
        else:
            return binary_create_tree(walk[parent][1],deep+1)
    
    

result=[]
while True:
    try:
        preorder_traval, inorder_traval=list(map(str,input().split()))
    except EOFError:
        break
    walk=dict()
    inorder_index=dict()
    root=preorder_traval[0]
    result.append([root])

    for rs in range(0,len(inorder_traval)):
        inorder_index[inorder_traval[rs]]=rs
    
    for rs in preorder_traval[1:]:
        add_element_to_result_with_index(rs,binary_create_tree(root,rs))

for rs in result:
    bot=0
    for pe in rs:
        bot+=1
        if bot==len(rs):
            print("".join(pe))
        else:
            print("".join(pe),end="")