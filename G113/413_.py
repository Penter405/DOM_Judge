from collections import defaultdict
data_size, interval_size=list(map(int,input().split()))
nums=list(map(int,input().split()))
d=[[] for _ in range(data_size)]
want=[]
res=dict()
for _ in range(interval_size):
    a,b=list(map(int,input().split()))
    a-=1
    b-=1
    d[a].append(b)
    want.append((a,b))
new=[]
for rs in range(len(d)):
    if rs%2==0:
        new.append(sorted(d[rs]))
    else:
        new.append(sorted(d[rs],reverse=True))
d=new

appear=defaultdict(int)
amount=set()

p1=0
p2=0
amount.add(nums[0])
appear[nums[0]]=1
for a in range(len(d)):
    while p1!=a:
        if p1<a:
            appear[nums[p1]]-=1
            if appear[nums[p1]]==0:
                amount.remove(nums[p1])
            p1+=1
    for b in d[a]:
        #move pointers to a,b
        while p2!=b:
            if p2<b:
                p2+=1
                appear[nums[p2]]+=1
                if appear[nums[p2]]>0:
                    amount.add(nums[p2])
            else:
                appear[nums[p2]]-=1
                if appear[nums[p2]]==0:
                    amount.remove(nums[p2])
                p2-=1
        res[(a,b)]=len(amount)

for rs in want:
    print(res[rs])

"""
for rs in range(len(d)):
    p1+=1
    if len(d[p1])==0:
        if appear[nums[p1]]!=0:
            appear[nums[p1]]-=1
            amount.remove(nums[p1])
            continue
    if nums[p1] in amount and appear[nums[p1]]!=0:
        appear[nums[p1]]-=1
        amount.remove(nums[p1])
    di=0
    if p2==
"""
