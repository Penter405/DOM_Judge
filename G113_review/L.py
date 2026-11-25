from itertools import permutations
d=[str(a) for a in range(1,int(input())+1)]
now=list(permutations(d))
now.sort(reverse=True)
for line in now:
    print(''.join(line))