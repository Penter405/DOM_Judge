t=int(input())
"""
addf
remove len-1 times

"""
def get():
    u=int(input())
    d=input()
    count=set()
    for rs in range(u-1):
        if d[0:rs]+d[rs+2:] not in count:
            count.add( d[0:rs]+d[rs+2:]  )
    #print(count)
    return len(count)

res=[]
for _ in range(t):
    res.append(str(get()))

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