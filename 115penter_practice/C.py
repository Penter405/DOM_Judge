def can(sizeof):
    global d,tlimit
    used=0
    ind=0
    while True:
        used+=1
        now=0
        while ind<len(d) and now+d[ind]<=sizeof:
            now+=d[ind]
            ind+=1
            
        if ind==len(d):
            return True
        if used==tlimit:
            return False

ds,tlimit=list(map(int,input().split()))#miss c as input
d=list(map(int,input().split()))
left=min(d)
right=sum(d)
while left<=right:
    mid=(left+right)//2
    if can(mid):
        right=mid-1
    else:
        left=mid+1
print(left)
