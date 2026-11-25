legal=[]
for ind in range(255):
    legal.append(ind*ind)
#3 sum
for _ in range(int(input())):
    d=int(input())
    res=[]
    for a in range(255):
        if res:
            break
        find=d-legal[a]
        b=a
        c=len(legal)-1
        while b<=c:
            now=legal[b]+legal[c]
            if now==find:
                res=[a,b,c]
                break
            elif now>find:
                c-=1
            else:
                b+=1
    if res:
        print(*res)
    else:
        print(-1)