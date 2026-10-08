n=int(input())
appear1=[0]*(n+1)
res=0
for rs in range(1,n+1):
    bot=0
    if rs%2==1:
        bot=1
    appear1[rs]=appear1[rs>>1]+bot
    res+=appear1[rs]

print(res)
    