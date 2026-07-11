seeing=-1#next num will be delete index
last=0#will be add index
answer=0
s=list(map(int,list(input())))
count=0
ever=set()
while True:
    if count==10 and tuple(s[seeing:last]) not in ever:
        ever.add(tuple(s[seeing:last]))
        answer+=1
    if last>len(s)-1:
        #index out and can not get answer anymore
        break
    if count<10:
        count+=s[last]
        last+=1
    else:
        seeing+=1
        count-=s[seeing]
print(answer)
#12345131
