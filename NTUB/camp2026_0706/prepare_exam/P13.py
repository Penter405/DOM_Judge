result=[]
for _ in range(int(input())):
    s=input()
    s2=s.split()
    if s2[1]=="AM":
        result.append(s2[0])
    else:
        s2[0]=str(int(s2[0][:2])+12)+s2[0][2:]
        result.append(s2[0])
        
print("\n".join(result))