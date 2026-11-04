from collections import Counter
"""
find appear same

"""

d=[]
while True:
    try:
        a=input()
        b=input()
    except:
        break
    d.append((a,b))

for a, b in d:
    a=dict(Counter(a))
    b=dict(Counter(b))
    buffer=[]
    for a_have in sorted(list(a.keys())):
        if a_have in b:
            amount=min(a[a_have],b[a_have])
            buffer.append(a_have*amount)
    print("".join(buffer))
"""
pretty
women
walking
down
the
street
"""