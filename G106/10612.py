s="IVXLCDM"
val=[1,5,10,50,100,500,1000]
worth=dict()
for rs in range(len(s)):
    worth[s[rs]]=val[rs]

res=[]
for _ in range(int(input())):
    d=input()
    last=None
    r=0
    for rs in d:
        if last!=None and last<worth[rs]:#small - big -> take away
            r-=last*2
        r+=worth[rs];last=worth[rs]
    res.append(r)
    

for rs in res:
    print(rs)
"""
8
IX
VI
XI
XVII
CCLXVIII
MMMCC
DCCVII
MMCDLXIX
"""