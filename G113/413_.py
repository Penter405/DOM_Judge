
data_size, interval_size=list(map(int,input().split()))
nums=list(map(int,input().split()))
dp=[[0  for _ in range(data_size+1)] for _ in range(data_size)]
#  [ )
for front in range(data_size):
    for back in range(data_size+1):
        dp[front][back]=