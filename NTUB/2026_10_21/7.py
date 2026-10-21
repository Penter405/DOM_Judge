want=int(input())
last=None
front=None
biggest=1001000
good=[False,False]+[True]*(biggest-2)
for n in range(biggest):
    if good[n]:
        if n>want:
            front=n
            break
        for bad in range(n+n,biggest,n):
            good[bad]=False
        if n<want:
            last=n

print(last,front)
"""
2 3 5 7 9 11 13 17 19 23 29
"""