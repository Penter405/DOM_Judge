from itertools import permutations
d=input()
d=list(permutations(d))
res=set()
for rs in d:
    now=int("".join(list(rs)))
    if now%7==0 or now%11==0:
        res.add(now)

print(len(res))
