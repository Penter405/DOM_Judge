result=[]
for _ in range(int(input())):
    a,b,c,d=list(map(int,input().split(",")))
    for x in range(a+1):
        if b*x+c*(a-x)==d:
            result.append(str(x)+","+str(a-x))
            break

print("\n".join(result))
                   
