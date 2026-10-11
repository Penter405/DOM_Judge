new=[]
guy,time=list(map(int,input().split()))
d=list(map(int,input().split()))
for _ in range(time):
    for a,b in zip(d[:len(d)//2],d[len(d)//2:]):
        new.append(a)
        new.append(b)
    d=new.copy()
    new.clear()

print(" ".join(list(map(str,d))))
"""
4 5
5 9 1 6
"""