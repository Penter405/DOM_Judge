def B(p1,p2):
    return (p2-p1)*2000

def S(p1,p2):
    return (p1-p2)*2000

status,st,back,promise=input().split()
st=int(st)
back=int(back)
promise=int(promise)
if status=="B":
    now=B(st,back)
else:
    now=S(st,back)

print(now)
print(f"{now*100/promise:.2f}")