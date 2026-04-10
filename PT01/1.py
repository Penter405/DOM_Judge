class node():
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def init():
    result=[]
    n=int(input())
    hash=dict()
    for _ in range(n):
        x,l,r=input().split(',')
        if x!='-':
            if int(x) in hash:
                xn=hash[int(x)]
                #print("is same object:",id(xn)==hash[int(x)])
            else:
                #print("new ", x)
                xn=node(int(x))
                result.append(xn)
                hash[int(x)]=xn
        if l!='-':
            #print("new",l)
            ln=node(int(l))
            xn.left=ln
            result.append(ln)
            hash[int(l)]=ln
        if r!='-':
            #print("new",r)
            rn=node(int(r))
            xn.right=rn
            result.append(rn)
            hash[int(r)]=rn
    #print("log init")
    """for rs in result:
        print(rs.value)
    """
    #print("done")
    return result[0]

root=init()
#print("the root global",root.value)
big=0
def recur(root,depth):
    global big
    if root==None:
        return 0
    #print(root.value)
    if root.left==None and root.right==None:
        #print("no child")
        if big<depth:
            big=depth
        return 0
    if root.left:
        recur(root.left,depth+1)
    if root.right:
        recur(root.right,depth+1)
recur(root,0)
print(big)
#print("result:",big)
"""
1
3
the log only two node,
"""