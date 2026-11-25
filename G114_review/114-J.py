d=list(map(int,input().split('.')))
res=[]
for data in d:
    res.append(bin(data)[2:].zfill(8))
print(''.join(res))