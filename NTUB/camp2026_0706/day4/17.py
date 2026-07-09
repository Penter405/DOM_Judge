from collections import Counter
ele=input().split()
ele=[dict(Counter(me)) for me in ele]
result=""
for rs in sorted(ele[0].keys()):
    mins=ele[0][rs]
    for pe in ele:
        if rs not in pe:
            mins=0
            break
        if pe[rs]<mins:
            mins=pe[rs]
    result+=rs*mins
print(result)
        