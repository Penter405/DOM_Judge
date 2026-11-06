from sys import stdin
d=stdin.read().split("\n")
for line in d:
    if line=="":
        continue
    array,target=line.split()
    target=int(target)
    array=list(map(int,array.split(",")))
    done=False
    for a in range(len(array)):
        if done:
            break

        for b in range(a+1,len(array)):
            if array[a]+array[b]==target:
                print(a,b,sep=",")
                done=True
                break