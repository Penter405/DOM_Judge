all, missed=list(map(int,input().split()))
result=int((1+all)/2*all)-sum(list(map(int,input().split())))
if result>65535:
    print("PORT OVERFLOW")
else:
    print(int(result))
