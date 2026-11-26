sizeof=int(input())
for _ in range(sizeof):
    d=int(input())
    if d%2==0:
        print('1'*(d//2))
    else:
        print('7'+'1'*((d-3)//2))
        