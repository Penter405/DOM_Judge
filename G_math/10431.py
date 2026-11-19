result=[]
for _ in range(int(input())):
    d=int(input())
    count=0
    while d:
        count+=d%2
        d//=2
    result.append(str(count))

print("\n".join(result))