worth={
    '+':1,
    '-':1,
    '*':2,
    '/':2,
    '(':3,
    ')':3
}
d=input().split()
stack=[]
res=[]
for char in d:
    if char in worth:
        if len(stack)==0:
            stack.append(char)
            continue
        if char==')':
            while stack:
                now=stack.pop()
                if now=='(':
                    break
                res.append(now)
            continue
        while stack and stack[-1]!='(' and worth[stack[-1]]>=worth[char]:
            res.append(stack.pop())
        stack.append(char)

    else:
        res.append(char)
res.extend(stack[::-1])
print(' '.join(res))