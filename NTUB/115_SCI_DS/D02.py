Nodes={}#value: object
result={}
class queue():
    def __init__(self,value):
        self.value=value
        self.next=None
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

#its not dfs
"""
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

"""
ever=set()
depth={}
def dfs(bot,last_object):
    the_queue=queue(bot)
    last_object=the_queue
    while True:
        if the_queue==None:
            return 0
        #print("log",the_queue.value)
        if(the_queue.value not in ever):
            ever.add(the_queue.value)
            root=Nodes[the_queue.value]
            for child_object in root.child:
                if(child_object.value not in depth):
                    depth[child_object.value]=depth[root.value]+1
                last_object.next=queue(child_object.value)
                last_object=last_object.next
        the_queue=the_queue.next
        #if(the_queue!=None):
        #    print(the_queue.value)
    

def main():
    init()
    depth[sorted(Nodes)[0]]=0
    dfs((sorted(Nodes)[0]),0)
    #print(depth)
    for rs in range(1,len(Nodes)+1):
        buffer=0
        if rs in depth:
            buffer=depth[rs]
        else:
            buffer=-1
        print(rs,buffer)
main()

