from collections import Counter
amount=int(input())
d=Counter(list(map(int,input().split())))
res=[]
have=0
for name,had in dict(d).items():
    if had>have:
        have=had
        res=[str(name)]
    elif had==have:
        res.append(str(name))

print(" ".join(sorted(res)))