win={
    "WF":'W',
    'FW':'W',
    'FG':'F',
    'GF':'F',
    'GW':'G',
    'WG':'G'
}
a=0
b=0
for _ in range(int(input())):
    bot=input()
    bot=bot.replace(' ','')
    if bot not in win:
        continue
    elif win[bot]==bot[0]:
        a+=1
    else:
        b+=1
print(a,b)