want=int(input())
res=0
now=1
for index in range(want):
    res+=now
    now*=4
print(res)