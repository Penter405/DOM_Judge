order=[]
fib=[1]
large=0
for _ in range(int(input())):
    d=int(input())
    large=max(large,d)
    order.append(d)
index=0#that we are seeing
last=1
friend=1
new=None
while new==None or new<large:
    new=last+friend
    last=friend
    friend=new
    fib.append(new)
for want in order:
    buffer=[]
    bot=want
    ever=False
    for index in range(len(fib)-1,-1,-1):
        if bot-fib[index]>=0:
            buffer.append("1")
            bot-=fib[index]
            ever=True
        else:
            if ever:
                buffer.append("0")
    print("{}={}".format(want,"".join(buffer)))

