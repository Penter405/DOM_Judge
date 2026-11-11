memo=[0]
large=0
d=[]
while True:
    me=int(input())
    if me==0:
        break
    d.append(me)

large=max(d)
for index in range(1,large+1):
    memo.append(memo[index-1]+index*index)

for need in d:
    print(memo[need])