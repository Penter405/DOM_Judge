from itertools import combinations
n,w=list(map(int,input().split()))
data=list(map(int,input().split()))
result=0
for pe in range(1,n+1):
    for rs in combinations(data,pe):
        if result<sum(rs)<=w:
            result=sum(rs)
print(result)