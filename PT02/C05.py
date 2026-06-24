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
    if len(walk[parent])==0:
        walk[parent].append(node)
        return deep
    elif len(walk[parent])==1:
        if inorder_index[node]<inorder_index[parent]:
            return binary_create_tree(walk[parent][0],node,deep+1)
        else:
            walk[parent].append(node)
            return deep
    else:
        #len 2
        if inorder_index[node]<inorder_index[parent]:
            return binary_create_tree(walk[parent][0],node,deep+1)
        else:
            return binary_create_tree(walk[parent][1],node,deep+1)

    
from collections import defaultdict
result=[]
while True:
    try:
        preorder_traval, inorder_traval=list(map(str,input().split()))
    except:
        break
    walk=defaultdict(list)
    inorder_index=dict()
    root=preorder_traval[0]
    result.append([root])

    for rs in range(0,len(inorder_traval)):
        inorder_index[inorder_traval[rs]]=rs
    
    for rs in preorder_traval[1:]:
        add_element_to_result_with_index(rs,binary_create_tree(root,rs))

for rs in result:
    for pe in rs:
        print("".join(pe),end="")
    print()