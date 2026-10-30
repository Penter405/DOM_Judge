res=[]
for _ in range(int(input())):
    now=0
    d=input().split()
    for rs in d:
        for pe in rs:
            if pe=="s" or pe=="S":
                now+=1
                break
    res.append(str(now))

print("\n".join(res))