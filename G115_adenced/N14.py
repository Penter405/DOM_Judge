level={
    "+":0,
    "-":0,
    "*":1,
    "/":1,
    "(":2,
    ")":2,
}
d=input().split()
stack=[]
res=[]
for rs in d:
    if rs not in "()" and rs not in level:
        res.append(rs)
        continue

    if rs =="(":
        stack.append("(")
        continue
    if rs==")":#遇右括號輸出堆疊中的運算子至左括號
        while True:
            me=stack.pop()
            if me=="(":
                break
            res.append(me)
        continue
    if len(stack)==0 or level[rs]>=level[stack[-1]]:
        stack.append(rs)
    else:
        while True:#堆疊中運算子優先順序若大於等於讀入的運算子優先順序，直接輸出堆疊中的運算子
            if len(stack)==0 or stack[-1]=="(" or level[stack[-1]]<level[rs]:
                break
            res.append(stack.pop())
        stack.append(rs)
for rs in stack[::-1]:
    res.append(rs)
print(" ".join(res))