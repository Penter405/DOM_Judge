from collections import Counter
res=[]
for _ in range(int(input())):
    d=list(map(int,input().split()))
    d.sort()
    only=[(n-1)%13 for n in d]
    only.sort()
    color=(d[0]-1)//13
    last=d[0]
    continuous=1
    have_a=(d[0]-1)%13==0
    for rs in d[1:]:
        if (rs-1)%13==0:
            have_a=True
        if (rs-1)//13!=color:
            continuous=1
            color=(rs-1)//13
        elif last+1!=rs:
            continuous=1
        else:
            continuous+=1
        last=rs
        if continuous>=5 or ( continuous==4 and have_a and (last-1)%13==12):
            break
    if continuous>=5 or ( continuous==4 and have_a and  (last-1)%13==12):
        res.append(str(7))
        continue

    see=Counter(only)
    if 6>see.most_common(1)[0][1]>=4:
        res.append("6")
        continue
    if len(see.most_common())>=2 and see.most_common()[0][1]>=3 and see.most_common()[1][1]>=2:
        res.append("5")
        continue
    
    continuous=1
    last=only[0]
    have_a=(only[0])%13==0
    for rs in only[1:]:
        now= rs
        if now==0:
            have_a=True
        if now-1!=last:
            continuous=1
        else:
            continuous+=1
        last=now
        if continuous>=5 or (continuous==4 and last==12 and have_a):
            break
    if continuous>=5 or (continuous==4 and last==12 and have_a):
        res.append("4")
        continue
        

    if see.most_common()[0][1]>=3:
        res.append("3")
        continue
    if len(see.most_common())>=2 and see.most_common()[0][1]>=2 and see.most_common()[1][1]>=2:
        res.append("2")
        continue
    if see.most_common()[0][1]>=2:
        res.append("1")
        continue
    res.append("0")

for rs in res:
    print(rs)