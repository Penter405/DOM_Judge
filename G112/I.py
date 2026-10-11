t=int(input())
res=[]
def get():
    u=int(input())
    d=list(map(int,input().split()))
    want=d[-1]
    d.pop(-1)
    d.sort()
    p1=0
    p2=len(d)-1
    while True:
        if p1>=p2:
            return 0
        if d[p1]+d[p2]==want:
            return 1
        elif d[p1]+d[p2]>want:
            p2-=1
            continue
        elif d[p1]+d[p2]<want:
            p1+=1
            continue


for _ in range(t):
    if get():
        res.append("YES")
    else:
        res.append("NO")





print("\n".join(res))

"""

7
7
1 2 3 4 5 6 11
5
2 7 11 15 9
11
1 2 3 4 5 6 7 8 9 10 19
8
3 16 9 20 20 15 16 29
6
1 1 5 9 12 18
5
5 1 3 6 10
9
10 20 30 1 5 2 1 7 36
"""