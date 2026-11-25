n=int(input())
bilen=n+1
res=0
ran=2
for _ in range(len(bin(n)[2:])):
    res+=(bilen//ran)*(ran//2)
    res+=max(0,(bilen%ran)-(ran//2))
    ran*=2
print(res)
