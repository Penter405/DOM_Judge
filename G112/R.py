from collections import defaultdict
guy=int(input())
point=defaultdict(list)
pointed=defaultdict(int)
score=0
left=guy
for _ in range(guy-1):
    a,b=list(map(int,input().split()))
    point[a].append(b)
    point[b].append(a)
    pointed[a]+=1
    pointed[b]+=1

while True:
    if left<=2:
        if left==2:
            print(score*2+1)
        else:
            print(score*2)             
        break

    to_remove=[]
    score+=1
    for rs in range(1,guy+1):
        if pointed[rs]==1:
            to_remove.append(rs)
            left-=1
    for rs in to_remove:
        pointed[rs]=0
        for friend in point[rs]:
            pointed[friend]-=1
"""
5
1 2
1 3
3 4
3 5
"""

    
    