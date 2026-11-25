table={'I':34,'O':35,'W':32,'Z':33}
now=10
for index in range(26):
    index+=65
    char=chr(index)
    if char in table:
        continue
    table[char]=now
    now+=1

d=list(map(int,input()))
now=0
time=9
for i in d:
    time-=1
    time=max(time,1)
    now+=time*i
result=[]
for index in range(26):
    value=table[chr(65+index)]
    value=value//10+(value%10)*9
    if (value+now)%10==0:
        result.append(chr(65+index))
print(''.join(result))