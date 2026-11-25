win={
    'I':34,
    'O':35,
    'W':32,
    'Z':33
}
now=10

for ind in range(26):
    char=chr(65+ind)
    if char in win:
        continue
    win[char]=now
    now+=1

d=input()
res=win[d[0]]
res=res//10+(res%10)*9
now=9
for char in d[1:]:
    i=int(char)
    now-=1
    now=max(now,1)
    res+=i*now
if res%10==0:
    print("Y")
else:
    print("N")