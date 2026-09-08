class tree:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def get():
    data=list(map(int,input().split(',')))
    root=tree(data[0])
    def build(dad,me):
        if dad.value==me:
            return 0
        while True:
            if me>dad.value:
                if dad.right==None:
                    dad.right=tree(me)
                    return 0
                dad=dad.right
            else:
                if dad.left==None:
                    dad.left=tree(me)
                    return 0
                dad=dad.left
    for rs in data:
        build(root,rs)
    #postorder
    result=[]
    def dfs(node):
        if node==None:
            return 0
        dfs(node.left)
        dfs(node.right)

        result.append(str(node.value))

        return 0
    dfs(root)
    return result

result=[]
for _ in range(int(input())):
    useless=input()
    result.append(get())

for rs in result:
    print(','.join(rs))