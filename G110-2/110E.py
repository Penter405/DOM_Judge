tran=dict()#get eng: unknown, need unknown as key

while True:
    data=input()
    if data=='':
        break
    data=data.split()
    tran[data[1]]=data[0]

result=[]

while True:
    try:
        data=input()
    except:
        break
    if data in tran:
        result.append(tran[data])
    else:
        result.append('eh')

print("\n".join(result))
"""
dog ogday
cat atcay
pig igpay
froot ootfray
loops oopslay

atcay
ittenkay
oopslay
"""