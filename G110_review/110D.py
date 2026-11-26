sizeof=int(input())
d=list(map(int,input().split()))
total=sum(d)
if (total&-total)&1==0:
    print(total)
else:
    pick=[n for n in d if (n&-n)&1==1]
    print(total-min(pick))