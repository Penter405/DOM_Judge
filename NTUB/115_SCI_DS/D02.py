Nodes={}#value: object
result={}
class Tree():
    def __init__(self,value):
        self.value=value
        self.child=[]

def init():
    for _ in range(int(input())):
        buffer=list(map(int,input().split()))
        if(buffer[0] not in Nodes):
            Nodes[buffer[0]]=Tree(buffer[0])
        for rs in range(buffer[1]):
            if(buffer[2+rs] not in Nodes):
                Nodes[buffer[2+rs]]=Tree(buffer[2+rs])
            Nodes[buffer[0]].child.append(Nodes[buffer[2+rs]])

def dfs(root,depth):
    if(root.value in result):
        #print("return 0")
        return 0
    if(root==None):
        return 0
    if(root not in result):
        result[root.value]=depth
    for rs in root.child:
        dfs(rs,depth+1)

def main():
    init()
    dfs(Nodes[sorted(Nodes)[0]],0)
    #print(result)
    for rs in range(1,len(Nodes)+1):
        buffer=0
        if rs in result:
            buffer=result[rs]
        else:
            buffer=-1
        print(rs,buffer)
main()

