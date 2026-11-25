from collections import Counter
now=list(Counter(input()).most_common())
now.sort(key= lambda x:(x[1],-ord(x[0])))
for k,v in now:
    print(ord(k),v)