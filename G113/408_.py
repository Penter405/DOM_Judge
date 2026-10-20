"""
a2+b2+c2=k
a<=b<=c<=254

"""
dp=dict()

for a in range(1,255):
    if a**2>50000:
        continue
    dp[a**2]=[a]
bad=[]
now=[]
for b in range(1,255):
    
    for rs in dp:
        if rs+b**2>50000:
            break
        if rs+b**2==13:
            print("found")
        now.append([rs+b**2,dp[rs].copy()+[b]])
for rs in now:
    dp[rs[0]]=rs[1]
bad=[]
now=[]
for c in range(1,255):

    for rs in dp:
        if rs+c**2>50000:
            break
        now.append([rs+c**2,dp[rs].copy()+[c]])
for rs in now:
    dp[rs[0]]=rs[1]
res=[]
for rs in range(int(input())):
    want=int(input())
    if want in dp:
        print(" ".join(list(map(str,dp[want]))))
    else:
        print(-1)

"""
4
13
15
17
67

"""