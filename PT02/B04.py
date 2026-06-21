from collections import defaultdict
walk=defaultdict(list)
close=defaultdict(list)
find={}
walked=set()

#parent:child
#dfs order: self, parent, left ,right
total=int(input())
for _ in range(total-1):
    bot=list(map(int,input().split()))
    walk[bot[0]]=bot[1]
    close[bot[0]].append(bot[1])
    close[bot[1]].append(bot[0])
    find[bot[1]]=bot[0]
root=int(input())
#print(close)
for rs in range(1,total+1):
    if rs!=1:
        print(" ",end="")
    #print(close[rs],end=" ")
    print(len(close[rs]),end="")
    if rs==total:
        print("")
result=[]
def dfs(root):
    global result
    if root in walked:
        return 0
    result.append(str(root))
    walked.add(root)
    for rs in close[root]:
        dfs(rs)
dfs(root)
print(" ".join(result))