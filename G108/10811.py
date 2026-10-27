res=[]
for _ in range(int(input())):
    ans=0
    d=input()
    now=1
    for rs in d:
        if rs=="O":
            ans+=now
            now+=1
        else:
            now=1
    res.append(str(ans))

print("\n".join(res))