sizeof=int(input())
for d in map(int,input().split()):
    while d%2==0:
        d//=2

    while d%3==0:
        d//=3

    while d%5==0:
        d//=5

    print(d==1)