"""
1,2,3,-,-,4
"""
class tree:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

from collections import defaultdict,deque
king=None
point=dict()
radd=dict()
data=input().replace(" ","").replace("(","").strip().split(")")[:-1]
for bot in data:
    name, child,place=bot.split(',')
    if king==None:
        king=name
    if name not in point:
        point[name]=[None,None]
    if place=="L":
        point[name][0]=child
    else:
        point[name][1]=child
legal=True
leave=[]
#postorder
def dfs(node,depth=0):
    if node==None:
        return 0
    if node in point:
        l=dfs(point[node][0],depth+1)
        r=dfs(point[node][1],depth+1)
    else:
        leave.append(depth)
    return 0

dfs(king)
if max(leave)-min(leave)>1:
    print(0)
else:
    print(1)