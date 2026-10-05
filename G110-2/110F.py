got=[]

useless=input()
bad=0
data=list(map(int,input().split()))
for rs in data:
    for pe in got:
        if rs<pe:
            bad+=1
    got.append(rs)

print(bad)