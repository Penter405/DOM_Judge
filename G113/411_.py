d=input().split()
stack=[]

for rs in d:
    try:
        rs=int(rs)
        stack.append(rs)
    except:
        stack.append(eval(str(stack.pop())+rs+str(stack.pop())))

if len(stack)==0:
    print(0)
print(stack[0])