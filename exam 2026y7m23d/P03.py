s=input().split()
new=[]
for rs in s:
    new.append(rs[0].upper()+rs[1:].lower())
print(" ".join(new))