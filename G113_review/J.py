d=[int(input())]
while d[-1]!=1:
    if d[-1]%2==0:
        d.append(d[-1]//2)
    else:
        d.append(d[-1]*3+1)
last=None
for data in d:
    if last!=None:
        print(' ',end='')
    print(data,end='')
    last=1