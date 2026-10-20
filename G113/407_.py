from itertools import permutations
n=int(input())
x=list(permutations(list(range(1,n+1))))
x.sort(reverse=True)
for rs in x:
    print("".join(list(map(str,rs))))