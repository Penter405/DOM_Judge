res=[]
for _ in range(int(input())):
    amount=int(input())
    ans=0   
    d=list(map(int,input().split()))
    for left in range(len(d)):
        for right in range(len(d)-1,left,-1):
            if d[right]<d[right-1]:
                ans+=1
                d[right],d[right-1]=d[right-1],d[right]
    res.append(ans)

for rs in res:
    print(f"Optimal train swapping takes {rs} swaps.")
"""
3
3
1 3 2
4
4 3 2 1
2
2 1
"""