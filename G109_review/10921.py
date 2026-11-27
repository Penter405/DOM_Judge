for _ in range(int(input())):
    now=list(map(int,input().split('/')))
    past=list(map(int,input().split('/')))

    if now[1]>past[1] or (now[1]==past[1] and now[0]>past[0]):
        print(now[2]-past[2])
    else:
        print(now[2]-past[2]-1)