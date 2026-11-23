want=[]
large=0
for _ in range(int(input())):
    d=int(input())
    want.append(d)
    if d%2!=0:
        large=max(large, d//2)
n_has=[1]
for n in range(1,large+1):
    have=0
    for a in range(n):
        have+=n_has[a]*n_has[n-a-1]
    n_has.append(have)
for rs in want:
    if rs%2==0:
        print(0)
    else:
        print(n_has[rs//2])