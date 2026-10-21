s=input()
p1=0
p2=0#will add
now=set()
size=0
res=0
while True:
    if p2>len(s)-1:
        break
    while s[p2] in now:
        if s[p1] in now:
            now.remove(s[p1])
        p1+=1
    now.add(s[p2])
    p2+=1
    res=max(res,p2-p1)

print(res)