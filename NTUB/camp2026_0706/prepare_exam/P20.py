from collections import Counter
votes=list()
for _ in range(int(input())):
    votes.append(int(input()))


ever=None
result=None
for n, appear in Counter(votes).most_common():
    if ever==None or appear==ever:
        if result==None or n<result:
            result=n
            ever=appear
    elif appear>ever:
        result=n
        ever=appear
print("{},{}".format(result,ever))
    