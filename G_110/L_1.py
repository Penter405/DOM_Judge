result=[]
buffer=0
class Tree():
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def preorder(root):
    global result
    if not root:
        return 0
    result[-1].append(str(root.value))
    preorder(root.left)
    preorder(root.right)

def search_your_parent(exroot,root,me):
    global buffer
    #print("log",exroot,root)
    if root==None:
        buffer=exroot
        return exroot
    if me>=root.value:
        search_your_parent(root,root.right,me)
    elif me<root.value:
        search_your_parent(root,root.left,me)

def make_tree():
    global result, buffer
    nodes=list(map(int,input().split(',')))
    root=Tree(nodes[0])
    #print(root)
    for rs in nodes[1:]:
        search_your_parent(root,root,rs)#pretend object is pass by object
        bot=buffer
        buffer=0
        if rs>bot.value:
            bot.right=Tree(rs)
        else:
            bot.left=Tree(rs)
    return root

def main():
    global result , buffer
    for _ in range(int(input())):
        useless=input()
        root=make_tree()
        result.append([])
        preorder(root)
    for rs in result:
        print(' '.join(rs))
main()
        