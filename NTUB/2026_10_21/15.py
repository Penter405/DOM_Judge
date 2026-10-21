dp=set()
while True:
     

"""
def get_diff(a,b,c):
    return 0,b-a,c-a
size=list(map(int,input().split()))
dp=[[ [False for _ in range(size[2]+1)] for _ in range(size[1]+1)  ] for _ in range(size[0]+1)]
dp[0][0][0]=True
for see1 in range(size[0]+1):
    for see2 in range(size[1]+1):
        for see3 in range(size[2]+1):
            for a1,a2,a3 in [[2,1,0],[0,2,3]]:
                if dp[see1][see2][see3]==True:
                    break
                if see1-a1>=0 and see2-a2>=0 and see3-a3>=0 and dp[see1-a1][see2-a2][see3-a3]==True:
                    dp[see1][see2][see3]=True
                    break
if dp[-1][-1][-1]==True:
    print("YES")
else:
    print("NO")
"""
"""
size=list(map(int,input().split()))
def cheak():
    dp=[(0,0,0)]
    while True:
        now=[]
        for u1,u2,u3 in dp:
            for a1,a2,a3 in [[2,1,0],[1,1,1],[0,2,3]]:
                if u1+a1<=size[0] and u2+a2<=size[1] and u3+a3<=size[2]:
                    if u1+a1==size[0] and u2+a2==size[1] and u3+a3==size[2]:
                        return True
                    now.append((u1+a1,u2+a2,u3+a3))
            if len(now)==0:
                return False 
            for good in now:
                dp.append(good)
            now.clear()
        return False

if cheak():
    print("YES")
else:
    print("NO")

"""