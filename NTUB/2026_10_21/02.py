good=0
d=list(map(int,input().split(",")))
for rs in d:
    if rs>=60:
        good+=1


if good>=5:
    print("過關")
else:
    print("卡關")