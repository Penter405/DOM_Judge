win={
    'Y':'X',
    'O':'Y',
    'X':'O'
}
a,b=input().split()
if win[a]==b:
    print(1)
elif a==b:
    print(0)
else:
    print(2)