amount, need_time=list(map(int,input().split()))
d=input().split()
for _ in range(need_time):
    a=zip(d[:amount//2],d[amount//2:])
    d=[]
    for b,c in a:
        d.append(b)
        d.append(c)
print(" ".join(d))