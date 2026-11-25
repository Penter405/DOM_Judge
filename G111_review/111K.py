import bisect
large=0
want=[]
for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    large=max(large,b)
    want.append((a,b))
inte=[True]*(large+1)
inte[0]=False
inte[1]=False
for n in range(2,int(large**0.5)+2):
    if inte[n]:
        for bad in range(n*n,large+1,n):
            inte[bad]=False
ever=False
for a,b in want:
    if ever:
        print()
    for ind in range(a,b+1):
        if inte[ind]:
            print(ind)
    ever=True
"""
3
1 10
3 5
1000000 1000090
"""