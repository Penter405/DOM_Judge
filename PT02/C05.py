"""
question gives us preorder and inorder traval
we can know A might be B child by preorder,
and knowing A might be in B's left or right by inorder.
"""
from collections import defaultdict
preorder_traval, inorder_traval=list(map(str,input().split()))
inorder_index=dict()
for rs in range(0,len(inorder_traval)):
    inorder_index[inorder_traval[rs]]=rs
may_have_right=[]
result=defaultdict(dict)
find=dict()
for rs in preorder_traval:
    if len(may_have_right)==0 or inorder_index[may_have_right[-1]]>inorder_index[rs]:
        #inorder_index[may_have_right[-1]]>inorder_index[rs] means last node we see have child on its left, so its inorder_index more than child
        may_have_right.append(rs)
    #cheak whose right child here
    #only 1 in may_have_right or many in
