x=int(input())
d=dict()
big=0
order=[]
for _ in range(x):
    y=int(input())
    d[y]=None
    order.append(y)
    big=max(big,y)


"""
10k
-> 
for int 10k
    for t 20


"""
res=[0]*10
for rs in range(1,big+1):
    for good in str(rs):
        res[int(good)]+=1
    if rs in d:
        d[rs]=" ".join(list(map(str,res)))


for rs in order:
    print(d[rs])