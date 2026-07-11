total=0
x=0
while True:
    s=input()
    if s=="-9999":
        break
    s=list(map(int,s.split()))
    x+=s[1]
    total+=s[0]*s[1]
print(x)
print(f"{total/x:.2f}")