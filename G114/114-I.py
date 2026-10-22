def length(a,b):
    if a<=b:
        return ord(b)-ord(a)
    else:
        return ord(a)-ord(b)
    
        
s=input()
res=[]
for rs in range(len(s)-1):
    res.append(str(length(s[rs],s[rs+1])))
#abcdefghijklmnop
#print(res)
print("".join(res))