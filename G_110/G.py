from collections import Counter
correct="".join((list(map(str,input().split()))))
result=[]
for _ in range(int(input())):
    a=0
    b=0
    user="".join((list(map(str,input().split()))))
    #print(correct,user)
    used=dict()
    for rs in range(4):
        if user[rs] in used or correct[rs] in used:
            continue
        if user[rs] ==correct[rs]:
            #print("same",correct[rs],user[rs])
            used[user[rs]]=1
            a+=1
    c_c=dict(Counter(correct))
    u_c=dict(Counter(user))
    for rs in sorted(c_c):
        if rs in u_c and rs not in used:
            b+=1
    result.append(f"{a}A{b}B")
print("\n".join(result))
            

    