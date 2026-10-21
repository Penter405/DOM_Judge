def legal():
    n=int(input())
    now=2
    if n%3==0 or n%5==0:
        return False
    for rs in range(2,n):
        if n%rs==0:
            now+=1
        if now>=5:
            return True
    if now>=5:
            return True
    return False

if legal():
    print(1)
else:
    print(0)