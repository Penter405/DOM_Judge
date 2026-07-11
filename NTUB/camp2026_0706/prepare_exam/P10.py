s=input()
ever=set()
sizeof=0
result=0
for rs in s:
    if rs in ever:
        ever=set()
        sizeof=0
    ever.add(rs)
    sizeof+=1
    if sizeof>result:
        result=sizeof
print(result)