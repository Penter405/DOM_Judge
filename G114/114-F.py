"""
two string find sub sequence
"""
s2="hello"
s1=input()

dp=[[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
#dp 1 indexed to avoid under 0 index if 0-1
def legal():
    for y in range(1,len(s1)+1):
        for x in range(1,len(s2)+1):
            same=0
            if s1[y-1]==s2[x-1]:
                same=1
            now=max(same+dp[y-1][x-1],dp[y][x-1],dp[y-1][x])
            if now==5:
                return True
            dp[y][x]=now
    return False

if legal():
    print("YES")
else:
    print("NO")