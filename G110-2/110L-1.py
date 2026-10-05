result=[]

def preorder(node):
    if node==None:
        return 0
    now.append(str(node))

    preorder(point[node][0])
    preorder(point[node][1])
    return 0


for _ in range(int(input())):
    now=[]
    useless=input()
    data=list(map(int,input().split(",")))
    root=data[0]
    point=dict()
    point[root]=[None,None]
    for node in data[1:]:
        seeing=root
        point[node]=[None,None]
        while True:
            if node<seeing:
                if point[seeing][0]==None:
                    point[seeing][0]=node
                    break
                else:
                    seeing=point[seeing][0]
            else:
                if point[seeing][1]==None:
                    point[seeing][1]=node
                    break
                else:
                    seeing=point[seeing][1]
                
    preorder(root)
    result.append(" ".join(now))
print("\n".join(result))
