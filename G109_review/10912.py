for _ in range(int(input())):
    d=list(input())
    new=list()
    index=-1
    ever=False
    for char in d:
        index+=1
        if char!='4':
            if ever:
                new.append('0')
        else:
            d[index]='3'
            new.append('1')
            ever=True
    print(''.join(d),''.join(new))