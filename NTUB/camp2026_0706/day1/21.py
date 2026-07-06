all, missed=list(map(int,input().split()))
bot=0
if missed!=0:
    bot=sum(list(map(int,input().split())))
result=int((1+all)/2*all)-bot
if result>65535:
    print("PORT OVERFLOW")
else:
    print(int(result))
