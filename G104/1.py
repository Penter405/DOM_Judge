result=[]

for _ in range(int(input())):
    useless=int(input())
    data=list(map(int,input().split(',')))
    buffer=0
    last=data[0]
    for rs in data[1:]:
        if last<rs:
            #go up
            buffer+=(rs-last)*20
        else:
            buffer+=(last-rs)*10
        last=rs
    result.append(str(buffer))

print("\n".join(result))