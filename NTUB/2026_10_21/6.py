want=int(input())
line=want-1
star=1

for _ in range(want):
    print("-"*line,"*"*star,"-"*line,sep="")
    line-=1
    star+=2
