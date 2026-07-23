n,k=list(map(int,input().split()))
data=input()
new=[]
last=None
for rs in data:
    if last==None or rs!=last:
        new.append([])
    last=rs
    new[-1]+=rs
new2=[]
index=-1
for rs in new:
    index+=1
    if index==0 or index==len(new)-1:
        new2.append(''.join(rs))
        continue
    if rs[0]=='0':
        if rs.count('0')<k:
            new2.append('1'*len(rs))
            continue
        else:
            new2.append('0'*len(rs))
    else:
        new2.append(''.join(rs))
result=[]
last=None
for rs in ''.join(new2):
    if last==None or rs!=last:
        result.append([])
    last=rs
    result[-1]+=rs
size_of=0
counts=0
for rs in result:
    if rs[0]=='1':
        counts+=1
        if len(rs)>size_of:
            size_of=len(rs)
print(counts,size_of)