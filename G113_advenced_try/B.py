while True:
    try:
        d=list(map(int,input().split()))
        d=set(d)
        print(len(d))
    except:
        break