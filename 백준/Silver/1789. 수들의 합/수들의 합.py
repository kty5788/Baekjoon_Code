s = int(input())
num = 0
cnt = 0
for i in range(1,s+1):
    if 2*i + 1 > s-num:
        cnt += 1
        break
    elif num == s:
        break
    else:
        cnt += 1
        num += i

print(cnt)