res=[]
for _ in range(int(input())):
    a=input().split()[1:]
    b=input().split()[1:]
    now=list(set(a)&set(b))
    res.append(len(now))

for rs in res:
    print(rs)