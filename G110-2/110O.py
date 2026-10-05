"""
dp[(a,b)]=self connect dp a-1 b  , dp a, b-1  OR dp a-1 b-1

"""

a=input()
b=input()
c=input()

appeared=set(a) & set(b) & set(c)
a=[rs for rs in a if rs in appeared]
b=[rs for rs in b if rs in appeared]
c=[rs for rs in c if rs in appeared]
dp=dict()

"""def get(a,b,c):
    if a<0 or b<0 or c<0:
        return 0
    return dp[(a,b,c)]
"""
for a1 in range(len(a)):
    for b1 in range(len(b)):
        for c1 in range(len(c)):
            ya=0
            if a[a1]==b[b1] and a[a1]==c[c1]:
                ya=1
            dp[(a1,b1,c1)]=max(dp.get((a1-1,b1-1,c1-1),0)+ya ,dp.get((a1-1,b1,c1),0) , dp.get((a1,b1-1,c1),0),  dp.get((a1,b1,c1-1),0))


print(dp[(len(a)-1,len(b)-1,len(c)-1)])