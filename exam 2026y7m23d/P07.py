from collections import Counter
useless=int(input())
big=-1
for ele, times in Counter(list(map(int,input().split()))).most_common():
    if ele==times:
        if ele>big:
            big=ele
print(big)