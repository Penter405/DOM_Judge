res=[]
d=list(int(input()) for _ in range(int(input())))
max_d=max(d)
memo=[1]
for _ in range(max_d-1):
    memo.append((memo[-1]+1)*2)

for rs in d:
    print(memo[rs-1])
