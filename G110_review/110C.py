from sys import stdin
me=stdin.read().split('\n')
for line in me:
    if line=='':
        continue
    status=-1
    res=int(line[0])
    for char in line[1:]:
        i=int(char)
        status*=-1
        res+=i*status
    print(res)
