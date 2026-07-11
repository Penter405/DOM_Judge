result=[]
while True:
    s=input()
    if s=="END":
        break
    s=s.split()
    if len(s)==2:
        result.pop(int(s[1]))
    else:
        if int(s[2])>len(result)-1:
            result.append(s[1])
        else:
            result.insert(int(s[2]),s[1])
print("".join(result))