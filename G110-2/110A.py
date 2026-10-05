result=[]

while True:
    try:
        a,b=input().split()
        result.append(str(int(a)*4+int(b)*6))
    except:
        break

print("\n".join(result))
