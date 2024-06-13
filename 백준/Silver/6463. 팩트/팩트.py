dp = [1,1,2] + [0 for i in range(10000)]
for i in range(3,10001):
    dp[i] = dp[i-1] * i
while True:
    try:
        n = int(input())
        print(' '*(5-len(str(n))) + str(n), '-> ', end = '')
        for i in str(dp[n])[::-1]:
            if i != '0':
                print(i)
                break
    except:
        exit()