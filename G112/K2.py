t=int(input())
"""
addf
remove len-1 times

"""

res=[]
for _ in range(t):
    u=int(input())
    d=input()
    count=0
    repeat=0
    last=d[1]
    time=0
    for rs in range(0,len(d)):
        if rs==0:
            last=d[rs]
            repeat+=1
            count+=1
            continue
        if last==d[rs]:
            if repeat>=1:
                pass
            else:
                count+=1
            repeat+=1
        else:
            count+=1
            repeat=0




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