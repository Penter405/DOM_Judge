from collections import Counter
for _ in range(int(input())):
    y,x=list(map(int,input().split()))
    d=[]
    for _ in range(y):
        d.append(input())
    res=[]
    for ind,ob in enumerate(zip(*d)):
        now=dict(Counter(ob))
        large=0
        guy=''
        for char in 'ACGT':
            if now.get(char,0)>large:
                large=now.get(char,0)
                guy=char
        res.append(guy)
    print(''.join(res))