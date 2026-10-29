memo=[0,1]
biggest=0
want=[]
for _ in range(int(input())):
    want.append(int(input()))
name=want.copy()
biggest=max(want)

while memo[-1]<biggest:
    memo.append(memo[-1]+memo[-2])

res=[[] for _ in range(len(want))]
for rs in memo[2:][::-1]:
    for i in range(len(res)):
        if want[i]//rs==1:
            want[i]-=rs
            res[i].append("1")
        else:
            if len(res[i])!=0:
                res[i].append("0")

for rs in range(len(res)):
    print(str(name[rs])+"="+"".join(res[rs]))

