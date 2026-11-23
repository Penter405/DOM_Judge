"""
O= out
L= root large
M= root min
B= binary tree
LMB
"""
now=[1,1]
traval=[]
def dfs(n=0):
    if n>=len(d):
        return 0
    left=n*2+1
    right=n*2+2
    dfs(left)
    traval.append(d[n])
    dfs(right)
    #is Large root
    if left>=len(d):
        l=float("-inf")
    else:
        l=d[left]
    if right>=len(d):
        r=float("-inf")
    else:
        r=d[right]
    if not(d[n]>l and d[n]>r):
        now[0]=0


    #is min root
    if left>=len(d):
        l=float("inf")
    if right>=len(d):
        r=float("inf")
    if not(d[n]<l and d[n]<r):
        now[1]=0
    return 0

for _ in range(int(input())):
    d=list(map(int,input().split(',')))
    now=[1,1]
    traval.clear()
    dfs()
    if now[0] or now[1]:
        print('H')
    elif traval==sorted(traval):
        print('B')
    else:
        print('F')