res=[]
for _ in range(int(input())):
    a=input()
    b=input()
    do=set(a) & set(b)
    r=[]
    s=[]
    for rs in a:
        if rs in do:
            r.append(rs)
    for rs in b:
        if rs in do:
            s.append(rs)

    dp=[[0 for _ in range(len(s)+1)] for _ in range(len(r)+1)]
    for a in range(len(r)):
        for b in range(len(s)):
            new=0
            if r[a]==s[b]:
                new=1
            dp[a+1][b+1]=max(new+dp[a][b],dp[a+1][b],dp[a][b+1])
    res.append(dp[-1][-1])

for rs in res:
    print(rs)            
"""
2
ACCGATGCAGCGCTC
CCGATGA
abcdghxy
aedfhrz

"""