memorize=dict()
def get(b,p,m):
    if (b,p,m) in memorize:
        return memorize[(b,p,m)]
    if p>1:
        target=p//2
        ans= get(b,p-target,m)*get(b,target,m)
    else:
        ans= b%m
    memorize[(b,p,m)]=ans
    return ans

result=[]
count=-1
while True:
    count+=1
    try:
        if count!=0:
            bot=input()
        a=int(input())
        b=int(input())
        c=int(input())
    except:
        break
    ans=0
    result.append(str(get(a,b,c)))#(a%c)**b
print("\n".join(result))
"""
10
2009
9

2
99
5

3
18132
17

17
1765
3
"""