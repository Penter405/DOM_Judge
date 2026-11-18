t=int(input())
"""
addf
remove len-1 times

"""

res=[]
for _ in range(t):
    u=int(input())
    d=input()
    count=1
    repeat=0
    last=d[1]
    time=0
    for rs in range(0,len(d)-2):
        if d[rs]!=d[rs+2]:
            count+=1




    res.append(str(count))

print("\n".join(res))
"""

7
6
aaabcc
10
aaaaaaaaaa
6
abcdef
7
abacaba
6
cccfff
4
abba
5
ababa
"""
"""
2
69
tqwkcomrhawhlizimbvajzjbuifleqpnkbgondlwubfwsifgtdwxipnhrakdqywjxjemb
71
nhlisuruyheyckzarqkuxsrnpivuowgoryvhtnwazbwuwjoabumgmuqibwmdoagpubfimbj
"""