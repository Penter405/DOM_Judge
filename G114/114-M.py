fib=[1,2]
"""
binary search
left out
right out
b-a+1
"""
while True:
    now=fib[-1]+fib[-2]
    if now>10**100:
        break
    fib.append(now)


def left_search(n):#search left in
    left=0
    right=len(fib)-1
    while left<=right:
        mid=(left+right)//2
        if fib[mid]>n:
            right=mid-1
        elif fib[mid]<n:
            #seeing smaller
            left=mid+1
        else:
            #seeing same
            right=mid-1
    return left
def right_search(n):#search right in
    left=0
    right=len(fib)-1
    while left<=right:
        mid=(left+right+1)//2
        if fib[mid]>n:
            right=mid-1
        elif fib[mid]<n:
            #seeing smaller
            left=mid+1
        else:
            #seeing same
            left=mid+1
    return right
res=[]
for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    r=right_search(b)
    l=left_search(a)
    res.append(str(r-l+1))

print("\n".join(res))