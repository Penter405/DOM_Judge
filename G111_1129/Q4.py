from sys import stdin
d=stdin.read().split("\n")
for line in d:
    if line=="":
        continue
    line=list(line.lower())
    if len(line)%2==0:
        print(line[0],line[len(line)//2-1]+line[len(line)//2],line[-1],sep=",")

    else:
        print(line[0],line[len(line)//2],line[-1],sep=",")