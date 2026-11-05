def solve(n):
    if n==int(n):#work
        return f"{n:.2f}"
    naga=False
    if n<0:
        naga=True
    n=abs(n)
    b=str(n).split(".")
    if len(b[1])<=2:
        return f"{n:.2f}"#work
    g=float(b[0]+"."+b[1][:2])
    if b[1][2]>="5":
        now=str(g+0.01)
        now=f"{float(now):.2f}"
        if now=="0.00":
            return "0.00"
        if naga:
            now="-"+now
        return now#work
    else:
        now=str(g)
        now=f"{float(now):.2f}"
        if now=="0.00":
            return "0.00"
        if naga:
            now="-"+now
        return now


res=[]
for _ in range(int(input())):
    res.append(solve(float(input())))

for rs in res:
    print(rs)