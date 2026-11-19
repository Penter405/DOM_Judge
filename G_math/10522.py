import math
for _ in range(int(input())):
    d=list(map(int,input().split(",")))
    large=1
    for a in range(len(d)):
        for b in range(a+1,len(d)):
            large=max(large,math.gcd(d[a],d[b]))
    print(large)

"""
3
10,20,30,40
125,15,25
8,12 
"""