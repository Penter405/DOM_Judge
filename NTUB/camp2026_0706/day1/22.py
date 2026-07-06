from collections import Counter
def get():
    s=Counter(input().split())
    bot=dict(s.most_common())
    for rs in bot:
        if bot[rs]%2!=0:
            return rs
        
print(get())