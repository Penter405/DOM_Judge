me=input()
ban=set(input())
res=[]
for rs in me:
    if rs not in ban:
        res.append(rs)

print("".join(res))