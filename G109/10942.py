"""
graph

time complexity= nodes dont point to any node * edges

me = 1 + best child
nodes dont point to any node = min
if point to  same , 


can run version :
for node:
    dfs()

time= node * edges!



meet loop: take all loop , or take some loop + take another line
"""
from collections import defaultdict
res=[]
def solve():
    n=int(input())
    ever_went=[False]*(n+1)
    point=defaultdict(list)
    my_best=[0]*(n+1)
    for _ in range(n):
        a,b=list(map(int,input().split()))
        point[a]=b
    

    def get_one_best(guy):
        if ever_went[guy]:
            #loop or went
            pass

        ever_went[guy]
        my_best_child=0
        for child in point[guy]:
            if not(ever_went[child]):
                get_one_best(child)
            my_best_child=max(my_best_child,my_best[child])
        my_best[guy]=my_best_child+1


        
            

    for ind in range(1,n+1):
        get_one_best(ind)

for _ in range(int(input())):
    res.append(solve())

for rs in res:
    print(rs)