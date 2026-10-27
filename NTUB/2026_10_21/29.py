#2n+1 2n+2
d=list(map(int,input().split()))
for rs in range(len(d)):
    if rs*2+2<=len(d)-1:
        print(f"{d[rs]}:({d[rs*2+1]},{d[rs*2+2]})")