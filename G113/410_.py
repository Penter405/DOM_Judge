d=input().split()
level={
    "+":1,
    "-":1,
    "*":2,
    "/":2,
    "(":3,
    ")":3
}
res=[]
stack=[]
for rs in d:
    if rs not in level:
        res.append(rs)
    else:
        if rs==")":
            while True:
                if stack[-1]=="(":
                    stack.pop()
                    break
                res.append(stack.pop(-1))
        else:
            if len(stack)!=0 and level[rs]<=level[stack[-1]] and level[stack[-1]]!=3:
                while len(stack)!=0 and stack[-1]!="(" and level[rs]<=level[stack[-1]]:
                    res.append(stack.pop())
                stack.append(rs)
            else:
                stack.append(rs)
res.extend(stack[::-1])
print(" ".join(res))

        
        

"""
a + b * d + c / d
a - b + c
a b - c +
堆疊法，
使用迴圈取出中序式的元素，
遇運算元123直接輸出，
    遇到運算子+-與左括號進行堆疊，
    堆疊中運算子優先順序若大於等於讀入的運算子優先順序，直接輸出堆疊中的運算子，再將讀入的運算子置入堆疊；
    遇右括號輸出堆疊中的運算子至左括號。ok
"""