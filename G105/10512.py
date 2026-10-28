while False:
    d="""0 ----- (Dah-Dah-Dah-Dah-Dah)
    1 .---- (DiW-Dah-Dah-Dah-Dah)
    2 ..--- (DiW-DiW-Dah-Dah-Dah)
    3 ...-- (DiW-DiW-DiW-Dah-Dah)
    4 ....- (DiW-DiW-DiW-DiW-Dah)
    5 ..... (DiW-DiW-DiW-DiW-DiW)
    6 -.... (Dah-DiW-DiW-DiW-DiW)
    7 --... (Dah-Dah-DiW-DiW-DiW)
    8 ---.. (Dah-Dah-Dah-DiW-DiW)
    9 ----. (Dah-Dah-Dah-Dah-""".split("\n")
    now=[]
    for rs in d:
        now.append(rs[2:7])

    print(now)

now=['-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']

get=dict()
for rs in range(10):
    get[now[rs]]=rs

res=[]

for _ in range(int(input())):
    d=input().replace(" ","")
    buffer=[]
    for rs in range(0,len(d),5):
        buffer.append(str(get[d[rs:rs+5]]))
    res.append("".join(buffer))

for rs in res:
    print(rs)