d=[]
for _ in range(int(input())):
    d.append(list(map(int,input().split())))

d.sort()
for a,b in d:
    print(a,b)