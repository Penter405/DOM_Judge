nodes=int(input())
point=[[] for _ in range(nodes+1)]
be=[0]*(nodes+1)
for _ in range(nodes-1):
    a,b=list(map(int,input().split()))
    point[a].append(b)
    point[b].append(a)
    be[a]+=1
    be[b]+=1
size=[0]*(nodes+1)
left=nodes
global_res=None
while True:
    imdie=[]
    for index in range(len(be)):
        if be[index]==1:
            left-=1
            imdie.append(index)
            be[index]=-1
            best=-1
            for friend in point[index]:
                if be[friend]==-1:
                    best=max(best,size[friend])
            size[index]=best+1
    for me in imdie:
        for friend in point[me]:
            if be[friend]>0:
                be[friend]-=1
    if left<=2:
        if left==1:
            for index in range(1,len(be)):
                if be[index]!=-1:
                    king=index
            if len(point[king])==0:
                global_res=0
                break
            if len(point[king])==1:
                global_res=size[point[king][0]]+1
                break
            tops=[size[child] for child in point[king]]
            tops.sort(reverse=True)
            global_res=tops[0]+tops[1]+2

        else:
            good2=[]
            for index in range(1,len(be)):
                if be[index]!=-1:
                    good2.append(index)
            res2=[]
            for king in good2:
                if len(point[king])==1:
                    res2.append(0)
                    break
                tops=[size[child] for child in point[king]]
                tops.sort(reverse=True)#only who become 0 has size
                res2.append(tops[0]+1)
            global_res=sum(res2)+1
        break
print(global_res)
"""
5
1 2
1 3
3 4
3 5
"""
"""
12
7 6
7 8
8 10
8 9
6 5
5 4
5 3
3 2
2 1
10 11
1 12
"""