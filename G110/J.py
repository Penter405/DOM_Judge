#if 235 / okay>>> fuck, else not fuck
take=[2,3,5]
result=[]
useless=input()
for num in list(map(int,input().split())):
    for rs in take:
        while num%rs==0:
            num//=rs
    result.append(str(num==1))
print("\n".join(result))