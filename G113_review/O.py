d=input().split()
stack=[]
for char in d:
    if char in "+-*/":
        stack.append(str(eval((stack.pop())+char+(stack.pop()))))
    else:
        stack.append(char)

print(stack[0])