def get(a,b):
    if a>b:
        a,b=b,a
    return ord(b)-ord(a)

d=input()
res=[]
for index in range(0,len(d)-1):
    res.append(str(get(d[index],d[index+1])))

print(''.join(res))