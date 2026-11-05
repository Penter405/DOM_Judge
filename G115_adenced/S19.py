mu=set("aoyeui")
imnot=[]
for rs in input().lower():
    if rs not in mu:
        imnot.append("."+rs)
print("".join(imnot))