def to_good(x):
    if x<0:
        return -x
    return x
def cheak():
    sizeof=int(input())
    data=list(map(int,input().split()))
    if data[0]!=data[-1]:
        return "NO"
    for rs in range(len(data)-1):
        if to_good(data[rs]-data[rs+1])>1:
            return "NO"
    return "YES"
print(cheak())
