"""
1,2,3,-,-,4
"""

from collections import defaultdict,deque
point=defaultdict(list)

data=input().strip().replace(' ','').split(',')

queue=deque()
queue.append(int(data[0]))


"""
n=0
2n+1
2n+2

"""





result=-1
#postorder
def dfs(node):
    global result,data
    if node>=len(data):
        return 0
    if data[node]=='-':
        return 0
    
    l=dfs(node*2+1)
    r=dfs(node*2+2)

    #print(data[node],l,r)
    result=max(result, l+r )



    return max(l,r)+1

dfs(0)
print(result)


"""
1   ,2,        5,3 ,4,6,    -  ,-,7
"""