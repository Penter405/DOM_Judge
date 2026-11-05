s="hello"
did=-1
for rs in input():
    see=did+1
    if see==len(s):
        break
    if s[see]==rs:
        did+=1
if did+1==len(s):
    print("YES")
else:
    print("NO")