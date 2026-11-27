
d='00001'
left=0
right=len(d)-1
while left<=right:
    mid=(left+right)//2
    if d[mid]=='1':
        last_legal=mid
        right=mid-1
    else:
        left=mid+1
print(left)