from collections import Counter
res=[]
def get_min(n):
    m=None
    for rs in n:
        if m==None or rs<m:
            m=rs
    return m
for _ in range(int(input())):
    r=[]
    dnas,dna_length=list(map(int,input().split()))
    d=[]
    for _ in range(dnas):
        d.append(list(input()))
    d=zip(*d)
    for rs in d:
        now=dict(Counter(rs))
        guy=None
        appear=None
        for char in sorted(now.keys()):
            if guy==None:
                guy=char
                appear=now[char]
            else:
                if now[char]>appear:
                    guy=char
                    appear=now[char]
                elif now[char]==appear:
                    if char<guy:
                        guy=char
        r.append(guy)
    res.append("".join(r))


print("\n".join(res))
