dp = [0,1]

for i in range(2,491):
    dp.append(dp[i-2]+dp[i-1])

while True:
    n = int(input())
    if n == -1:
        break
    else:
        print(f'Hour {n}: {dp[n]} cow(s) affected')