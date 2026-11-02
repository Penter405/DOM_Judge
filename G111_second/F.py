res=[]
d=[]
want=[]
memo=[0,1,1,1]
for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    d.append(a)
    want.append(b)
for _ in range(max(d)-3):
    memo.append(sum(memo[-3:]))

for index,sizeof in zip(d,want):
    print(str(memo[index])[-sizeof:])