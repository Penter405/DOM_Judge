from collections import deque
"""
x 與 y 皆相同才視為同一個檔案
"""
trash=deque()
sizeof=int(input())
size=set()
now=0
while True:
    try:
        d=input()
    except:
        break
    name,fat=d.split()
    name=int(name)
    fat=int(fat)
    if (name,fat) in size:#hand remove
        now-=fat
        size.remove((name,fat))
        trash.remove((name,fat))#make sure item really removed
        continue
    while now+fat>sizeof:#remove ancient item
        see,sfat=trash.popleft()
        now-=sfat
        size.remove((see,sfat))
    now+=fat
    size.add((name,fat))
    trash.append((name,fat))
        
ever=False
while trash:
    see,fat=trash.popleft()
    ever=True
    print(see,fat)
if not ever:
    print("None")