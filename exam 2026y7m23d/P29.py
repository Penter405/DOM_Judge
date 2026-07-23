from itertools import permutations
ans="1111111111111000000000000"
n,k=list(map(int,input().split()))
data=input().split()
def get():
    for rs in permutations(data,k):
        if ''.join(rs)==ans:
            return 1
    return 0


if get()==1:
    print("YES")
else:
    print("NO")