bad=set(["a","o","y","e","u","i"])
s=input().lower()
res=[""]
for rs in s:
    if rs not in bad:
        res.append(rs)

print(".".join(res))