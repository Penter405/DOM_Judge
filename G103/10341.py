res=[]
back=dict()
get=dict()
s="""00 0
01 1
100 2
101 3
1100 4
1101 5
11100 6
11101 7
111100 8
111101 9"""
def find(s):
    seeing=back[s[0]]
    for rs in s[1:]:
        seeing=seeing[rs]
    return seeing
        


for rs in s.split("\n"):
    b,i=rs.split()
    i=int(i)
    seeing=None
    if b[0] not in back:
        back[b[0]]=dict()
    seeing=back[b[0]]
    for me in b[1:-1]:
        if me not in seeing:
            seeing[me]=dict()
        seeing=seeing[me]
    seeing[b[-1]]=i

ss="D E F G H I J K L M N O PQ R S T U V W X Y Z A B C".replace(" ","")

for rs in range(len(ss)):
    get[str(1+rs).zfill(2)]=ss[rs]



        

d=[]
for _ in range(int(input())):
    d.append(input())

for rs in d:
    r=[]
    see=None
    for me in rs:
        if see==None:
            see=back[me]
            continue
        if type(see[me])==int:
            r.append(str(see[me]))
            see=None
        else:
            see=see[me]
    res.append(get["".join(r)])

for rs in res:
    print(rs)
