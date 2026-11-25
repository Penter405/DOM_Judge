import bisect
fib=[1,2]
large=0
need=[]
for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    large=max(large,b)
    need.append([a,b])
while True:
    new=fib[-1]+fib[-2]
    if new>large:
        break
    fib.append(new)

for a,b in need:
    print(bisect.bisect_right(fib,b)-bisect.bisect_left(fib,a))
