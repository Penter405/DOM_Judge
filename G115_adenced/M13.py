from itertools import permutations
me=int(input())
d=[n for n in range(1,me+1)]
good=list(permutations(d))
good.sort(reverse=True)


for rs in good:
    buffer=[]
    for pe in rs:
        buffer.append(str(pe))

    print("".join(buffer))