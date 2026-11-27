for _ in range(int(input())):
    d=int(input())
    sd=str(d)
    while sd!=sd[::-1]:
        d+=int(sd[::-1])
        sd=str(d)
    print(d)