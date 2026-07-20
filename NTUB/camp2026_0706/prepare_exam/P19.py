from collections import Counter
a=list(map(int,input().split(", ")))
b=list(map(int,input().split(", ")))
a.extend(b)

new=Counter(a)
ever=None
result=None
for n, appear in new.most_common():
    if ever==None or appear==ever:
        if result==None or n<result:
            result=n
            ever=appear
    elif appear>ever:
        result=n
        ever=appear
print(result)


"""
3, 2, 6, 4
2, 5, 4
"""