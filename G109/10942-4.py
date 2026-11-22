def dfs(node,value=1):#do i need return value? have i ever use it?
    #or i have only take out side memory 
    global cycle_point,in_cycle
    #normal logic
    if not point[node]:
        result[node]=1
        return 1

    #dp logic
    if visit[node]:
        return result[node]
    visit[node]=value
    if visit[point[node]] and result[point[node]]:
        result[node]=result[point[node]]+1
        return result[node]
    

    #cycle logic
    if visit[point[node]] and not result[point[node]]:
        cycle_point=point[node]
        in_cycle=True
        result[node]=value-visit[point[node]]+1
        return result[node]


    #normal logic
    if point[node]:#not 0
        dfs(point[node],value+1)
    credit=1
    if in_cycle:#it is recursion,  backing cycle by recursion call back, cheak in cycle should be under row of dfs recursion
        credit=0
    if node==cycle_point:
        in_cycle=False
    result[node]=result[point[node]]+credit
    return result[node]

for _ in range(int(input())):
    n=int(input())
    point=[0 for i in range(n+1)]
    visit=[False]*(n+1)
    be=[i for i in range(n+1)]
    result=[0]*(n+1)
    for _ in range(n):
        a,b=list(map(int,input().split()))
        point[a]=b
        be[b]=a
    cycle_point=0
    in_cycle=False
    for i in range(1,n+1):
        dfs(i)
    print(result.index(max(result)))





