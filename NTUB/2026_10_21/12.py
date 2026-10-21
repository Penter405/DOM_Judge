import time
st=time.time()
n=10**6
prime=[]
good=[False,False]+[True]*n
for rs in range(n+2):
    if good[rs]:
        prime.append(rs)

        for pe in range(rs*2,n+2,rs):
            good[pe]=False

print(time.time()-st)
print("done")

d=[]
for _ in range(int(input("input"))):
    d.append(int(input()))

def part(n):
    res=[]
    for pri in prime:
        if n==1:
            return res
        while n%pri==0:
            res.append(pri)
            n//=pri
def get_sum(d):
    res=0
    for ob_int in d:
        for char in str(ob_int):
            res+=int(char)
    return res
legals=[]
def legal(n):
    if n==1:
        return False
    if good[n]:
        return False
    if get_sum(part(n))==sum(list(map(int,list(str(n))))):
        return True
    return False

for rs in range(1,10**9+1000):
    if legal(rs):
        legals.append(rs)

print(legals)
