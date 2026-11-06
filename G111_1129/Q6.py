res=[]
d=input().split(",")
for rs in d:
    if rs!="0":
        res.append(rs)

while len(res)!=len(d):
    res.append("0")

print(",".join(res))