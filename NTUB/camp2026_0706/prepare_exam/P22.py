def do(a,b):
    result=[]
    for rs in range(len(a)):
        if a[rs]==b[rs]:
            result.append(a[rs])
        else:
            if a[rs]==0:
                result.append('1')
            result.append('0')
    return ''.join(result)

data=input().split('/')
binned=[]
result=[]
for rs in range(2):
    binned.append([])
    for pe in data[rs].split('.'):
        binned[-1].append(bin(int(pe))[2:].zfill(8))
for rs in range(4):
    result.append(str(int(do(binned[0][rs],binned[1][rs]).zfill(8),2)))
print('.'.join(result))
#192.168.10.65/255.255.255.224