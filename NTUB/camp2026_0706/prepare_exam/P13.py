result=[]
for _ in range(int(input())):
    s=input()
    s2=s.split()
    if (s2[1]=="AM" and s2[0]!="12:00") or (s2[1]=="PM" and s2[0]=="12:00"):   
        result.append(s2[0])
    else:
        s2[0]=(str((int(s2[0][:2])+12)%24)).zfill(2)+s2[0][2:]
        result.append(s2[0])
        
print("\n".join(result))