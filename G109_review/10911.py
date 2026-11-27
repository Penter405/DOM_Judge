for _ in range(int(input())):
    d=list(map(int,input().split()))
    d.sort(reverse=True)
    print(d[0],d[1])