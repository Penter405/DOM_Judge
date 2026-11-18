from sys import stdin
def new(char,index):
    if index%2!=0:
        index=26-index
    if "A"<=char<="Z":
        value=ord(char)
        return chr(((value-65+index)%26)+65)
    elif "a"<=char<="z":
        value=ord(char)
        return chr((value-97+index)%26+97)
    else:
        return char
res=[]
now=0
diff=None
is_int=False
for line in stdin.read().split("\n"):
    if line=="":
        continue
    try:
        line=int(line)
        if diff==None:
            diff=line
        else:
            now=line
        res.append(str(line))
    except:
        buffer=[]
        if now==1:
            use=diff
        else:
            use=-diff
        for d in line:
            buffer.append(new(d,use))
        res.append("".join(buffer))
print("\n".join(res))
