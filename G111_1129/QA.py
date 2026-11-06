from sys import stdin
get=stdin.read().split("\n")

for line in get:
    if line=="":
        continue
    res=0
    d=list(map(int,line.split(",")))
    for a in range(len(d)):
        for b in range(a+1,len(d)):
            if d[a]==d[b]:
                res+=1

    print(res)