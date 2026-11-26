from sys import stdin
#EN :foriner

#input for, want en

d=stdin.read().split('\n')
ever=False
translate={}
for line in d:
    if not ever and line=='':
        ever=True
        continue
    if line=='':
        continue
    if not ever:
        a,b=line.split()
        translate[b]=a
    else:
        a=line
        print(translate.get(a,'eh'))
'''
dog ogday
cat latcay
pig igpay
froot ootfray
loops oopslay
kitten abooskay
paper koopsmay

latcay
ittenkay
oopslay
abooskay
kitten
booskay
koopsmay
'''