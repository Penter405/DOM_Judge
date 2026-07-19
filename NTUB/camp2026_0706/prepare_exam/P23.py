def get():
    data=input()
    if data[0]=='#':
        result=[]
        for a,b in [(1,3),(3,5),(5,7)]:
            result.append(str(int(data[a:b],16)))
        return 'rgb('+','.join(result)+')'
    result=[]
    for rs in data[4:-1].split(','):
        result.append(hex(int(rs))[2:].zfill(2).upper())
    return '#'+''.join(result)
print(get())