sizeof=int(input())
d=input().split()

def marge(n):
    if n>len(d)-1:#imposible
        return 0
    try:
        bot=int(d[n])
        return int(d[n])
    except:
        return eval(str(marge(n*2+1))+d[n]+str(marge(n*2+2)))


print(marge(0))