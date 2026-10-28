from collections import Counter
correct="".join((list(map(str,input().split()))))
result=[]
for _ in range(int(input())):
    new_c=""
    new_u=""
    a=0
    b=0
    user="".join((list(map(str,input().split()))))
    #print(correct,user)
    used=dict()
    for rs in range(4):
        if user[rs] ==correct[rs]:
            #print("same",correct[rs],user[rs])
            a+=1
        else:
            new_c+=correct[rs]
            new_u+=user[rs]
    c_c=dict(Counter(new_c))
    u_c=dict(Counter(new_u))
    for rs in sorted(c_c):
        if rs in u_c:
            b+=min(c_c[rs],u_c[rs])
    result.append(f"{a}A{b}B")
print("\n".join(result))
            

    