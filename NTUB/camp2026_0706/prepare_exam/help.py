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
print(do(bin(19),bin(240)))