from collections import defaultdict

def get():
    wrong=[None,0,0,0]
    n,k,m=list(map(int,input().split()))
    data=input()
    last=None
    times=defaultdict(int)
    for rs in data:
        
        #cheak 1
        if last!=None and last==rs:
            wrong[1]=1
        last=rs
        times[rs]+=1
    #cheak 2
    if len(dict(times))<m:
            wrong[3]=1
    if times['X']>k:
        wrong[2]=1
    if 1 in wrong:
        bad=[]
        index=0
        for  rs in wrong[1:]:
            index+=1
            if rs==1:
                bad.append(str(index))
        return ' '.join(bad)
    return '0'
result=get()
if result=='0':
    print('VALID')
else:
    print('INVALID',result)
'''
5 0 3
ABABA
'''
