d=input().split(".")
res=[]
for rs in d:
    res.append(bin(int(rs))[2:].zfill(8))

print("".join(res))