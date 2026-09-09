from collections import defaultdict
point=defaultdict(list)
king=None
datas=input().strip()
datas=datas.replace('(','')
datas=datas.replace(' ','')
datas=datas.split(')')
for data in datas:
    if data=='':
        continue
    root,l,r=data.split(',')
    root=(root)
    if king==None:
        king=root
    point[root].append(l)
    point[root].append(r)

result=[]
def dfs(node):
    global result
    if node=='-':
        return 0
    dfs(point[node][0])

    result.append(str(node))

    dfs(point[node][1])



    return 0

dfs(king)
print(','.join(result))

"""
(1,2,-)  (  2,3,-)(3,4,-) (4,5,6)  (5,-,-)  (6,-,7  ) (7,-,-)
"""