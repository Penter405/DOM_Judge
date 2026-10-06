res=[]
for _ in range(int(input())):
    d=input()
    ans=[]
    time=[]
    for rs in d[::-1]:
        if "0"<=rs<="9":
            time.append(rs)
        else:
            ans.append(rs* int("".join(time[::-1])))
            time.clear()
    res.append("".join(ans[::-1]))

print("\n".join(res))