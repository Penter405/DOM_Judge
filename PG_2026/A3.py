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
for index,d in enumerate(input()):
    res.append(new(d,index))

print("".join(res))