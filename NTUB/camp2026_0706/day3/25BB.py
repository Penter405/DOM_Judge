s=list(input())
s2=""
time=-1
while s:
    time+=1
    ans=[]
    ever=set()
    to_pop=[]
    for rs in range(len(s)):
        if s[rs] in ever:
            continue
        ever.add(s[rs])
        ans.append(s[rs])
        to_pop.append(rs)
    for rs in range(len(to_pop)-1,-1,-1):
        s.pop(to_pop[rs])
    if time%2==0:
        s2+="".join(sorted(ans))
    else:
        s2+="".join(sorted(ans,reverse=True))
print(s2)