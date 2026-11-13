want , have =input().split()
want=set(want)
res=0
for data in have:
    if data in want:
        res+=1

print(res)