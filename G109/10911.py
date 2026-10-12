n=int(input())
def get():
    d=list(map(int,input().split()))
    res=[]
    res.append(str(max(d)))
    d.remove(max(d))
    res.append(str(max(d)))
    return res


res=[]
for _ in range(n):
    res.append(" ".join(get()))


for rs in res:
    print(rs)