sizeof,edges=list(map(int,input().split()))
prefix=list(map(int,input().split()))
todo=list()
def get(n):
    if n<0:
        return 0
    return prefix[n]
for _ in range(edges):
    a,b=list(map(int,input().split()))
    todo.append((a,b))

for rs in range(1,len(prefix)):
    prefix[rs]+=prefix[rs-1]

for a,b in todo:
    print(get(b-1)-get(a-2))