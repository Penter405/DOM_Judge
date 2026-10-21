"""
def cheak():
    d=input()
    d.replace(" ","")
    d=list(map(int,d.split(",")))
    total=sum(d)
    if total%2!=0:
        return False
    target=total//2
    fetch=[True]+[False]*target
    for rs in d:
        for ind in range(len(fetch)-1,-1,-1):
            if ind-rs>=0 and fetch[ind-rs]==True:
                fetch[ind]=True
    return fetch[-1]==True

if cheak():
    print(1)
else:
    print(0)
"""
d=input()
d.replace(" ","")
d=list(map(int,d.split(",")))
d.sort()

def cheak():
    total=sum(d)
    if total%2!=0:
        return False
    target=total//2
    for a in range(len(d)):
        for b in range(len(d)):
            for c in range(len(d)):
                if a==b or b==c or a==c:
                    continue
                if d[a]+d[b]+d[c]==target:
                    return True
    return False

if cheak():
    print(1)
else:
    print(0)