cards, time=list(map(int,input().split()))
d=input().split()
new=[]
for _ in range(time):
    new.clear()
    for a,b in zip(d[:len(d)//2],d[len(d)//2:]):
        new.append(a)
        new.append(b)
    d=new.copy()
print(' '.join(d))
"""
6 1
1 2 3 4 5 6
"""