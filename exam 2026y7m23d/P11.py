result=[]
a,b,c=list(map(int,input().split()))
for _ in range(int(input())):
    data=list(map(int,input().split(',')))
    sc=(data[1]*a+data[2]*b+data[3]*c)/100
    if (sc-sc//1)>=0.5:
        sc=(sc//1)+1
    if 56<=sc<=59:
        result.append(f"{data[0]}: #60")
    elif sc==60:
        result.append(f"{data[0]}: &61")
    else:
        result.append(f"{data[0]}: {sc:.0f}")
#11146001: 66
print("\n".join(result))