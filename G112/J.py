times=int(input())
"""
0123456789
6255456376
try get most int
or get large int


dp=used part, and get most int
"""

res=[]
def get():
    want=int(input())
    if want%2==0:
        res.append("1"*(want//2))
    else:
        tar=(want-3)//2
        res.append("7"+"1"*tar)


for _ in range(times):
    get()


print("\n".join(res))
