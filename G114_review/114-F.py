s="hello"
now=0
for char in input():
    if now==len(s):
        break
    if s[now]==char:
        now+=1
if now==len(s):
    print("YES")
else:
    print("NO")