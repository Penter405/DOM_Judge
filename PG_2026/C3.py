from sys import stdin
d=stdin.read()
now=[]
last_space=False
for data in d:
    if "0"<=data<="9":
        now.append(data)
        last_space=False
    else:
        if not last_space:
            now.append(" ")
        last_space=True

now=("".join(now)).split()
res=0
for rs in now:
    rs=rs[::-1]
    res+=int(rs)

print(res)