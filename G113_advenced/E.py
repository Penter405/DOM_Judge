s=input()
sizeof=len(s)
for data in s[::-1]:
    if int(data)%2!=0:
        break
    sizeof-=1
if sizeof==0:
    print(0)
else:
    print(s[:sizeof])