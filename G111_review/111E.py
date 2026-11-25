while True:
    d=input()
    if d=='0':
        break
    target, string=d.split()
    target=len(string)//int(target)
    new=[]
    for ind in range(0,len(string),target):
        new.append(string[ind:ind+target][::-1])
    print(''.join(new))