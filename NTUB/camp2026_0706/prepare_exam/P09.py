seeing=0#next num will be delete index
last=0#will be add index
answer=0
s=list(map(int,list(input())))
count=0
ever=set()
while True:
    if count==10 and tuple(s[seeing:last]) not in ever:
        #print(seeing,last)
        ever.add(tuple(s[seeing:last]))
        answer+=1
    if last>len(s)-1:
        #index out and can not get answer anymore
        break
    if count<10:
        count+=s[last]
        last+=1
    else:
        count-=s[seeing]
        seeing+=1
#print(ever)
print(answer)
#12345131

"""
X(不重複)    輸入一個字串，其內容都是數字。檢查該字串有多少個不重複「子字串」，其數
    字之和為 10?
    註:
    (1) 「子字串」是指一個字串「連續內容」的「部分」或「全部」
    (2) 若在本題的輸入字串中，有多個相同內容的子字串，只能算 1 次    
"""