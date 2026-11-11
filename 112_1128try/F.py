#1+2+3+4...I>=n  -> return I
#(k+1)*k=2n   -> require euation  -> ((8n+1)**0.5-1)/2
#k=(2n/k)-1
#k2+k =2n
from sys import stdin
d=stdin.read().split("\n")[:-1]
for line in d:
    n=int(line)
    k=int(((n*8+1)**0.5)//2)
    if k*(k+1)//2<n:
        k+=1
    print(k)