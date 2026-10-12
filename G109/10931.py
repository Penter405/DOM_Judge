res=[]
for _ in range(int(input())):
    d=(input())
    while True:
        if d==d[::-1]:
            break
        d= str(int(d)+int(d[::-1]))

    res.append(str(d))

for rs in res:
    print(rs)