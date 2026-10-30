res=[]
for _ in range(int(input())):
    d=input().split()
    stack=[]
    
    for rs in d:
        try:
            rs=int(rs)
            stack.append(rs)
        except:
            b=stack.pop()
            a=stack.pop()
            stack.append(int(eval(str(a)+rs+str(b))))
    res.append(stack[0])


for rs in res:
    print(rs)