n = int(input())                    # 1. Takes the upper limit 'n'
dp = [0] * (n + 1)                  # 2. Allocates memory for results from 0 to n

for i in range(1, n + 1):           # 3. Loops through every number from 1 to n
    dp[i] = dp[i >> 1] + (1 & i)    # 4. DP Recurrence Relation

print(sum(dp))                      # 5. Sums all set bits from 0 to n