a,b=list(map(int,input().split()))
out=[[0 for _ in range(a)] for _ in range(b)]
for rs in range(a):
    bot=input().split()
    for pe in range(b):
        out[pe][rs]=bot[pe]
for rs in out:
    print(" ".join(rs))

"""
3 2
1 2
3 4
5 6

"""