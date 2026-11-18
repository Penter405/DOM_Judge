best=[]
current=[]
def get(now=1):
    global n,best,current
    #require return here
    if n==now:
        if len(current)<len(best) or len(best)==0:
            best=current.copy()
        return 0
    if now>n:
        return 0
    for value in range(2,10):
        current.append(str(value))
        get(now*value)
        current.pop()

n=int(input())
get()
if len(best)==0:
    print(-1)
else:
    print(" ".join(best))