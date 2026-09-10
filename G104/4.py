import math
result=[]
for _ in range(int(input())):
    data=input().strip().replace(" ","")
    data=data.split(",")
    buffer=int(data[0])
    for rs in data[1:]:
        buffer=math.gcd(buffer,int(rs))
    result.append(str(buffer))

print("\n".join(result))