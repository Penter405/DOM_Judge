import bisect
want=[]
large=0
while True:
    a,b=list(map(int,input().split()))
    if a==0 and b==0:
        break
    large=max(large,b)
    want.append((a,b))
fibo=[1,2]
while fibo[-1]<large:
    fibo.append(fibo[-1]+fibo[-2])



for a,b in want:
    print(bisect.bisect_right(fibo,b)-bisect.bisect_left(fibo,a))
