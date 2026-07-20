self_win=dict()
def get():
    for rs in ["YX","XO","OY"]:
        self_win[rs[0]]=rs[1]
        
    a=input()
    b=input()
    c=input()
    if a!=b and b!=c:
        return 0
    if a==b and a==c:
        return 0
    if a==b:
        if self_win[a]==c:
            return "1,2"
        return 3
    elif b==c:
        if self_win[b]==a:
            return "2,3"
        return 1
    else:
        if self_win[c]==b:
            return "1,3"
        return 2
print(get())