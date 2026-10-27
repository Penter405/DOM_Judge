def cheak():
    n=int(input())
    buffer=0
    for rs in str(n):
        buffer+=int(rs)
    if n%buffer==0:
        return True
    return False

if cheak():
    print(1)
else:
    print(0)