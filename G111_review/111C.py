for _ in range(int(input())):
    intb=[]
    d=input()
    res=[]
    c=None
    for char in d:
        if 'A'<=char<='Z':
            if c:
                res.append(c*int(''.join(intb)))
                intb.clear()
            c=char
        else:
            intb.append(char)
    res.append(c*int(''.join(intb)))
    print("".join(res))
