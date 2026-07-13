s=input()
ever=set()
seeing=0
#last=0
sizeof=0
result=0
for rs in s:
    while rs in ever:
        ever.remove(s[seeing])
        seeing+=1
        sizeof-=1
    #in the loop above us has sure that there will no second same value guy
    ever.add(rs)
    sizeof+=1
    if sizeof>result:
        result=sizeof
print(result)
#abcaabcde
#cbabcde
"""
we cant greedy by the second test case. only two pointer allowed
"""