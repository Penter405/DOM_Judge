d=list(map(int,input().split(",")))
res=0
appeared=set()
past=[d[0]]
while False:
    for a in range(len(d)):
        for b in range(a+1,len(d)):
            if d[a]>d[b]:
                res.add((a,b))
                #oh shit, we uses index based, and it is correct


for a in range(1,len(d)):
    #we are finding min value of unique and more value
    #finding min value -> near left
    #more value-> when euqal we need to put left on right of middle
    #right pointer==more value
    #left pointer==min value
    """
    1,2,3,4,5,6
        t g
        m
    """
    left=0
    right=len(past)-1
    while left<=right:
        mid=(left+right+1)//2
        if past[mid]>d[a]:
            right=mid-1
        elif past[mid]<d[a]:
            left=mid+1
        else:
            #when equal
            left=mid+1

    for used in past[left:]:
        res+=1
        
    
    appeared.add(d[a])
    past.append(d[a])
    past.sort()

print(res)
