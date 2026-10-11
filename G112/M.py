times=int(input())
res=[]
def get():
    guy, tar=list(map(int,input().split()))
    res=0
    d=list(map(int,input().split()))
    d.sort(reverse=True)
    pick=0
    for rs in d:
        pick+=1
        if pick*rs>=tar:

            res+=1
            pick=0
    return res


for _ in range(times):
    res.append(get())


for rs in res:
    print(rs)


"""
3
5 10
7 11 2 9 5
4 8
2 4 2 3
4 11
1 3 3 7
"""
"""
2
2 839020818
455326647 226571364
1 447153477
348243555
"""