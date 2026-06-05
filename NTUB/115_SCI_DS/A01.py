result=0
n=int(input())
if n>=13:
    result+=(n-12)*150
    n=12
if n<13 and n>=7:
    result+=(n-6)*200
    n=6
if n<7 and n>=4:
    result+=(n-3)*250
    n=3
if n<=3:
    result+=n*300
print(result)