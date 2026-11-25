spe=set("[ ! @ # $ ^ & * ( ) , . ? ” : { } | < > ]".split())
good=[0,0,0,0]
d=input()
for char in d:
    if '0'<=char<='9':
        good[0]=1
    elif 'A'<=char<='Z':
        good[1]=1
    elif 'a'<=char<='z':
        good[2]=1
    elif char in spe:
        good[3]=1



res=good.count(1)
if len(d)>=8:
    print(res+1)
else:
    print(res)