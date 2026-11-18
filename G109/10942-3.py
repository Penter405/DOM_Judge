from collections import deque
#1 indexed
for _ in range(int(input())):
    n=int(input())
    point=[0]*(n+1)
    be=[[0]]+[[a] for a in range(1,n+1)]
    cheaked=[False]*(n+1)
    for _ in range(n):
        a,b=list(map(int,input().split()))
        point[a]=b
        be[b].append(a)
    roots=[]
    loops=[]
    my_value=[0]*(n+1)
    for index in range(1,n+1):
        if point[index]==index:
            roots.append(index)
            my_value[index]=1
        if cheaked[index]==False:
            path=[False]*(n+1)
            seeing=index
            cheaked[index]=True
            while True:
                path[seeing]=True
                cheaked[seeing]=True
                if cheaked[point[seeing]]==True:
                    if path[point[seeing]]==True:
                        loops.append(seeing)
                    break
                seeing=point[seeing]
    in_loop=[False]*(n+1)
    for loop_point in loops:
        in_loop[loop_point]=True
        now_loop=[loop_point]
        size=1
        while in_loop[point[loop_point]]==False:
            loop_point=point[loop_point]
            now_loop.append(loop_point)
            size+=1
            in_loop[loop_point]=True
        for same in now_loop:
            my_value[same]=size
    
    que=deque([element for element in range(1,n+1) if in_loop[element]]+roots)
    while que:
        me=que.popleft()
        for parent in be[me]:
            if in_loop[parent]==False:
                in_loop[parent]=True
                my_value[parent]=my_value[me]+1
                que.append(parent)

    print(my_value.index(max(my_value)))


