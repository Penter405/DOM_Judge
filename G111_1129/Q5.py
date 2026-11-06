d=input().split()
for rs in range(2,len(d)-2):
    d[rs]="*"*len(d[rs])

print(" ".join(d))