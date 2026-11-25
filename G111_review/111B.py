from sys import stdin
d=list(map(int,[bot for bot in stdin.read().split('\n') if bot!=""]))
large=max(d)
have=[0]*(large+1)
for n in range(2,large+1):
    if have[n]==0:
        for im in range(n,large+1,n):
            have[im]+=1

for line in d:
    if line!=0:
        print("{} : {}".format(line,have[line]))