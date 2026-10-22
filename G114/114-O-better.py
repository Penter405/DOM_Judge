n=0
def formating(s):
    for rs in range(len(s)):
        if s[rs]!="0":
            return s[rs:]
def rever(n):
    return int(formating(str(n)[::-1]))
guy=[]
guy2=[]
get=[]
friend=[]
for _ in range(int(input())):
    want=int(input())
    n=max(n,want,rever(want))
    guy.append(want)
    guy2.append(rever(want))
    get.append(want)
    if rever(want)!=want:
        friend.append(rever(want))
    else:
        friend.append(0)


prime=[False,False]+[True]*(int(n**0.5+1)-1)
for rs in range(2,len(prime)):
    if prime[rs]:
        for bad in range(rs*2,len(prime),rs):
            prime[bad]=False
        all_1or0=True
        for i in range(len(get)):
            if get[i]==rs:
                continue
            while get[i]!=0 and get[i]%rs==0:
                get[i]//=rs
            if get[i]!=0 and get[i] !=1:
                all_1or0=False
        for i in range(len(friend)):
            if friend[i]==rs:
                continue
            while friend[i]!=0 and friend[i]%rs==0:
                friend[i]//=rs
            if friend[i]!=0 and friend[i] !=1:
                all_1or0=False
        if all_1or0:
            break

for want in range(len(get)):
    if get[want]==guy[want]:
        if friend[want]==guy2[want]:
            print(f"{guy[want]} is an emirp number.")
        else:
            print(f"{guy[want]} is a prime number.")
    else:
        print(f"{guy[want]} is not a prime number.")