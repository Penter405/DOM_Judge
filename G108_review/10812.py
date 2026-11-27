for _ in range(int(input())):
    res=0
    d=input().split()
    ind=0
    first=True
    gamed=0
    while True:
        if d[ind]=='X':
            res+=10
            if d[ind+1]=='X':
                res+=10
                if d[ind+2]=='X':
                    res+=10
                else:
                    res+=int(d[ind+2])
            elif d[ind+2]=='/':
                res+=10
            else:
                res+=int(d[ind+1])+int(d[ind+2])
            ind+=1
        else:
            if d[ind+1]=='/':
                res+=10
                if d[ind+2]=='X':
                    res+=10
                else:
                    res+=int(d[ind+2])
                ind+=2
            else:
                res+=int(d[ind])+int(d[ind+1])
                ind+=2
        gamed+=1
        if gamed==10:
            break
    print(res)
"""
1
6 3 9 / X 8 0 X X 5 2 7 / 9 / X 3 4
"""