from collections import defaultdict
size,slide_size=list(map(int,input().split()))
d=list(map(int,input().split()))
appear=defaultdict(int)
left=0#to be remove
right=0#to be add
res=[]
for rs in range(size-slide_size+1):
    while right<slide_size+rs:
        appear[d[right]]+=1
        right+=1
    while left<rs:
        appear[d[left]]-=1
        left+=1
    me=float("-inf")
    for n in appear:
        if appear[n]>=1 and n>me:
            me=n
    res.append(str(me))

print(" ".join(res))

"""
8 3
1 3 -1 -3 5 3 6 7

"""
