"""
chr  str-> int
ord int -> str
"""
def get():
    n=int(input())
    if 65<=n<=90 :
        return 1
    elif 97<=n<=122 :
        return 2
    else:
        return 0

print(get())