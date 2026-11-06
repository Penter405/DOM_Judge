from collections import Counter
d=input().lower().split()
now=Counter(d).most_common()
if len(now)>1 and now[0][1]==now[1][1]:
    print("No")
else:
    print(now[0][0],now[0][1])