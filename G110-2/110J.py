result=[]

def is_good(a):
    #only 235
    while True:
        if a%2!=0:
            break
        a//=2
    while True:
        if a%3!=0:
            break
        a//=3
    while True:
        if a%5!=0:
            break
        a//=5
    if a==1:
        return True
    return False

useless=input()

data=list(map(int,input().split()))
for rs in data:
    result.append(str(is_good(rs)))

print("\n".join(result))