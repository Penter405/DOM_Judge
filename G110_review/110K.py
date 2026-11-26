memo=dict()
def mod(a,b,m):
    global memo
    if b==1:
        return a%m
    if (a,b,m) in memo:
        return memo[(a,b,m)]
    if b & 1 ==0:
        res=mod(a,b//2,m)%m
        res=(res*res)%m
    else:
        res=((mod(a,b//2,m)%m )* mod(a,b//2+1,m)%m)%m

    memo[(a,b,m)]=res
    return res
while True:
    try:
        print(mod(int(input()),int(input()),int(input())))
        input()
    except EOFError:
        exit()
"""
10
2009
9

2
99
5

3
18132
17

17
1765
3
"""