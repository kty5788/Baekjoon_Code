dp = [1,1]

for i in range(2,46):
    dp.append(dp[i-2]+dp[i-1])

n = int(input())
for i in range(n):
    number = int(input())
    print(dp[number])